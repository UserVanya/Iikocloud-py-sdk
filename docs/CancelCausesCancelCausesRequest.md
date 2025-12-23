# CancelCausesCancelCausesRequest

Request for organization's delivery cancel causes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations ids which delivery cancel causes needs to be returned.                 Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.cancel_causes_cancel_causes_request import CancelCausesCancelCausesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelCausesCancelCausesRequest from a JSON string
cancel_causes_cancel_causes_request_instance = CancelCausesCancelCausesRequest.from_json(json)
# print the JSON string representation of the object
print(CancelCausesCancelCausesRequest.to_json())

# convert the object into a dict
cancel_causes_cancel_causes_request_dict = cancel_causes_cancel_causes_request_instance.to_dict()
# create an instance of CancelCausesCancelCausesRequest from a dict
cancel_causes_cancel_causes_request_from_dict = CancelCausesCancelCausesRequest.from_dict(cancel_causes_cancel_causes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


