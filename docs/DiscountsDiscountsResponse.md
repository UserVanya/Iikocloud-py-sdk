# DiscountsDiscountsResponse

Response with list of discounts/surcharges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**discounts** | [**List[WrapperDiscountsDiscountCardTypeInfo]**](WrapperDiscountsDiscountCardTypeInfo.md) | List of discounts/surcharges. | 

## Example

```python
from iikocloud_client.models.discounts_discounts_response import DiscountsDiscountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountsDiscountsResponse from a JSON string
discounts_discounts_response_instance = DiscountsDiscountsResponse.from_json(json)
# print the JSON string representation of the object
print(DiscountsDiscountsResponse.to_json())

# convert the object into a dict
discounts_discounts_response_dict = discounts_discounts_response_instance.to_dict()
# create an instance of DiscountsDiscountsResponse from a dict
discounts_discounts_response_from_dict = DiscountsDiscountsResponse.from_dict(discounts_discounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


