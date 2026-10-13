# ResponsiblePerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full name of the responsible person; null if the name is not set | [optional] 
**role** | **str** | Role of the responsible person. Confirmed values: ACCOUNTANT — accountant, LEADER — leader, TECHNOLOGIST — technologist, WORKS_MANAGER — works manager; null if the role is not set | [optional] 

## Example

```python
from iikocloud_client.models.responsible_person import ResponsiblePerson

# TODO update the JSON string below
json = "{}"
# create an instance of ResponsiblePerson from a JSON string
responsible_person_instance = ResponsiblePerson.from_json(json)
# print the JSON string representation of the object
print(ResponsiblePerson.to_json())

# convert the object into a dict
responsible_person_dict = responsible_person_instance.to_dict()
# create an instance of ResponsiblePerson from a dict
responsible_person_from_dict = ResponsiblePerson.from_dict(responsible_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


