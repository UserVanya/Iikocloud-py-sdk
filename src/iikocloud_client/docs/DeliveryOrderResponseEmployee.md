# DeliveryOrderResponseEmployee

Employee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 
**phone** | **str** | Phone. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_employee import DeliveryOrderResponseEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseEmployee from a JSON string
delivery_order_response_employee_instance = DeliveryOrderResponseEmployee.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseEmployee.to_json())

# convert the object into a dict
delivery_order_response_employee_dict = delivery_order_response_employee_instance.to_dict()
# create an instance of DeliveryOrderResponseEmployee from a dict
delivery_order_response_employee_from_dict = DeliveryOrderResponseEmployee.from_dict(delivery_order_response_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


