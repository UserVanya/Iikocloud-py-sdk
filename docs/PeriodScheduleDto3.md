# PeriodScheduleDto3

Schedule availability interval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** | Start time | 
**end** | **str** | End time | 
**days_of_week** | **List[str]** | Availability days of week | 

## Example

```python
from iikocloud_client.models.period_schedule_dto3 import PeriodScheduleDto3

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodScheduleDto3 from a JSON string
period_schedule_dto3_instance = PeriodScheduleDto3.from_json(json)
# print the JSON string representation of the object
print(PeriodScheduleDto3.to_json())

# convert the object into a dict
period_schedule_dto3_dict = period_schedule_dto3_instance.to_dict()
# create an instance of PeriodScheduleDto3 from a dict
period_schedule_dto3_from_dict = PeriodScheduleDto3.from_dict(period_schedule_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


