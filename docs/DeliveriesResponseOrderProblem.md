# DeliveriesResponseOrderProblem

Order problem details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_problem** | **bool** | Has problem. | 
**description** | **str** | Problem description. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_problem import DeliveriesResponseOrderProblem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderProblem from a JSON string
deliveries_response_order_problem_instance = DeliveriesResponseOrderProblem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderProblem.to_json())

# convert the object into a dict
deliveries_response_order_problem_dict = deliveries_response_order_problem_instance.to_dict()
# create an instance of DeliveriesResponseOrderProblem from a dict
deliveries_response_order_problem_from_dict = DeliveriesResponseOrderProblem.from_dict(deliveries_response_order_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


