# GetPriceListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counteragent_id** | **str** | Supplier identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.get_price_list_request import GetPriceListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPriceListRequest from a JSON string
get_price_list_request_instance = GetPriceListRequest.from_json(json)
# print the JSON string representation of the object
print(GetPriceListRequest.to_json())

# convert the object into a dict
get_price_list_request_dict = get_price_list_request_instance.to_dict()
# create an instance of GetPriceListRequest from a dict
get_price_list_request_from_dict = GetPriceListRequest.from_dict(get_price_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


