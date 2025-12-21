# RmsItemsResponseWrapperDiscountsDiscountCardTypeInfo

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[IikoTransportPublicApiContractsDiscountsDiscountCardTypeInfo]**](IikoTransportPublicApiContractsDiscountsDiscountCardTypeInfo.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.rms_items_response_wrapper_discounts_discount_card_type_info import RmsItemsResponseWrapperDiscountsDiscountCardTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RmsItemsResponseWrapperDiscountsDiscountCardTypeInfo from a JSON string
rms_items_response_wrapper_discounts_discount_card_type_info_instance = RmsItemsResponseWrapperDiscountsDiscountCardTypeInfo.from_json(json)
# print the JSON string representation of the object
print(RmsItemsResponseWrapperDiscountsDiscountCardTypeInfo.to_json())

# convert the object into a dict
rms_items_response_wrapper_discounts_discount_card_type_info_dict = rms_items_response_wrapper_discounts_discount_card_type_info_instance.to_dict()
# create an instance of RmsItemsResponseWrapperDiscountsDiscountCardTypeInfo from a dict
rms_items_response_wrapper_discounts_discount_card_type_info_from_dict = RmsItemsResponseWrapperDiscountsDiscountCardTypeInfo.from_dict(rms_items_response_wrapper_discounts_discount_card_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


