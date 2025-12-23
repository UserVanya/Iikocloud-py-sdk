# TipsTypesTipsTypesResponse

Response to request for tips types by api-login`s rms group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**tips_types** | [**List[TipsTypesTipsType]**](TipsTypesTipsType.md) | List of tips types for rms group. | 

## Example

```python
from iikocloud_client.models.tips_types_tips_types_response import TipsTypesTipsTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TipsTypesTipsTypesResponse from a JSON string
tips_types_tips_types_response_instance = TipsTypesTipsTypesResponse.from_json(json)
# print the JSON string representation of the object
print(TipsTypesTipsTypesResponse.to_json())

# convert the object into a dict
tips_types_tips_types_response_dict = tips_types_tips_types_response_instance.to_dict()
# create an instance of TipsTypesTipsTypesResponse from a dict
tips_types_tips_types_response_from_dict = TipsTypesTipsTypesResponse.from_dict(tips_types_tips_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


