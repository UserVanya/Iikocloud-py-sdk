# WrapperDiscountsDiscountCardTypeInfo

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[DiscountsDiscountCardTypeInfo]**](DiscountsDiscountCardTypeInfo.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.wrapper_discounts_discount_card_type_info import WrapperDiscountsDiscountCardTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperDiscountsDiscountCardTypeInfo from a JSON string
wrapper_discounts_discount_card_type_info_instance = WrapperDiscountsDiscountCardTypeInfo.from_json(json)
# print the JSON string representation of the object
print(WrapperDiscountsDiscountCardTypeInfo.to_json())

# convert the object into a dict
wrapper_discounts_discount_card_type_info_dict = wrapper_discounts_discount_card_type_info_instance.to_dict()
# create an instance of WrapperDiscountsDiscountCardTypeInfo from a dict
wrapper_discounts_discount_card_type_info_from_dict = WrapperDiscountsDiscountCardTypeInfo.from_dict(wrapper_discounts_discount_card_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


