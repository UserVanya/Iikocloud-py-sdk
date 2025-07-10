# TransportRemovalTypesRemovalTypesResponse

Response with removal types (reasons for deletion) list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**removal_types** | [**List[TransportRemovalTypesRemovalType]**](TransportRemovalTypesRemovalType.md) | List of removal types. | 

## Example

```python
from iiko_cloud_client.models.transport_removal_types_removal_types_response import TransportRemovalTypesRemovalTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportRemovalTypesRemovalTypesResponse from a JSON string
transport_removal_types_removal_types_response_instance = TransportRemovalTypesRemovalTypesResponse.from_json(json)
# print the JSON string representation of the object
print(TransportRemovalTypesRemovalTypesResponse.to_json())

# convert the object into a dict
transport_removal_types_removal_types_response_dict = transport_removal_types_removal_types_response_instance.to_dict()
# create an instance of TransportRemovalTypesRemovalTypesResponse from a dict
transport_removal_types_removal_types_response_from_dict = TransportRemovalTypesRemovalTypesResponse.from_dict(transport_removal_types_removal_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


