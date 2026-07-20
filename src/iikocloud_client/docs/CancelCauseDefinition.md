# CancelCauseDefinition

Delivery cancel cause.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Identifier. | 
**is_deleted** | **bool** | Is deleted sign. | [optional] 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.cancel_cause_definition import CancelCauseDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CancelCauseDefinition from a JSON string
cancel_cause_definition_instance = CancelCauseDefinition.from_json(json)
# print the JSON string representation of the object
print(CancelCauseDefinition.to_json())

# convert the object into a dict
cancel_cause_definition_dict = cancel_cause_definition_instance.to_dict()
# create an instance of CancelCauseDefinition from a dict
cancel_cause_definition_from_dict = CancelCauseDefinition.from_dict(cancel_cause_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


