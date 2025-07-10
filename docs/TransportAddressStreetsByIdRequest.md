# TransportAddressStreetsByIdRequest

Organization and city request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization Id. | 
**ids** | **List[str]** | Street Ids. | [optional] 
**classifier_ids** | **List[str]** | Street classifierIds. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_address_streets_by_id_request import TransportAddressStreetsByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressStreetsByIdRequest from a JSON string
transport_address_streets_by_id_request_instance = TransportAddressStreetsByIdRequest.from_json(json)
# print the JSON string representation of the object
print(TransportAddressStreetsByIdRequest.to_json())

# convert the object into a dict
transport_address_streets_by_id_request_dict = transport_address_streets_by_id_request_instance.to_dict()
# create an instance of TransportAddressStreetsByIdRequest from a dict
transport_address_streets_by_id_request_from_dict = TransportAddressStreetsByIdRequest.from_dict(transport_address_streets_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


