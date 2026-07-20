# DiscountsResponse

Response with list of discounts/surcharges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**discounts** | [**List[RmsDiscountCardTypeItemsResponse]**](RmsDiscountCardTypeItemsResponse.md) | List of discounts/surcharges. | 

## Example

```python
from iikocloud_client.models.discounts_response import DiscountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountsResponse from a JSON string
discounts_response_instance = DiscountsResponse.from_json(json)
# print the JSON string representation of the object
print(DiscountsResponse.to_json())

# convert the object into a dict
discounts_response_dict = discounts_response_instance.to_dict()
# create an instance of DiscountsResponse from a dict
discounts_response_from_dict = DiscountsResponse.from_dict(discounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


