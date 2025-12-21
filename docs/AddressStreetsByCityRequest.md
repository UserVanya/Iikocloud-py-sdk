# AddressStreetsByCityRequest

Organization and city request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID details of which have to be returned.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**city_id** | **UUID** | City ID. | 
**include_deleted** | **bool** | Include deleted streets in response. | [optional] 

## Example

```python
from iikocloud_client.models.address_streets_by_city_request import AddressStreetsByCityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressStreetsByCityRequest from a JSON string
address_streets_by_city_request_instance = AddressStreetsByCityRequest.from_json(json)
# print the JSON string representation of the object
print(AddressStreetsByCityRequest.to_json())

# convert the object into a dict
address_streets_by_city_request_dict = address_streets_by_city_request_instance.to_dict()
# create an instance of AddressStreetsByCityRequest from a dict
address_streets_by_city_request_from_dict = AddressStreetsByCityRequest.from_dict(address_streets_by_city_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


