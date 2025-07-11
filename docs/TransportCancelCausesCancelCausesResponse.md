# TransportCancelCausesCancelCausesResponse

Response with delivery cancel causes (reasons for deletion) list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**cancel_causes** | [**List[TransportCancelCausesCancelCause]**](TransportCancelCausesCancelCause.md) | List of delivery cancel causes. | 

## Example

```python
from iikocloud_client.models.transport_cancel_causes_cancel_causes_response import TransportCancelCausesCancelCausesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCancelCausesCancelCausesResponse from a JSON string
transport_cancel_causes_cancel_causes_response_instance = TransportCancelCausesCancelCausesResponse.from_json(json)
# print the JSON string representation of the object
print(TransportCancelCausesCancelCausesResponse.to_json())

# convert the object into a dict
transport_cancel_causes_cancel_causes_response_dict = transport_cancel_causes_cancel_causes_response_instance.to_dict()
# create an instance of TransportCancelCausesCancelCausesResponse from a dict
transport_cancel_causes_cancel_causes_response_from_dict = TransportCancelCausesCancelCausesResponse.from_dict(transport_cancel_causes_cancel_causes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


