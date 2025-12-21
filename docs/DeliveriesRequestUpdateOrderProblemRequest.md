# DeliveriesRequestUpdateOrderProblemRequest

Request for order problem update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**has_problem** | **bool** | Problem flag. | 
**problem** | **str** | Problem text. | 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_problem_request import DeliveriesRequestUpdateOrderProblemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderProblemRequest from a JSON string
deliveries_request_update_order_problem_request_instance = DeliveriesRequestUpdateOrderProblemRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderProblemRequest.to_json())

# convert the object into a dict
deliveries_request_update_order_problem_request_dict = deliveries_request_update_order_problem_request_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderProblemRequest from a dict
deliveries_request_update_order_problem_request_from_dict = DeliveriesRequestUpdateOrderProblemRequest.from_dict(deliveries_request_update_order_problem_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


