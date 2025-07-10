# TransportDeliveriesResponseOrderEmployee

Employee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 
**phone** | **str** | Phone. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_employee import TransportDeliveriesResponseOrderEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderEmployee from a JSON string
transport_deliveries_response_order_employee_instance = TransportDeliveriesResponseOrderEmployee.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderEmployee.to_json())

# convert the object into a dict
transport_deliveries_response_order_employee_dict = transport_deliveries_response_order_employee_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderEmployee from a dict
transport_deliveries_response_order_employee_from_dict = TransportDeliveriesResponseOrderEmployee.from_dict(transport_deliveries_response_order_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


