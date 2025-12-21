# CancelCausesCancelCausesResponse

Response with delivery cancel causes (reasons for deletion) list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**cancel_causes** | [**List[CancelCausesCancelCause]**](CancelCausesCancelCause.md) | List of delivery cancel causes. | 

## Example

```python
from iikocloud_client.models.cancel_causes_cancel_causes_response import CancelCausesCancelCausesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelCausesCancelCausesResponse from a JSON string
cancel_causes_cancel_causes_response_instance = CancelCausesCancelCausesResponse.from_json(json)
# print the JSON string representation of the object
print(CancelCausesCancelCausesResponse.to_json())

# convert the object into a dict
cancel_causes_cancel_causes_response_dict = cancel_causes_cancel_causes_response_instance.to_dict()
# create an instance of CancelCausesCancelCausesResponse from a dict
cancel_causes_cancel_causes_response_from_dict = CancelCausesCancelCausesResponse.from_dict(cancel_causes_cancel_causes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


