# TransportDeliveriesResponseOrderCourierInfo

Driver information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier** | [**TransportDeliveriesResponseOrderEmployee**](TransportDeliveriesResponseOrderEmployee.md) | Order driver. | 
**is_courier_selected_manually** | **bool** | Whether driver is selected manually. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_courier_info import TransportDeliveriesResponseOrderCourierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderCourierInfo from a JSON string
transport_deliveries_response_order_courier_info_instance = TransportDeliveriesResponseOrderCourierInfo.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderCourierInfo.to_json())

# convert the object into a dict
transport_deliveries_response_order_courier_info_dict = transport_deliveries_response_order_courier_info_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderCourierInfo from a dict
transport_deliveries_response_order_courier_info_from_dict = TransportDeliveriesResponseOrderCourierInfo.from_dict(transport_deliveries_response_order_courier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


