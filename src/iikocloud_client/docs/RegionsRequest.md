# RegionsRequest

Organization request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | IDs of organizations that require data return.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.regions_request import RegionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsRequest from a JSON string
regions_request_instance = RegionsRequest.from_json(json)
# print the JSON string representation of the object
print(RegionsRequest.to_json())

# convert the object into a dict
regions_request_dict = regions_request_instance.to_dict()
# create an instance of RegionsRequest from a dict
regions_request_from_dict = RegionsRequest.from_dict(regions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


