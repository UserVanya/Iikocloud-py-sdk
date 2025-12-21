# DeliveriesResponseOrderCourierInfo

Driver information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier** | [**DeliveriesResponseOrderEmployee**](DeliveriesResponseOrderEmployee.md) | Order driver. | 
**is_courier_selected_manually** | **bool** | Whether driver is selected manually. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_courier_info import DeliveriesResponseOrderCourierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderCourierInfo from a JSON string
deliveries_response_order_courier_info_instance = DeliveriesResponseOrderCourierInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderCourierInfo.to_json())

# convert the object into a dict
deliveries_response_order_courier_info_dict = deliveries_response_order_courier_info_instance.to_dict()
# create an instance of DeliveriesResponseOrderCourierInfo from a dict
deliveries_response_order_courier_info_from_dict = DeliveriesResponseOrderCourierInfo.from_dict(deliveries_response_order_courier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


