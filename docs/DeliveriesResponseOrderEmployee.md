# DeliveriesResponseOrderEmployee

Employee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 
**phone** | **str** | Phone. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_employee import DeliveriesResponseOrderEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderEmployee from a JSON string
deliveries_response_order_employee_instance = DeliveriesResponseOrderEmployee.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderEmployee.to_json())

# convert the object into a dict
deliveries_response_order_employee_dict = deliveries_response_order_employee_instance.to_dict()
# create an instance of DeliveriesResponseOrderEmployee from a dict
deliveries_response_order_employee_from_dict = DeliveriesResponseOrderEmployee.from_dict(deliveries_response_order_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


