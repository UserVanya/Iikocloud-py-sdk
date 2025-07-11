# TransportAddressCitiesRequest

Organization request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | IDs of organizations that require data return.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**include_deleted** | **bool** | Include deleted cities in response. | [optional] 

## Example

```python
from iikocloud_client.models.transport_address_cities_request import TransportAddressCitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressCitiesRequest from a JSON string
transport_address_cities_request_instance = TransportAddressCitiesRequest.from_json(json)
# print the JSON string representation of the object
print(TransportAddressCitiesRequest.to_json())

# convert the object into a dict
transport_address_cities_request_dict = transport_address_cities_request_instance.to_dict()
# create an instance of TransportAddressCitiesRequest from a dict
transport_address_cities_request_from_dict = TransportAddressCitiesRequest.from_dict(transport_address_cities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


