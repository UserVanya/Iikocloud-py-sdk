from __future__ import annotations

import dataclasses
import hashlib
import inspect
import json
from itertools import permutations
from typing import Any, cast, get_args, get_type_hints

import pytest

from iikocloud_client import api as generated_api
from tests.integration.read.cases import ALL_READ_CASES, FULL_READ_PLAN
from tests.integration.read.cases.addresses import ADDRESS_CASES
from tests.integration.read.cases.deliveries import DELIVERY_CASES
from tests.integration.read.cases.employees import EMPLOYEE_CASES
from tests.integration.read.cases.finance import FINANCE_CASES
from tests.integration.read.cases.foundation import FOUNDATION_CASES
from tests.integration.read.cases.inventory import INVENTORY_CASES
from tests.integration.read.cases.loyalty import LOYALTY_CASES
from tests.integration.read.cases.menu import MENU_CASES
from tests.integration.read.cases.reserves_orders import RESERVE_ORDER_CASES
from tools.openapi_pipeline.live.read_case import (
    NO_REQUEST,
    GeneratedReadBinding,
    NoLiveTargetCode,
    ReadCase,
)
from tools.openapi_pipeline.live.read_planner import ReadPlan

_POLYMORPHIC_REQUEST_MODELS = {
    "get_customer_info_with_http_info": (
        "iikocloud_client.models.get_customer_info_by_id_request",
        "GetCustomerInfoByIdRequest",
    ),
}


def _assert_binding_matches_generated_declaration(
    binding: GeneratedReadBinding,
) -> None:
    matches = tuple(
        api_class
        for _, api_class in inspect.getmembers(generated_api, inspect.isclass)
        if api_class.__module__.startswith("iikocloud_client.api.")
        and binding.method_name in vars(api_class)
    )
    assert len(matches) == 1
    api_class = matches[0]
    assert (binding.api_module, binding.api_class) == (
        api_class.__module__,
        api_class.__name__,
    )

    method = getattr(api_class, binding.method_name)
    request_parameters = tuple(
        parameter
        for parameter in inspect.signature(method).parameters.values()
        if parameter.name not in {"self", "timeout"} and not parameter.name.startswith("_")
    )
    assert len(request_parameters) <= 1
    expected_request: tuple[str | None, str | None, str | None]
    if not request_parameters:
        expected_request = (None, None, None)
    else:
        request_parameter = request_parameters[0]
        pending_annotations = [get_type_hints(method)[request_parameter.name]]
        request_models: set[type[object]] = set()
        while pending_annotations:
            annotation = pending_annotations.pop()
            if inspect.isclass(annotation) and annotation.__module__.startswith(
                "iikocloud_client.models."
            ):
                request_models.add(annotation)
            pending_annotations.extend(get_args(annotation))
        assert len(request_models) == 1
        annotated_request_model = request_models.pop()
        request_module, request_class = _POLYMORPHIC_REQUEST_MODELS.get(
            binding.method_name,
            (annotated_request_model.__module__, annotated_request_model.__name__),
        )
        expected_request = (
            request_module,
            request_class,
            request_parameter.name,
        )
    assert (
        binding.request_module,
        binding.request_class,
        binding.request_keyword,
    ) == expected_request
    resolved = binding.resolve()
    if binding.method_name in _POLYMORPHIC_REQUEST_MODELS:
        assert resolved.request_class is not None
        assert issubclass(resolved.request_class, annotated_request_model)


def _case(
    operation_id: str,
    *,
    revision: int = 1,
    depends_on: tuple[str, ...] = (),
    requires: tuple[str, ...] = (),
    provides: tuple[str, ...] = (),
    allowed_no_target_codes: frozenset[NoLiveTargetCode] = frozenset(),
) -> ReadCase:
    return ReadCase(
        operation_id=operation_id,
        revision=revision,
        depends_on=depends_on,
        requires=requires,
        provides=provides,
        allowed_no_target_codes=allowed_no_target_codes,
        binding=GeneratedReadBinding(
            api_module=f"iikocloud_client.api.{operation_id}_api",
            api_class="SyntheticApi",
            method_name=f"{operation_id}_with_http_info",
            request_module=None,
            request_class=None,
            request_keyword=None,
        ),
        build_values=lambda _view: NO_REQUEST,
        validate_response=lambda _response, _view: None,
        extract=lambda _response, _view: {},
    )


def _dag_cases() -> tuple[ReadCase, ...]:
    root = _case("root", provides=("root_key",))
    alpha = _case(
        "alpha",
        depends_on=("root",),
        requires=("root_key",),
        provides=("alpha_key",),
    )
    beta = _case(
        "beta",
        depends_on=("root",),
        requires=("root_key",),
        provides=("beta_key",),
    )
    leaf = _case(
        "leaf",
        depends_on=("alpha", "beta"),
        requires=("alpha_key", "beta_key"),
    )
    return root, alpha, beta, leaf


def _expected_registry_sha256(cases: tuple[ReadCase, ...]) -> str:
    descriptor = {
        "version": 1,
        "cases": [
            {
                "operation_id": case.operation_id,
                "revision": case.revision,
                "depends_on": list(case.depends_on),
                "requires": list(case.requires),
                "provides": list(case.provides),
                "allowed_no_target_codes": sorted(
                    code.value for code in case.allowed_no_target_codes
                ),
                "binding": dataclasses.asdict(case.binding),
            }
            for case in sorted(cases, key=lambda item: item.operation_id)
        ],
    }
    encoded = (
        json.dumps(
            descriptor,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
        + b"\n"
    )
    return hashlib.sha256(encoded).hexdigest()


def test_build_orders_each_kahn_layer_lexicographically_for_every_input_order() -> None:
    cases = _dag_cases()

    for shuffled in permutations(cases):
        plan = ReadPlan.build(shuffled)

        assert plan.ordered_operation_ids == ("root", "alpha", "beta", "leaf")
        assert tuple(case.operation_id for case in plan.cases) == (
            "root",
            "alpha",
            "beta",
            "leaf",
        )


def test_build_does_not_mix_newly_unlocked_cases_into_current_kahn_layer() -> None:
    root = _case("root", provides=("root_key",))
    zeta = _case("zeta")
    alpha = _case(
        "alpha",
        depends_on=("root",),
        requires=("root_key",),
    )

    plan = ReadPlan.build((alpha, zeta, root))

    assert plan.ordered_operation_ids == ("root", "zeta", "alpha")


def test_registry_hash_uses_exact_canonical_operation_sorted_descriptor() -> None:
    root, alpha, beta, leaf = _dag_cases()
    revised_beta = _case(
        "beta",
        revision=4,
        depends_on=("root",),
        requires=("root_key",),
        provides=("beta_key",),
        allowed_no_target_codes=frozenset({NoLiveTargetCode.PRODUCT, NoLiveTargetCode.CITY}),
    )
    cases = (leaf, revised_beta, root, alpha)

    plan = ReadPlan.build(cases)

    assert plan.registry_sha256 == _expected_registry_sha256(cases)
    assert len(plan.registry_sha256) == 64
    assert plan.registry_sha256 != _expected_registry_sha256((root, alpha, beta, leaf))


def test_plan_and_case_lookup_are_immutable() -> None:
    root, alpha, beta, leaf = _dag_cases()
    plan = ReadPlan.build((root, alpha, beta, leaf))

    assert plan.case_for("alpha") is alpha
    with pytest.raises(dataclasses.FrozenInstanceError):
        cast(Any, plan).registry_sha256 = "changed"
    with pytest.raises(TypeError):
        cast(Any, plan)._case_lookup["other"] = root


def test_seed_required_key_needs_no_dependency_provider() -> None:
    seeded = _case("seeded", requires=("profile_organization_id",))

    plan = ReadPlan.build((seeded,))

    assert plan.ordered_operation_ids == ("seeded",)


def test_build_rejects_duplicate_operation_ids() -> None:
    duplicate_a = _case("duplicate")
    duplicate_b = _case("duplicate", revision=2)

    with pytest.raises(Exception, match="duplicate"):
        ReadPlan.build((duplicate_a, duplicate_b))


def test_build_rejects_missing_dependency() -> None:
    child = _case("child", depends_on=("missing",))

    with pytest.raises(Exception, match="dependency"):
        ReadPlan.build((child,))


def test_build_rejects_self_dependency() -> None:
    self_dependent = _case("self_dependent", depends_on=("self_dependent",))

    with pytest.raises(Exception, match="self"):
        ReadPlan.build((self_dependent,))


def test_build_rejects_dependency_cycle() -> None:
    alpha = _case("alpha", depends_on=("beta",))
    beta = _case("beta", depends_on=("alpha",))

    with pytest.raises(Exception, match="cycle"):
        ReadPlan.build((alpha, beta))


def test_build_rejects_dependency_without_required_key_provider() -> None:
    root = _case("root", provides=("different_key",))
    child = _case(
        "child",
        depends_on=("root",),
        requires=("required_key",),
    )

    with pytest.raises(Exception, match="required"):
        ReadPlan.build((child, root))


def test_build_rejects_required_key_from_non_dependency() -> None:
    provider = _case("provider", provides=("required_key",))
    child = _case("child", requires=("required_key",))

    with pytest.raises(Exception, match="required"):
        ReadPlan.build((child, provider))


def test_build_rejects_duplicate_context_provider() -> None:
    alpha = _case("alpha", provides=("shared_key",))
    beta = _case("beta", provides=("shared_key",))
    leaf = _case(
        "leaf",
        depends_on=("alpha", "beta"),
        requires=("shared_key",),
    )

    with pytest.raises(Exception, match="provider"):
        ReadPlan.build((leaf, beta, alpha))


def test_case_for_and_dependency_closure_reject_unknown_operation() -> None:
    plan = ReadPlan.build(_dag_cases())

    with pytest.raises(Exception, match="operation"):
        plan.case_for("unknown")
    with pytest.raises(Exception, match="operation"):
        plan.dependency_closure("unknown")


def test_dependency_closure_keeps_only_transitive_dependencies_in_original_order() -> None:
    root, alpha, beta, leaf = _dag_cases()
    zeta = _case("zeta")
    plan = ReadPlan.build((leaf, beta, zeta, alpha, root))

    closure = plan.dependency_closure("leaf")

    assert plan.ordered_operation_ids == ("root", "zeta", "alpha", "beta", "leaf")
    assert closure.ordered_operation_ids == ("root", "alpha", "beta", "leaf")
    assert tuple(case.operation_id for case in closure.cases) == (
        "root",
        "alpha",
        "beta",
        "leaf",
    )
    assert closure.registry_sha256 == _expected_registry_sha256((root, alpha, beta, leaf))
    assert closure.registry_sha256 != plan.registry_sha256


def test_dependency_closure_for_root_contains_only_root() -> None:
    root, alpha, beta, leaf = _dag_cases()
    plan = ReadPlan.build((leaf, beta, alpha, root))

    closure = plan.dependency_closure("root")

    assert closure.ordered_operation_ids == ("root",)
    assert closure.cases == (root,)
    assert closure.registry_sha256 == _expected_registry_sha256((root,))


def test_real_read_registry_has_exact_domain_order_and_count() -> None:
    expected = (
        *FOUNDATION_CASES,
        *ADDRESS_CASES,
        *MENU_CASES,
        *DELIVERY_CASES,
        *RESERVE_ORDER_CASES,
        *EMPLOYEE_CASES,
        *LOYALTY_CASES,
        *FINANCE_CASES,
        *INVENTORY_CASES,
    )
    assert type(ALL_READ_CASES) is tuple
    assert expected == ALL_READ_CASES
    assert len(ALL_READ_CASES) == 91
    assert len(FULL_READ_PLAN.cases) == 91
    assert set(FULL_READ_PLAN.ordered_operation_ids) == {
        case.operation_id for case in ALL_READ_CASES
    }


def test_every_real_generated_binding_resolves_its_exact_request_contract() -> None:
    for case in ALL_READ_CASES:
        binding = case.binding
        _assert_binding_matches_generated_declaration(binding)
        resolved = binding.resolve()
        assert binding.method_name == f"{case.operation_id}_with_http_info"
        assert resolved.method.__name__ == binding.method_name
        assert resolved.api_class.__name__ == binding.api_class
        request_fields = (
            binding.request_module,
            binding.request_class,
            binding.request_keyword,
        )
        if binding.request_module is None:
            assert request_fields == (None, None, None)
            assert resolved.request_class is None
        else:
            assert all(type(value) is str and value for value in request_fields)
            assert resolved.request_class is not None
            assert resolved.request_class.__name__ == binding.request_class


def test_generated_declaration_check_rejects_a_dropped_request_triple() -> None:
    binding = next(
        case.binding for case in ALL_READ_CASES if case.binding.request_module is not None
    )
    broken = dataclasses.replace(
        binding,
        request_module=None,
        request_class=None,
        request_keyword=None,
    )

    with pytest.raises(AssertionError):
        _assert_binding_matches_generated_declaration(broken)


def test_real_registry_declares_every_expected_no_target_code() -> None:
    context_dependent = tuple(case for case in ALL_READ_CASES if case.allowed_no_target_codes)
    assert len(context_dependent) == 44
    assert all(case.depends_on and case.requires for case in context_dependent)
    assert frozenset(
        code for case in context_dependent for code in case.allowed_no_target_codes
    ) == frozenset(NoLiveTargetCode)
