"""Exact executable registry for every reviewed automatic iiko read."""

from tests.integration.read.cases.addresses import ADDRESS_CASES
from tests.integration.read.cases.deliveries import DELIVERY_CASES
from tests.integration.read.cases.employees import EMPLOYEE_CASES
from tests.integration.read.cases.finance import FINANCE_CASES
from tests.integration.read.cases.foundation import FOUNDATION_CASES
from tests.integration.read.cases.inventory import INVENTORY_CASES
from tests.integration.read.cases.loyalty import LOYALTY_CASES
from tests.integration.read.cases.menu import MENU_CASES
from tests.integration.read.cases.reserves_orders import RESERVE_ORDER_CASES
from tools.openapi_pipeline.live.read_case import ReadCase
from tools.openapi_pipeline.live.read_planner import ReadPlan

ALL_READ_CASES: tuple[ReadCase, ...] = (
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

FULL_READ_PLAN = ReadPlan.build(ALL_READ_CASES)

__all__ = ["ALL_READ_CASES", "FULL_READ_PLAN"]
