# RegionsResponse

Service response with list of districts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**regions** | [**List[RmsRegionItemsResponse]**](RmsRegionItemsResponse.md) | List of districts. | 

## Example

```python
from iikocloud_client.models.regions_response import RegionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsResponse from a JSON string
regions_response_instance = RegionsResponse.from_json(json)
# print the JSON string representation of the object
print(RegionsResponse.to_json())

# convert the object into a dict
regions_response_dict = regions_response_instance.to_dict()
# create an instance of RegionsResponse from a dict
regions_response_from_dict = RegionsResponse.from_dict(regions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


