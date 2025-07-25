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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from iikocloud_client.models.net_customer_iiko_net_user_sex import NetCustomerIikoNetUserSex
from iikocloud_client.models.net_customer_personal_data_consent_status import NetCustomerPersonalDataConsentStatus
from typing import Optional, Set
from typing_extensions import Self

class NetCustomerCreateOrUpdateCustomerRequest(BaseModel):
    """
    Not empty `phone` or `magnetCardTrack` or `id` is required for successful import.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Customer id.")
    phone: Optional[StrictStr] = Field(default=None, description="Customer phone. Can be null.")
    card_track: Optional[StrictStr] = Field(default=None, description="Card track. Required if cardNumber set. Can be null.", alias="cardTrack")
    card_number: Optional[StrictStr] = Field(default=None, description="Card number. Required if cardTrack set. Can be null.", alias="cardNumber")
    name: Optional[StrictStr] = Field(default=None, description="Customer name. Can be null.")
    middle_name: Optional[StrictStr] = Field(default=None, description="Customer middle name. Can be null.", alias="middleName")
    sur_name: Optional[StrictStr] = Field(default=None, description="Customer surname. Can be null.", alias="surName")
    birthday: Optional[StrictStr] = Field(default=None, description="Customer birthday.")
    email: Optional[StrictStr] = Field(default=None, description="Customer email. Can be null.")
    sex: Optional[NetCustomerIikoNetUserSex] = Field(default=None, description="Customer sex.  <br>0 - not specified,<br />1 - male,<br />2 - female.")
    consent_status: Optional[NetCustomerPersonalDataConsentStatus] = Field(default=None, description="Customer consent status.  <br>0 - unknown,<br />1 - given,<br />2 - revoked.", alias="consentStatus")
    should_receive_loyalty_info: Optional[StrictBool] = Field(default=None, description="Customer get loyalty messages (email, sms). If the parameter is not specified for new customers, the value 'true' is used.", alias="shouldReceiveLoyaltyInfo")
    should_receive_promo_actions_info: Optional[StrictBool] = Field(default=None, description="Customer get promo messages (email, sms). If the parameter is not specified for new customers, the value 'true' is used.", alias="shouldReceivePromoActionsInfo")
    referrer_id: Optional[StrictStr] = Field(default=None, description="Id for referrer guest. Null for old integrations, Guid.Empty - for referrer deletion. Can be null.", alias="referrerId")
    user_data: Optional[StrictStr] = Field(default=None, description="Customer user data. Can be null.", alias="userData")
    is_deleted: Optional[StrictBool] = Field(default=None, description="Customer logical deletion flag.", alias="isDeleted")
    organization_id: StrictStr = Field(description="Customer organization id.", alias="organizationId")
    __properties: ClassVar[List[str]] = ["id", "phone", "cardTrack", "cardNumber", "name", "middleName", "surName", "birthday", "email", "sex", "consentStatus", "shouldReceiveLoyaltyInfo", "shouldReceivePromoActionsInfo", "referrerId", "userData", "isDeleted", "organizationId"]

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
        """Create an instance of NetCustomerCreateOrUpdateCustomerRequest from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if birthday (nullable) is None
        # and model_fields_set contains the field
        if self.birthday is None and "birthday" in self.model_fields_set:
            _dict['birthday'] = None

        # set to None if should_receive_loyalty_info (nullable) is None
        # and model_fields_set contains the field
        if self.should_receive_loyalty_info is None and "should_receive_loyalty_info" in self.model_fields_set:
            _dict['shouldReceiveLoyaltyInfo'] = None

        # set to None if should_receive_promo_actions_info (nullable) is None
        # and model_fields_set contains the field
        if self.should_receive_promo_actions_info is None and "should_receive_promo_actions_info" in self.model_fields_set:
            _dict['shouldReceivePromoActionsInfo'] = None

        # set to None if is_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_deleted is None and "is_deleted" in self.model_fields_set:
            _dict['isDeleted'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetCustomerCreateOrUpdateCustomerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "phone": obj.get("phone"),
            "cardTrack": obj.get("cardTrack"),
            "cardNumber": obj.get("cardNumber"),
            "name": obj.get("name"),
            "middleName": obj.get("middleName"),
            "surName": obj.get("surName"),
            "birthday": obj.get("birthday"),
            "email": obj.get("email"),
            "sex": obj.get("sex"),
            "consentStatus": obj.get("consentStatus"),
            "shouldReceiveLoyaltyInfo": obj.get("shouldReceiveLoyaltyInfo"),
            "shouldReceivePromoActionsInfo": obj.get("shouldReceivePromoActionsInfo"),
            "referrerId": obj.get("referrerId"),
            "userData": obj.get("userData"),
            "isDeleted": obj.get("isDeleted"),
            "organizationId": obj.get("organizationId")
        })
        return _obj


