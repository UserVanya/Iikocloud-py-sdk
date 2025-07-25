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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from iikocloud_client.models.transport_deliveries_common_payment_additional_data import TransportDeliveriesCommonPaymentAdditionalData
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from iikocloud_client.models.transport_deliveries_request_create_order_card_payment import TransportDeliveriesRequestCreateOrderCardPayment
    from iikocloud_client.models.transport_deliveries_request_create_order_cash_payment import TransportDeliveriesRequestCreateOrderCashPayment
    from iikocloud_client.models.transport_deliveries_request_create_order_external_payment import TransportDeliveriesRequestCreateOrderExternalPayment
    from iikocloud_client.models.transport_deliveries_request_create_order_loyalty_card_payment import TransportDeliveriesRequestCreateOrderLoyaltyCardPayment

class TransportDeliveriesRequestCreateOrderPayment(BaseModel):
    """
    Base class of delivery order payment item.
    """ # noqa: E501
    payment_type_kind: StrictStr = Field(alias="paymentTypeKind")
    sum: Union[Annotated[float, Field(le=10000000000, strict=True, ge=0)], Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(description="Amount due.")
    payment_type_id: StrictStr = Field(description="Payment type.                 Can be obtained by `/api/1/payment_types` operation.", alias="paymentTypeId")
    is_processed_externally: Optional[StrictBool] = Field(default=None, description="Whether payment item is processed by external payment system (made from outside).", alias="isProcessedExternally")
    payment_additional_data: Optional[TransportDeliveriesCommonPaymentAdditionalData] = Field(default=None, description="Additional payment parameters.", alias="paymentAdditionalData")
    is_fiscalized_externally: Optional[StrictBool] = Field(default=None, description="Whether the payment item is externally fiscalized.   > Allowed from version `7.6.3`.", alias="isFiscalizedExternally")
    is_prepay: Optional[StrictBool] = Field(default=None, description="Whether the payment item is prepay. Unavailable for `paymentKindType.LoyaltyCard`.   > Allowed from version `8.2.6`.", alias="isPrepay")
    __properties: ClassVar[List[str]] = ["paymentTypeKind", "sum", "paymentTypeId", "isProcessedExternally", "paymentAdditionalData", "isFiscalizedExternally", "isPrepay"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'paymentTypeKind'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'Card': 'TransportDeliveriesRequestCreateOrderCardPayment','Cash': 'TransportDeliveriesRequestCreateOrderCashPayment','External': 'TransportDeliveriesRequestCreateOrderExternalPayment','LoyaltyCard': 'TransportDeliveriesRequestCreateOrderLoyaltyCardPayment'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[TransportDeliveriesRequestCreateOrderCardPayment, TransportDeliveriesRequestCreateOrderCashPayment, TransportDeliveriesRequestCreateOrderExternalPayment, TransportDeliveriesRequestCreateOrderLoyaltyCardPayment]]:
        """Create an instance of TransportDeliveriesRequestCreateOrderPayment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payment_additional_data
        if self.payment_additional_data:
            _dict['paymentAdditionalData'] = self.payment_additional_data.to_dict()
        # set to None if payment_additional_data (nullable) is None
        # and model_fields_set contains the field
        if self.payment_additional_data is None and "payment_additional_data" in self.model_fields_set:
            _dict['paymentAdditionalData'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[TransportDeliveriesRequestCreateOrderCardPayment, TransportDeliveriesRequestCreateOrderCashPayment, TransportDeliveriesRequestCreateOrderExternalPayment, TransportDeliveriesRequestCreateOrderLoyaltyCardPayment]]:
        """Create an instance of TransportDeliveriesRequestCreateOrderPayment from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'TransportDeliveriesRequestCreateOrderCardPayment':
            return import_module("iikocloud_client.models.transport_deliveries_request_create_order_card_payment").TransportDeliveriesRequestCreateOrderCardPayment.from_dict(obj)
        if object_type ==  'TransportDeliveriesRequestCreateOrderCashPayment':
            return import_module("iikocloud_client.models.transport_deliveries_request_create_order_cash_payment").TransportDeliveriesRequestCreateOrderCashPayment.from_dict(obj)
        if object_type ==  'TransportDeliveriesRequestCreateOrderExternalPayment':
            return import_module("iikocloud_client.models.transport_deliveries_request_create_order_external_payment").TransportDeliveriesRequestCreateOrderExternalPayment.from_dict(obj)
        if object_type ==  'TransportDeliveriesRequestCreateOrderLoyaltyCardPayment':
            return import_module("iikocloud_client.models.transport_deliveries_request_create_order_loyalty_card_payment").TransportDeliveriesRequestCreateOrderLoyaltyCardPayment.from_dict(obj)

        raise ValueError("TransportDeliveriesRequestCreateOrderPayment failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


