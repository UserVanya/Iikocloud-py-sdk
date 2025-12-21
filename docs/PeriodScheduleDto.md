# PeriodScheduleDto

Schedule availability interval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** | Start time | 
**end** | **str** | End time | 
**days_of_week** | **List[str]** | Availability days of week | 

## Example

```python
from iikocloud_client.models.period_schedule_dto import PeriodScheduleDto

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodScheduleDto from a JSON string
period_schedule_dto_instance = PeriodScheduleDto.from_json(json)
# print the JSON string representation of the object
print(PeriodScheduleDto.to_json())

# convert the object into a dict
period_schedule_dto_dict = period_schedule_dto_instance.to_dict()
# create an instance of PeriodScheduleDto from a dict
period_schedule_dto_from_dict = PeriodScheduleDto.from_dict(period_schedule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


