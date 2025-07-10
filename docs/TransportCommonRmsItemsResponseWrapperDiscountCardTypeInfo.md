# TransportCommonRmsItemsResponseWrapperDiscountCardTypeInfo

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[TransportDiscountsDiscountCardTypeInfo]**](TransportDiscountsDiscountCardTypeInfo.md) | Items for organization. | 

## Example

```python
from iiko_cloud_client.models.transport_common_rms_items_response_wrapper_discount_card_type_info import TransportCommonRmsItemsResponseWrapperDiscountCardTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommonRmsItemsResponseWrapperDiscountCardTypeInfo from a JSON string
transport_common_rms_items_response_wrapper_discount_card_type_info_instance = TransportCommonRmsItemsResponseWrapperDiscountCardTypeInfo.from_json(json)
# print the JSON string representation of the object
print(TransportCommonRmsItemsResponseWrapperDiscountCardTypeInfo.to_json())

# convert the object into a dict
transport_common_rms_items_response_wrapper_discount_card_type_info_dict = transport_common_rms_items_response_wrapper_discount_card_type_info_instance.to_dict()
# create an instance of TransportCommonRmsItemsResponseWrapperDiscountCardTypeInfo from a dict
transport_common_rms_items_response_wrapper_discount_card_type_info_from_dict = TransportCommonRmsItemsResponseWrapperDiscountCardTypeInfo.from_dict(transport_common_rms_items_response_wrapper_discount_card_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


