# UpdateOrderProblemRequest

Request for order problem update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_problem** | **bool** | Problem flag. | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**problem** | **str** | Problem text. | 

## Example

```python
from iikocloud_client.models.update_order_problem_request import UpdateOrderProblemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderProblemRequest from a JSON string
update_order_problem_request_instance = UpdateOrderProblemRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderProblemRequest.to_json())

# convert the object into a dict
update_order_problem_request_dict = update_order_problem_request_instance.to_dict()
# create an instance of UpdateOrderProblemRequest from a dict
update_order_problem_request_from_dict = UpdateOrderProblemRequest.from_dict(update_order_problem_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


