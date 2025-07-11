# TransportDiscountsDiscountsResponse

Response with list of discounts/surcharges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**discounts** | [**List[TransportCommonRmsItemsResponseWrapperDiscountCardTypeInfo]**](TransportCommonRmsItemsResponseWrapperDiscountCardTypeInfo.md) | List of discounts/surcharges. | 

## Example

```python
from iikocloud_client.models.transport_discounts_discounts_response import TransportDiscountsDiscountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDiscountsDiscountsResponse from a JSON string
transport_discounts_discounts_response_instance = TransportDiscountsDiscountsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDiscountsDiscountsResponse.to_json())

# convert the object into a dict
transport_discounts_discounts_response_dict = transport_discounts_discounts_response_instance.to_dict()
# create an instance of TransportDiscountsDiscountsResponse from a dict
transport_discounts_discounts_response_from_dict = TransportDiscountsDiscountsResponse.from_dict(transport_discounts_discounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


