# TransportAddressStreetsByCityRequest

Organization and city request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID details of which have to be returned.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**city_id** | **str** | City ID. | 
**include_deleted** | **bool** | Include deleted streets in response. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_address_streets_by_city_request import TransportAddressStreetsByCityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressStreetsByCityRequest from a JSON string
transport_address_streets_by_city_request_instance = TransportAddressStreetsByCityRequest.from_json(json)
# print the JSON string representation of the object
print(TransportAddressStreetsByCityRequest.to_json())

# convert the object into a dict
transport_address_streets_by_city_request_dict = transport_address_streets_by_city_request_instance.to_dict()
# create an instance of TransportAddressStreetsByCityRequest from a dict
transport_address_streets_by_city_request_from_dict = TransportAddressStreetsByCityRequest.from_dict(transport_address_streets_by_city_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


