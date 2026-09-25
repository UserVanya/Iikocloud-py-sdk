# AttendanceTypeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Attendance type code | [optional] 
**comment** | **str** | Description | [optional] 
**id** | **UUID** | Attendance type UUID | [optional] 
**is_deleted** | **bool** | Attendance type deleted flag | [optional] 
**is_presence** | **bool** | Presence flag: the value &#x60;true&#x60; means the employee is present, the value &#x60;false&#x60; means the employee is absent | [optional] 
**name** | **str** | Localized name | [optional] 
**pay_rate** | **float** | Payment coefficient | [optional] 

## Example

```python
from iikocloud_client.models.attendance_type_item import AttendanceTypeItem

# TODO update the JSON string below
json = "{}"
# create an instance of AttendanceTypeItem from a JSON string
attendance_type_item_instance = AttendanceTypeItem.from_json(json)
# print the JSON string representation of the object
print(AttendanceTypeItem.to_json())

# convert the object into a dict
attendance_type_item_dict = attendance_type_item_instance.to_dict()
# create an instance of AttendanceTypeItem from a dict
attendance_type_item_from_dict = AttendanceTypeItem.from_dict(attendance_type_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


