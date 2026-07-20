# TipsTypesResponse

Response to request for tips types by api-login`s rms group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**tips_types** | [**List[TipsTypeDefinition]**](TipsTypeDefinition.md) | List of tips types for rms group. | 

## Example

```python
from iikocloud_client.models.tips_types_response import TipsTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TipsTypesResponse from a JSON string
tips_types_response_instance = TipsTypesResponse.from_json(json)
# print the JSON string representation of the object
print(TipsTypesResponse.to_json())

# convert the object into a dict
tips_types_response_dict = tips_types_response_instance.to_dict()
# create an instance of TipsTypesResponse from a dict
tips_types_response_from_dict = TipsTypesResponse.from_dict(tips_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


