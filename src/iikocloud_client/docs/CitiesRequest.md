# CitiesRequest

Organization request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_deleted** | **bool** | Include deleted cities in response. | [optional] 
**organization_ids** | **List[UUID]** | IDs of organizations that require data return.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.cities_request import CitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CitiesRequest from a JSON string
cities_request_instance = CitiesRequest.from_json(json)
# print the JSON string representation of the object
print(CitiesRequest.to_json())

# convert the object into a dict
cities_request_dict = cities_request_instance.to_dict()
# create an instance of CitiesRequest from a dict
cities_request_from_dict = CitiesRequest.from_dict(cities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


