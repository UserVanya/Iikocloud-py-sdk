# TransportTipsTypesTipsTypesResponse

Response to request for tips types by api-login`s rms group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**tips_types** | [**List[TransportTipsTypesTipsType]**](TransportTipsTypesTipsType.md) | List of tips types for rms group. | 

## Example

```python
from iiko_cloud_client.models.transport_tips_types_tips_types_response import TransportTipsTypesTipsTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTipsTypesTipsTypesResponse from a JSON string
transport_tips_types_tips_types_response_instance = TransportTipsTypesTipsTypesResponse.from_json(json)
# print the JSON string representation of the object
print(TransportTipsTypesTipsTypesResponse.to_json())

# convert the object into a dict
transport_tips_types_tips_types_response_dict = transport_tips_types_tips_types_response_instance.to_dict()
# create an instance of TransportTipsTypesTipsTypesResponse from a dict
transport_tips_types_tips_types_response_from_dict = TransportTipsTypesTipsTypesResponse.from_dict(transport_tips_types_tips_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


