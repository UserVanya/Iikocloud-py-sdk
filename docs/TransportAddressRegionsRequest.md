# TransportAddressRegionsRequest

Organization request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | IDs of organizations that require data return.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iiko_cloud_client.models.transport_address_regions_request import TransportAddressRegionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportAddressRegionsRequest from a JSON string
transport_address_regions_request_instance = TransportAddressRegionsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportAddressRegionsRequest.to_json())

# convert the object into a dict
transport_address_regions_request_dict = transport_address_regions_request_instance.to_dict()
# create an instance of TransportAddressRegionsRequest from a dict
transport_address_regions_request_from_dict = TransportAddressRegionsRequest.from_dict(transport_address_regions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


