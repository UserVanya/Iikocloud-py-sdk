# CitiesResponse

Service response with list of cities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cities** | [**List[RmsCityItemsResponse]**](RmsCityItemsResponse.md) | List of cities. | 
**correlation_id** | **UUID** | Operation ID. | 

## Example

```python
from iikocloud_client.models.cities_response import CitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CitiesResponse from a JSON string
cities_response_instance = CitiesResponse.from_json(json)
# print the JSON string representation of the object
print(CitiesResponse.to_json())

# convert the object into a dict
cities_response_dict = cities_response_instance.to_dict()
# create an instance of CitiesResponse from a dict
cities_response_from_dict = CitiesResponse.from_dict(cities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


