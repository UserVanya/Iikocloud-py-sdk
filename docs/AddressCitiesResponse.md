# AddressCitiesResponse

Service response with list of cities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**cities** | [**List[WrapperAddressCity]**](WrapperAddressCity.md) | List of cities. | 

## Example

```python
from iikocloud_client.models.address_cities_response import AddressCitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressCitiesResponse from a JSON string
address_cities_response_instance = AddressCitiesResponse.from_json(json)
# print the JSON string representation of the object
print(AddressCitiesResponse.to_json())

# convert the object into a dict
address_cities_response_dict = address_cities_response_instance.to_dict()
# create an instance of AddressCitiesResponse from a dict
address_cities_response_from_dict = AddressCitiesResponse.from_dict(address_cities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


