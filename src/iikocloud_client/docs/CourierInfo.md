# CourierInfo

Driver information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier** | [**DeliveryOrderResponseEmployee**](DeliveryOrderResponseEmployee.md) | Order driver. | 
**is_courier_selected_manually** | **bool** | Whether driver is selected manually. | 

## Example

```python
from iikocloud_client.models.courier_info import CourierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CourierInfo from a JSON string
courier_info_instance = CourierInfo.from_json(json)
# print the JSON string representation of the object
print(CourierInfo.to_json())

# convert the object into a dict
courier_info_dict = courier_info_instance.to_dict()
# create an instance of CourierInfo from a dict
courier_info_from_dict = CourierInfo.from_dict(courier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


