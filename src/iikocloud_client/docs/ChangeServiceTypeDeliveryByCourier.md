# ChangeServiceTypeDeliveryByCourier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_point** | [**DeliveryOrderCreatePoint**](DeliveryOrderCreatePoint.md) | Address of delivery. | 

## Example

```python
from iikocloud_client.models.change_service_type_delivery_by_courier import ChangeServiceTypeDeliveryByCourier

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeServiceTypeDeliveryByCourier from a JSON string
change_service_type_delivery_by_courier_instance = ChangeServiceTypeDeliveryByCourier.from_json(json)
# print the JSON string representation of the object
print(ChangeServiceTypeDeliveryByCourier.to_json())

# convert the object into a dict
change_service_type_delivery_by_courier_dict = change_service_type_delivery_by_courier_instance.to_dict()
# create an instance of ChangeServiceTypeDeliveryByCourier from a dict
change_service_type_delivery_by_courier_from_dict = ChangeServiceTypeDeliveryByCourier.from_dict(change_service_type_delivery_by_courier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


