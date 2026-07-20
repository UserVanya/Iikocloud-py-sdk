# PersonalShift

Employee personal shift info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Employee ID. | 
**opened** | **bool** | Personal shift state flag (true - shift is opened, false - shift is closed). | 
**role_id** | **UUID** | Employee Role ID. | [optional] 
**terminal_group_id** | **UUID** | ID of the terminal group where the personal shift is opened/closed. | 

## Example

```python
from iikocloud_client.models.personal_shift import PersonalShift

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalShift from a JSON string
personal_shift_instance = PersonalShift.from_json(json)
# print the JSON string representation of the object
print(PersonalShift.to_json())

# convert the object into a dict
personal_shift_dict = personal_shift_instance.to_dict()
# create an instance of PersonalShift from a dict
personal_shift_from_dict = PersonalShift.from_dict(personal_shift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


