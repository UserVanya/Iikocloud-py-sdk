# UpdateOrderCourierRequest

Request for order courier update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** | Courier ID.                Can be obtained by &#x60;/api/1/employees/couriers&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.update_order_courier_request import UpdateOrderCourierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderCourierRequest from a JSON string
update_order_courier_request_instance = UpdateOrderCourierRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderCourierRequest.to_json())

# convert the object into a dict
update_order_courier_request_dict = update_order_courier_request_instance.to_dict()
# create an instance of UpdateOrderCourierRequest from a dict
update_order_courier_request_from_dict = UpdateOrderCourierRequest.from_dict(update_order_courier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


