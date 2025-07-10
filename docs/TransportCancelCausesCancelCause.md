# TransportCancelCausesCancelCause

Delivery cancel cause.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier. | 
**name** | **str** | Name. | 
**is_deleted** | **bool** | Is deleted sign. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_cancel_causes_cancel_cause import TransportCancelCausesCancelCause

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCancelCausesCancelCause from a JSON string
transport_cancel_causes_cancel_cause_instance = TransportCancelCausesCancelCause.from_json(json)
# print the JSON string representation of the object
print(TransportCancelCausesCancelCause.to_json())

# convert the object into a dict
transport_cancel_causes_cancel_cause_dict = transport_cancel_causes_cancel_cause_instance.to_dict()
# create an instance of TransportCancelCausesCancelCause from a dict
transport_cancel_causes_cancel_cause_from_dict = TransportCancelCausesCancelCause.from_dict(transport_cancel_causes_cancel_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


