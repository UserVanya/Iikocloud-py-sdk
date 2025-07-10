# TransportEmployeesPersonalShift

Employee personal shift info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee ID. | 
**role_id** | **str** | Employee Role ID. | [optional] 
**opened** | **bool** | Personal shift state flag (true - shift is opened, false - shift is closed). | 
**terminal_group_id** | **str** | ID of the terminal group where the personal shift is opened/closed. | 

## Example

```python
from iiko_cloud_client.models.transport_employees_personal_shift import TransportEmployeesPersonalShift

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesPersonalShift from a JSON string
transport_employees_personal_shift_instance = TransportEmployeesPersonalShift.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesPersonalShift.to_json())

# convert the object into a dict
transport_employees_personal_shift_dict = transport_employees_personal_shift_instance.to_dict()
# create an instance of TransportEmployeesPersonalShift from a dict
transport_employees_personal_shift_from_dict = TransportEmployeesPersonalShift.from_dict(transport_employees_personal_shift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


