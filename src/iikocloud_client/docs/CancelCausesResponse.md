# CancelCausesResponse

Response with delivery cancel causes (reasons for deletion) list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_causes** | [**List[CancelCauseDefinition]**](CancelCauseDefinition.md) | List of delivery cancel causes. | 
**correlation_id** | **UUID** | Operation ID. | 

## Example

```python
from iikocloud_client.models.cancel_causes_response import CancelCausesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelCausesResponse from a JSON string
cancel_causes_response_instance = CancelCausesResponse.from_json(json)
# print the JSON string representation of the object
print(CancelCausesResponse.to_json())

# convert the object into a dict
cancel_causes_response_dict = cancel_causes_response_instance.to_dict()
# create an instance of CancelCausesResponse from a dict
cancel_causes_response_from_dict = CancelCausesResponse.from_dict(cancel_causes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


