# StreetsByCityRequest

Organization and city request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city_id** | **UUID** | City ID. | 
**include_deleted** | **bool** | Include deleted streets in response. | [optional] 
**organization_id** | **UUID** | Organization ID details of which have to be returned.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.streets_by_city_request import StreetsByCityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreetsByCityRequest from a JSON string
streets_by_city_request_instance = StreetsByCityRequest.from_json(json)
# print the JSON string representation of the object
print(StreetsByCityRequest.to_json())

# convert the object into a dict
streets_by_city_request_dict = streets_by_city_request_instance.to_dict()
# create an instance of StreetsByCityRequest from a dict
streets_by_city_request_from_dict = StreetsByCityRequest.from_dict(streets_by_city_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


