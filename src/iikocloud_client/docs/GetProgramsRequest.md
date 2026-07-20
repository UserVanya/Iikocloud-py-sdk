# GetProgramsRequest

Get programs request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | 
**without_marketing_campaigns** | **bool** | Determines if marketing campaigns not required. | [optional] 

## Example

```python
from iikocloud_client.models.get_programs_request import GetProgramsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetProgramsRequest from a JSON string
get_programs_request_instance = GetProgramsRequest.from_json(json)
# print the JSON string representation of the object
print(GetProgramsRequest.to_json())

# convert the object into a dict
get_programs_request_dict = get_programs_request_instance.to_dict()
# create an instance of GetProgramsRequest from a dict
get_programs_request_from_dict = GetProgramsRequest.from_dict(get_programs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


