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

from pydantic import ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from iikocloud_client.models.transport_deliveries_common_gender import TransportDeliveriesCommonGender
from iikocloud_client.models.transport_deliveries_request_create_order_customer import TransportDeliveriesRequestCreateOrderCustomer
from typing import Optional, Set
from typing_extensions import Self

class TransportDeliveriesRequestCreateOrderRegularCustomer(TransportDeliveriesRequestCreateOrderCustomer):
    """
    'Regular' customer:  - can be used only if a customer agrees to take part in the store's loyalty programs  - customer details will be added (updated) to the store's customer database  - benefits (accumulation of rewards, etc.) of active loyalty programs will be made available to the customer
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Existing customer ID in RMS.   > If null - the phone number is searched in database, otherwise the new customer is created in RMS.")
    name: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, description="Name of customer.  > Required for new customers (i.e. if \"id\" == null)  > Not required if \"id\" specified.")
    surname: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, description="Last name.")
    comment: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, description="Comment.")
    birthdate: Optional[StrictStr] = Field(default=None, description="Date of birth.")
    email: Optional[StrictStr] = Field(default=None, description="Email.")
    should_receive_promo_actions_info: Optional[StrictBool] = Field(default=None, description="Deprecated, use \"shouldReceiveOrderStatusNotifications\" instead.", alias="shouldReceivePromoActionsInfo")
    should_receive_order_status_notifications: Optional[StrictBool] = Field(default=None, description="Whether customer receives order status notification messages.", alias="shouldReceiveOrderStatusNotifications")
    gender: Optional[TransportDeliveriesCommonGender] = Field(default=None, description="Gender.")
    __properties: ClassVar[List[str]] = ["type"]

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
        """Create an instance of TransportDeliveriesRequestCreateOrderRegularCustomer from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransportDeliveriesRequestCreateOrderRegularCustomer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type")
        })
        return _obj


