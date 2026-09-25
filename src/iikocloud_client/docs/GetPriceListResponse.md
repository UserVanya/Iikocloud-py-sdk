# GetPriceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PriceListItem]**](PriceListItem.md) | List of supplier price list items | [optional] 

## Example

```python
from iikocloud_client.models.get_price_list_response import GetPriceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPriceListResponse from a JSON string
get_price_list_response_instance = GetPriceListResponse.from_json(json)
# print the JSON string representation of the object
print(GetPriceListResponse.to_json())

# convert the object into a dict
get_price_list_response_dict = get_price_list_response_instance.to_dict()
# create an instance of GetPriceListResponse from a dict
get_price_list_response_from_dict = GetPriceListResponse.from_dict(get_price_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


