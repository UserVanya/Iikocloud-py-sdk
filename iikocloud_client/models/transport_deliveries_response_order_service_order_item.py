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

from pydantic import ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from iikocloud_client.models.transport_deliveries_response_order_combo_item_information import TransportDeliveriesResponseOrderComboItemInformation
from iikocloud_client.models.transport_deliveries_response_order_item_deleted_info import TransportDeliveriesResponseOrderItemDeletedInfo
from iikocloud_client.models.transport_deliveries_response_order_order_item import TransportDeliveriesResponseOrderOrderItem
from iikocloud_client.models.transport_deliveries_response_order_order_item_status import TransportDeliveriesResponseOrderOrderItemStatus
from iikocloud_client.models.transport_deliveries_response_order_product import TransportDeliveriesResponseOrderProduct
from iikocloud_client.models.transport_deliveries_response_order_product_size import TransportDeliveriesResponseOrderProductSize
from typing import Optional, Set
from typing_extensions import Self

class TransportDeliveriesResponseOrderServiceOrderItem(TransportDeliveriesResponseOrderOrderItem):
    """
    Order item: service.
    """ # noqa: E501
    service: TransportDeliveriesResponseOrderProduct = Field(description="Item.")
    cost: Union[StrictFloat, StrictInt] = Field(description="Total cost per item without tax, discounts/surcharges.")
    __properties: ClassVar[List[str]] = ["type", "status", "deleted", "amount", "comment", "whenPrinted", "size", "comboInformation"]

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
        """Create an instance of TransportDeliveriesResponseOrderServiceOrderItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of deleted
        if self.deleted:
            _dict['deleted'] = self.deleted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of size
        if self.size:
            _dict['size'] = self.size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of combo_information
        if self.combo_information:
            _dict['comboInformation'] = self.combo_information.to_dict()
        # set to None if deleted (nullable) is None
        # and model_fields_set contains the field
        if self.deleted is None and "deleted" in self.model_fields_set:
            _dict['deleted'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if when_printed (nullable) is None
        # and model_fields_set contains the field
        if self.when_printed is None and "when_printed" in self.model_fields_set:
            _dict['whenPrinted'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if combo_information (nullable) is None
        # and model_fields_set contains the field
        if self.combo_information is None and "combo_information" in self.model_fields_set:
            _dict['comboInformation'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransportDeliveriesResponseOrderServiceOrderItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "status": obj.get("status"),
            "deleted": TransportDeliveriesResponseOrderItemDeletedInfo.from_dict(obj["deleted"]) if obj.get("deleted") is not None else None,
            "amount": obj.get("amount"),
            "comment": obj.get("comment"),
            "whenPrinted": obj.get("whenPrinted"),
            "size": TransportDeliveriesResponseOrderProductSize.from_dict(obj["size"]) if obj.get("size") is not None else None,
            "comboInformation": TransportDeliveriesResponseOrderComboItemInformation.from_dict(obj["comboInformation"]) if obj.get("comboInformation") is not None else None
        })
        return _obj


