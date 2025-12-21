# CancelCausesCancelCause

Delivery cancel cause.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Identifier. | 
**name** | **str** | Name. | 
**is_deleted** | **bool** | Is deleted sign. | [optional] 

## Example

```python
from iikocloud_client.models.cancel_causes_cancel_cause import CancelCausesCancelCause

# TODO update the JSON string below
json = "{}"
# create an instance of CancelCausesCancelCause from a JSON string
cancel_causes_cancel_cause_instance = CancelCausesCancelCause.from_json(json)
# print the JSON string representation of the object
print(CancelCausesCancelCause.to_json())

# convert the object into a dict
cancel_causes_cancel_cause_dict = cancel_causes_cancel_cause_instance.to_dict()
# create an instance of CancelCausesCancelCause from a dict
cancel_causes_cancel_cause_from_dict = CancelCausesCancelCause.from_dict(cancel_causes_cancel_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


