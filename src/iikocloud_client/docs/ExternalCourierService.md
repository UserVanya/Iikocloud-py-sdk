# ExternalCourierService

ECS info (external courier service).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ECS setting record id. Unique through all organizations. | 
**name** | **str** | ECS name. | 

## Example

```python
from iikocloud_client.models.external_courier_service import ExternalCourierService

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalCourierService from a JSON string
external_courier_service_instance = ExternalCourierService.from_json(json)
# print the JSON string representation of the object
print(ExternalCourierService.to_json())

# convert the object into a dict
external_courier_service_dict = external_courier_service_instance.to_dict()
# create an instance of ExternalCourierService from a dict
external_courier_service_from_dict = ExternalCourierService.from_dict(external_courier_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


