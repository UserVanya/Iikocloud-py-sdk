# PeriodScheduleDto2

Schedule availability interval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** | Start time | 
**end** | **str** | End time | 
**days_of_week** | **List[str]** | Availability days of week | 

## Example

```python
from iikocloud_client.models.period_schedule_dto2 import PeriodScheduleDto2

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodScheduleDto2 from a JSON string
period_schedule_dto2_instance = PeriodScheduleDto2.from_json(json)
# print the JSON string representation of the object
print(PeriodScheduleDto2.to_json())

# convert the object into a dict
period_schedule_dto2_dict = period_schedule_dto2_instance.to_dict()
# create an instance of PeriodScheduleDto2 from a dict
period_schedule_dto2_from_dict = PeriodScheduleDto2.from_dict(period_schedule_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


