# GetProgramsResponse

Get programs response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**programs** | [**List[LoyaltyProgram]**](LoyaltyProgram.md) | Programs. | [optional] 

## Example

```python
from iikocloud_client.models.get_programs_response import GetProgramsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProgramsResponse from a JSON string
get_programs_response_instance = GetProgramsResponse.from_json(json)
# print the JSON string representation of the object
print(GetProgramsResponse.to_json())

# convert the object into a dict
get_programs_response_dict = get_programs_response_instance.to_dict()
# create an instance of GetProgramsResponse from a dict
get_programs_response_from_dict = GetProgramsResponse.from_dict(get_programs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


