# AddressRegionsRequest

Organization request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | IDs of organizations that require data return.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.address_regions_request import AddressRegionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRegionsRequest from a JSON string
address_regions_request_instance = AddressRegionsRequest.from_json(json)
# print the JSON string representation of the object
print(AddressRegionsRequest.to_json())

# convert the object into a dict
address_regions_request_dict = address_regions_request_instance.to_dict()
# create an instance of AddressRegionsRequest from a dict
address_regions_request_from_dict = AddressRegionsRequest.from_dict(address_regions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


