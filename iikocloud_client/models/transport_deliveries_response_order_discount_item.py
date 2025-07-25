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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from iikocloud_client.models.transport_deliveries_response_order_discount_type import TransportDeliveriesResponseOrderDiscountType
from iikocloud_client.models.transport_deliveries_response_order_position_with_sum import TransportDeliveriesResponseOrderPositionWithSum
from typing import Optional, Set
from typing_extensions import Self

class TransportDeliveriesResponseOrderDiscountItem(BaseModel):
    """
    Discount.
    """ # noqa: E501
    discount_type: TransportDeliveriesResponseOrderDiscountType = Field(description="Discount type.                 Can be obtained by `/api/1/discounts` operation.", alias="discountType")
    sum: Union[StrictFloat, StrictInt] = Field(description="Total.")
    selective_positions: Optional[List[StrictStr]] = Field(default=None, description="Order item positions.", alias="selectivePositions")
    selective_positions_with_sum: Optional[List[TransportDeliveriesResponseOrderPositionWithSum]] = Field(default=None, description="Order item positions with position discount sum.   > Allowed from version `8.5.6`.", alias="selectivePositionsWithSum")
    __properties: ClassVar[List[str]] = ["discountType", "sum", "selectivePositions", "selectivePositionsWithSum"]

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
        """Create an instance of TransportDeliveriesResponseOrderDiscountItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of discount_type
        if self.discount_type:
            _dict['discountType'] = self.discount_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in selective_positions_with_sum (list)
        _items = []
        if self.selective_positions_with_sum:
            for _item_selective_positions_with_sum in self.selective_positions_with_sum:
                if _item_selective_positions_with_sum:
                    _items.append(_item_selective_positions_with_sum.to_dict())
            _dict['selectivePositionsWithSum'] = _items
        # set to None if selective_positions (nullable) is None
        # and model_fields_set contains the field
        if self.selective_positions is None and "selective_positions" in self.model_fields_set:
            _dict['selectivePositions'] = None

        # set to None if selective_positions_with_sum (nullable) is None
        # and model_fields_set contains the field
        if self.selective_positions_with_sum is None and "selective_positions_with_sum" in self.model_fields_set:
            _dict['selectivePositionsWithSum'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransportDeliveriesResponseOrderDiscountItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "discountType": TransportDeliveriesResponseOrderDiscountType.from_dict(obj["discountType"]) if obj.get("discountType") is not None else None,
            "sum": obj.get("sum"),
            "selectivePositions": obj.get("selectivePositions"),
            "selectivePositionsWithSum": [TransportDeliveriesResponseOrderPositionWithSum.from_dict(_item) for _item in obj["selectivePositionsWithSum"]] if obj.get("selectivePositionsWithSum") is not None else None
        })
        return _obj


