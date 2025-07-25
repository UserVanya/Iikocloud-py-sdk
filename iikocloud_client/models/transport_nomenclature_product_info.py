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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from iikocloud_client.models.transport_nomenclature_group_modifier_info import TransportNomenclatureGroupModifierInfo
from iikocloud_client.models.transport_nomenclature_order_item_type import TransportNomenclatureOrderItemType
from iikocloud_client.models.transport_nomenclature_simple_modifier_info import TransportNomenclatureSimpleModifierInfo
from iikocloud_client.models.transport_nomenclature_size_price import TransportNomenclatureSizePrice
from typing import Optional, Set
from typing_extensions import Self

class TransportNomenclatureProductInfo(BaseModel):
    """
    DTO for outside transferring of external menu item details.
    """ # noqa: E501
    fat_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Fat per 100g.", alias="fatAmount")
    proteins_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Protein per 100g.", alias="proteinsAmount")
    carbohydrates_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Carbohydrate per 100g.", alias="carbohydratesAmount")
    energy_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Calories per 100g.", alias="energyAmount")
    fat_full_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Fat per item.", alias="fatFullAmount")
    proteins_full_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Protein per item.", alias="proteinsFullAmount")
    carbohydrates_full_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Carbohydrate per item.", alias="carbohydratesFullAmount")
    energy_full_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Calories per item.", alias="energyFullAmount")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Item weight.")
    group_id: Optional[StrictStr] = Field(default=None, description="Stock list group in RMS.", alias="groupId")
    product_category_id: Optional[StrictStr] = Field(default=None, description="Product category in RMS.", alias="productCategoryId")
    type: Optional[StrictStr] = Field(default=None, description="dish | good | modifier.")
    order_item_type: Optional[TransportNomenclatureOrderItemType] = Field(default=None, description="Product or compound. Depends on modifiers scheme existence.", alias="orderItemType")
    modifier_schema_id: Optional[StrictStr] = Field(default=None, description="Modifier schema's ID.", alias="modifierSchemaId")
    modifier_schema_name: Optional[StrictStr] = Field(default=None, description="Modifier schema's name.", alias="modifierSchemaName")
    splittable: StrictBool = Field(description="Is product splittable.")
    measure_unit: Optional[StrictStr] = Field(default=None, description="Item's unit of measurement.", alias="measureUnit")
    size_prices: Optional[List[TransportNomenclatureSizePrice]] = Field(default=None, description="Prices.", alias="sizePrices")
    modifiers: Optional[List[TransportNomenclatureSimpleModifierInfo]] = Field(default=None, description="Modifiers.")
    group_modifiers: Optional[List[TransportNomenclatureGroupModifierInfo]] = Field(default=None, description="Modifier groups.", alias="groupModifiers")
    image_links: Optional[List[StrictStr]] = Field(default=None, description="Links to images.", alias="imageLinks")
    do_not_print_in_cheque: Optional[StrictBool] = Field(default=None, description="Do not print on bill.", alias="doNotPrintInCheque")
    parent_group: Optional[StrictStr] = Field(default=None, description="External menu group.", alias="parentGroup")
    order: Optional[StrictInt] = Field(default=None, description="Product's order (priority) in menu.")
    full_name_english: Optional[StrictStr] = Field(default=None, description="Full name in a foreign language.", alias="fullNameEnglish")
    use_balance_for_sell: StrictBool = Field(description="Weighed product.", alias="useBalanceForSell")
    can_set_open_price: StrictBool = Field(description="Open price.", alias="canSetOpenPrice")
    payment_subject: Optional[StrictStr] = Field(default=None, description="Payment subject.", alias="paymentSubject")
    id: StrictStr = Field(description="ID.")
    code: Optional[StrictStr] = Field(default=None, description="SKU.")
    name: StrictStr = Field(description="Name.")
    description: Optional[StrictStr] = Field(default=None, description="Description.")
    additional_info: Optional[StrictStr] = Field(default=None, description="Additional information.", alias="additionalInfo")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Tags.")
    is_deleted: Optional[StrictBool] = Field(default=None, description="Is-Deleted attribute.", alias="isDeleted")
    seo_description: Optional[StrictStr] = Field(default=None, description="SEO description for client.", alias="seoDescription")
    seo_text: Optional[StrictStr] = Field(default=None, description="SEO text for robots.", alias="seoText")
    seo_keywords: Optional[StrictStr] = Field(default=None, description="SEO key words.", alias="seoKeywords")
    seo_title: Optional[StrictStr] = Field(default=None, description="SEO header.", alias="seoTitle")
    __properties: ClassVar[List[str]] = ["fatAmount", "proteinsAmount", "carbohydratesAmount", "energyAmount", "fatFullAmount", "proteinsFullAmount", "carbohydratesFullAmount", "energyFullAmount", "weight", "groupId", "productCategoryId", "type", "orderItemType", "modifierSchemaId", "modifierSchemaName", "splittable", "measureUnit", "sizePrices", "modifiers", "groupModifiers", "imageLinks", "doNotPrintInCheque", "parentGroup", "order", "fullNameEnglish", "useBalanceForSell", "canSetOpenPrice", "paymentSubject", "id", "code", "name", "description", "additionalInfo", "tags", "isDeleted", "seoDescription", "seoText", "seoKeywords", "seoTitle"]

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
        """Create an instance of TransportNomenclatureProductInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in size_prices (list)
        _items = []
        if self.size_prices:
            for _item_size_prices in self.size_prices:
                if _item_size_prices:
                    _items.append(_item_size_prices.to_dict())
            _dict['sizePrices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in modifiers (list)
        _items = []
        if self.modifiers:
            for _item_modifiers in self.modifiers:
                if _item_modifiers:
                    _items.append(_item_modifiers.to_dict())
            _dict['modifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in group_modifiers (list)
        _items = []
        if self.group_modifiers:
            for _item_group_modifiers in self.group_modifiers:
                if _item_group_modifiers:
                    _items.append(_item_group_modifiers.to_dict())
            _dict['groupModifiers'] = _items
        # set to None if fat_amount (nullable) is None
        # and model_fields_set contains the field
        if self.fat_amount is None and "fat_amount" in self.model_fields_set:
            _dict['fatAmount'] = None

        # set to None if proteins_amount (nullable) is None
        # and model_fields_set contains the field
        if self.proteins_amount is None and "proteins_amount" in self.model_fields_set:
            _dict['proteinsAmount'] = None

        # set to None if carbohydrates_amount (nullable) is None
        # and model_fields_set contains the field
        if self.carbohydrates_amount is None and "carbohydrates_amount" in self.model_fields_set:
            _dict['carbohydratesAmount'] = None

        # set to None if energy_amount (nullable) is None
        # and model_fields_set contains the field
        if self.energy_amount is None and "energy_amount" in self.model_fields_set:
            _dict['energyAmount'] = None

        # set to None if fat_full_amount (nullable) is None
        # and model_fields_set contains the field
        if self.fat_full_amount is None and "fat_full_amount" in self.model_fields_set:
            _dict['fatFullAmount'] = None

        # set to None if proteins_full_amount (nullable) is None
        # and model_fields_set contains the field
        if self.proteins_full_amount is None and "proteins_full_amount" in self.model_fields_set:
            _dict['proteinsFullAmount'] = None

        # set to None if carbohydrates_full_amount (nullable) is None
        # and model_fields_set contains the field
        if self.carbohydrates_full_amount is None and "carbohydrates_full_amount" in self.model_fields_set:
            _dict['carbohydratesFullAmount'] = None

        # set to None if energy_full_amount (nullable) is None
        # and model_fields_set contains the field
        if self.energy_full_amount is None and "energy_full_amount" in self.model_fields_set:
            _dict['energyFullAmount'] = None

        # set to None if weight (nullable) is None
        # and model_fields_set contains the field
        if self.weight is None and "weight" in self.model_fields_set:
            _dict['weight'] = None

        # set to None if group_id (nullable) is None
        # and model_fields_set contains the field
        if self.group_id is None and "group_id" in self.model_fields_set:
            _dict['groupId'] = None

        # set to None if product_category_id (nullable) is None
        # and model_fields_set contains the field
        if self.product_category_id is None and "product_category_id" in self.model_fields_set:
            _dict['productCategoryId'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if modifier_schema_id (nullable) is None
        # and model_fields_set contains the field
        if self.modifier_schema_id is None and "modifier_schema_id" in self.model_fields_set:
            _dict['modifierSchemaId'] = None

        # set to None if modifier_schema_name (nullable) is None
        # and model_fields_set contains the field
        if self.modifier_schema_name is None and "modifier_schema_name" in self.model_fields_set:
            _dict['modifierSchemaName'] = None

        # set to None if parent_group (nullable) is None
        # and model_fields_set contains the field
        if self.parent_group is None and "parent_group" in self.model_fields_set:
            _dict['parentGroup'] = None

        # set to None if full_name_english (nullable) is None
        # and model_fields_set contains the field
        if self.full_name_english is None and "full_name_english" in self.model_fields_set:
            _dict['fullNameEnglish'] = None

        # set to None if payment_subject (nullable) is None
        # and model_fields_set contains the field
        if self.payment_subject is None and "payment_subject" in self.model_fields_set:
            _dict['paymentSubject'] = None

        # set to None if code (nullable) is None
        # and model_fields_set contains the field
        if self.code is None and "code" in self.model_fields_set:
            _dict['code'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if additional_info (nullable) is None
        # and model_fields_set contains the field
        if self.additional_info is None and "additional_info" in self.model_fields_set:
            _dict['additionalInfo'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if seo_description (nullable) is None
        # and model_fields_set contains the field
        if self.seo_description is None and "seo_description" in self.model_fields_set:
            _dict['seoDescription'] = None

        # set to None if seo_text (nullable) is None
        # and model_fields_set contains the field
        if self.seo_text is None and "seo_text" in self.model_fields_set:
            _dict['seoText'] = None

        # set to None if seo_keywords (nullable) is None
        # and model_fields_set contains the field
        if self.seo_keywords is None and "seo_keywords" in self.model_fields_set:
            _dict['seoKeywords'] = None

        # set to None if seo_title (nullable) is None
        # and model_fields_set contains the field
        if self.seo_title is None and "seo_title" in self.model_fields_set:
            _dict['seoTitle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransportNomenclatureProductInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fatAmount": obj.get("fatAmount"),
            "proteinsAmount": obj.get("proteinsAmount"),
            "carbohydratesAmount": obj.get("carbohydratesAmount"),
            "energyAmount": obj.get("energyAmount"),
            "fatFullAmount": obj.get("fatFullAmount"),
            "proteinsFullAmount": obj.get("proteinsFullAmount"),
            "carbohydratesFullAmount": obj.get("carbohydratesFullAmount"),
            "energyFullAmount": obj.get("energyFullAmount"),
            "weight": obj.get("weight"),
            "groupId": obj.get("groupId"),
            "productCategoryId": obj.get("productCategoryId"),
            "type": obj.get("type"),
            "orderItemType": obj.get("orderItemType"),
            "modifierSchemaId": obj.get("modifierSchemaId"),
            "modifierSchemaName": obj.get("modifierSchemaName"),
            "splittable": obj.get("splittable"),
            "measureUnit": obj.get("measureUnit"),
            "sizePrices": [TransportNomenclatureSizePrice.from_dict(_item) for _item in obj["sizePrices"]] if obj.get("sizePrices") is not None else None,
            "modifiers": [TransportNomenclatureSimpleModifierInfo.from_dict(_item) for _item in obj["modifiers"]] if obj.get("modifiers") is not None else None,
            "groupModifiers": [TransportNomenclatureGroupModifierInfo.from_dict(_item) for _item in obj["groupModifiers"]] if obj.get("groupModifiers") is not None else None,
            "imageLinks": obj.get("imageLinks"),
            "doNotPrintInCheque": obj.get("doNotPrintInCheque"),
            "parentGroup": obj.get("parentGroup"),
            "order": obj.get("order"),
            "fullNameEnglish": obj.get("fullNameEnglish"),
            "useBalanceForSell": obj.get("useBalanceForSell"),
            "canSetOpenPrice": obj.get("canSetOpenPrice"),
            "paymentSubject": obj.get("paymentSubject"),
            "id": obj.get("id"),
            "code": obj.get("code"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "additionalInfo": obj.get("additionalInfo"),
            "tags": obj.get("tags"),
            "isDeleted": obj.get("isDeleted"),
            "seoDescription": obj.get("seoDescription"),
            "seoText": obj.get("seoText"),
            "seoKeywords": obj.get("seoKeywords"),
            "seoTitle": obj.get("seoTitle")
        })
        return _obj


