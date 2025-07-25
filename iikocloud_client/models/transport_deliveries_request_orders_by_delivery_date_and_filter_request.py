# coding: utf-8

"""
    iikoCloud API

    <h3>Description of common data formats:</h3><b>uuid</b> - string in UUID(universally unique identifier).<br/>Examples: <i>550e8400-e29b-41d4-a716-446655440000, b090de0b-8550-6e17-70b2-bbba152bcbd3</i><br/><br/><b>date-time</b> - date and time string in custom string format <b>yyyy-MM-dd HH:mm:ss.fff</b>.<br/>Examples: <i>2017-04-29 20:45:00.000, 2018-01-01 01:01:30.123</i>

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iikocloud_client.models.transport_common_sort_direction import TransportCommonSortDirection
from iikocloud_client.models.transport_deliveries_common_delivery_status import TransportDeliveriesCommonDeliveryStatus
from iikocloud_client.models.transport_deliveries_request_create_order_order_service_type import TransportDeliveriesRequestCreateOrderOrderServiceType
from iikocloud_client.models.transport_deliveries_request_order_sort_property import TransportDeliveriesRequestOrderSortProperty
from typing import Optional, Set
from typing_extensions import Self

class TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest(BaseModel):
    """
    Request for information about orders from external source and based on additional filters.
    """ # noqa: E501
    organization_ids: List[StrictStr] = Field(description="Organization ID for which an order search will be performed.                Can be obtained by `/api/1/organizations` operation.", alias="organizationIds")
    terminal_group_ids: Optional[List[StrictStr]] = Field(default=None, description="List of terminal groups IDs.", alias="terminalGroupIds")
    delivery_date_from: Optional[StrictStr] = Field(default=None, description="Order delivery date (Local for delivery terminal). Lower limit.                The guaranteed order availability period is the last 7 days. To access earlier orders, use the `/api/1/deliveries/history/by_delivery_date_and_phone` method.", alias="deliveryDateFrom")
    delivery_date_to: Optional[StrictStr] = Field(default=None, description="Order delivery date (Local for delivery terminal). Upper limit.", alias="deliveryDateTo")
    statuses: Optional[List[TransportDeliveriesCommonDeliveryStatus]] = Field(default=None, description="Allowed order statuses.")
    has_problem: Optional[StrictBool] = Field(default=None, description="If true, delivery has a problem.  > Conditions under which the order has a problem:  > * order.problem.hasProblem is true;  > * order status is Unconfirmed and CookingStartTime before now;  > * order status is ReadyForCooking and (CookingStartTime + timeToCookingErrorTimeout) before now;  > * order status is CookingCompleted or Waiting and (CookingStartTime + cookingTimeout) before now.", alias="hasProblem")
    order_service_type: Optional[TransportDeliveriesRequestCreateOrderOrderServiceType] = Field(default=None, description="Order service type.", alias="orderServiceType")
    search_text: Optional[StrictStr] = Field(default=None, description="Value for search. Used for prefix search.", alias="searchText")
    time_to_cooking_error_timeout: Optional[StrictInt] = Field(default=None, description="Error timeout for status time to cooking, in seconds.", alias="timeToCookingErrorTimeout")
    cooking_timeout: Optional[StrictInt] = Field(default=None, description="Expected cooking time, in seconds.", alias="cookingTimeout")
    sort_property: Optional[TransportDeliveriesRequestOrderSortProperty] = Field(default=None, description="Sorting property.", alias="sortProperty")
    sort_direction: Optional[TransportCommonSortDirection] = Field(default=None, description="Sorting direction.", alias="sortDirection")
    rows_count: Optional[StrictInt] = Field(default=None, description="Maximum number of items returned.", alias="rowsCount")
    source_keys: Optional[List[StrictStr]] = Field(default=None, description="Source keys.", alias="sourceKeys")
    order_ids: Optional[List[StrictStr]] = Field(default=None, description="Order IDs.                > Must be null if \"posOrderIds\" is not null.", alias="orderIds")
    pos_order_ids: Optional[List[StrictStr]] = Field(default=None, description="POS order IDs.                > Must be null if \"orderIds\" is not null.", alias="posOrderIds")
    __properties: ClassVar[List[str]] = ["organizationIds", "terminalGroupIds", "deliveryDateFrom", "deliveryDateTo", "statuses", "hasProblem", "orderServiceType", "searchText", "timeToCookingErrorTimeout", "cookingTimeout", "sortProperty", "sortDirection", "rowsCount", "sourceKeys", "orderIds", "posOrderIds"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if terminal_group_ids (nullable) is None
        # and model_fields_set contains the field
        if self.terminal_group_ids is None and "terminal_group_ids" in self.model_fields_set:
            _dict['terminalGroupIds'] = None

        # set to None if delivery_date_from (nullable) is None
        # and model_fields_set contains the field
        if self.delivery_date_from is None and "delivery_date_from" in self.model_fields_set:
            _dict['deliveryDateFrom'] = None

        # set to None if delivery_date_to (nullable) is None
        # and model_fields_set contains the field
        if self.delivery_date_to is None and "delivery_date_to" in self.model_fields_set:
            _dict['deliveryDateTo'] = None

        # set to None if statuses (nullable) is None
        # and model_fields_set contains the field
        if self.statuses is None and "statuses" in self.model_fields_set:
            _dict['statuses'] = None

        # set to None if has_problem (nullable) is None
        # and model_fields_set contains the field
        if self.has_problem is None and "has_problem" in self.model_fields_set:
            _dict['hasProblem'] = None

        # set to None if order_service_type (nullable) is None
        # and model_fields_set contains the field
        if self.order_service_type is None and "order_service_type" in self.model_fields_set:
            _dict['orderServiceType'] = None

        # set to None if search_text (nullable) is None
        # and model_fields_set contains the field
        if self.search_text is None and "search_text" in self.model_fields_set:
            _dict['searchText'] = None

        # set to None if source_keys (nullable) is None
        # and model_fields_set contains the field
        if self.source_keys is None and "source_keys" in self.model_fields_set:
            _dict['sourceKeys'] = None

        # set to None if order_ids (nullable) is None
        # and model_fields_set contains the field
        if self.order_ids is None and "order_ids" in self.model_fields_set:
            _dict['orderIds'] = None

        # set to None if pos_order_ids (nullable) is None
        # and model_fields_set contains the field
        if self.pos_order_ids is None and "pos_order_ids" in self.model_fields_set:
            _dict['posOrderIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransportDeliveriesRequestOrdersByDeliveryDateAndFilterRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "organizationIds": obj.get("organizationIds"),
            "terminalGroupIds": obj.get("terminalGroupIds"),
            "deliveryDateFrom": obj.get("deliveryDateFrom"),
            "deliveryDateTo": obj.get("deliveryDateTo"),
            "statuses": obj.get("statuses"),
            "hasProblem": obj.get("hasProblem"),
            "orderServiceType": obj.get("orderServiceType"),
            "searchText": obj.get("searchText"),
            "timeToCookingErrorTimeout": obj.get("timeToCookingErrorTimeout"),
            "cookingTimeout": obj.get("cookingTimeout"),
            "sortProperty": obj.get("sortProperty"),
            "sortDirection": obj.get("sortDirection"),
            "rowsCount": obj.get("rowsCount"),
            "sourceKeys": obj.get("sourceKeys"),
            "orderIds": obj.get("orderIds"),
            "posOrderIds": obj.get("posOrderIds")
        })
        return _obj


