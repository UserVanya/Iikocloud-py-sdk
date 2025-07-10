# TransportDeliveriesResponseOrderProblem

Order problem details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_problem** | **bool** | Has problem. | 
**description** | **str** | Problem description. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_problem import TransportDeliveriesResponseOrderProblem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderProblem from a JSON string
transport_deliveries_response_order_problem_instance = TransportDeliveriesResponseOrderProblem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderProblem.to_json())

# convert the object into a dict
transport_deliveries_response_order_problem_dict = transport_deliveries_response_order_problem_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderProblem from a dict
transport_deliveries_response_order_problem_from_dict = TransportDeliveriesResponseOrderProblem.from_dict(transport_deliveries_response_order_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


