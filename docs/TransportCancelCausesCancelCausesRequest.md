# TransportCancelCausesCancelCausesRequest

Request for organization's delivery cancel causes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations ids which delivery cancel causes needs to be returned.                 Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_cancel_causes_cancel_causes_request import TransportCancelCausesCancelCausesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCancelCausesCancelCausesRequest from a JSON string
transport_cancel_causes_cancel_causes_request_instance = TransportCancelCausesCancelCausesRequest.from_json(json)
# print the JSON string representation of the object
print(TransportCancelCausesCancelCausesRequest.to_json())

# convert the object into a dict
transport_cancel_causes_cancel_causes_request_dict = transport_cancel_causes_cancel_causes_request_instance.to_dict()
# create an instance of TransportCancelCausesCancelCausesRequest from a dict
transport_cancel_causes_cancel_causes_request_from_dict = TransportCancelCausesCancelCausesRequest.from_dict(transport_cancel_causes_cancel_causes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


