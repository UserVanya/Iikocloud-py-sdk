# TransportDeliveriesRequestUpdateOrderProblemRequest

Request for order problem update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 
**has_problem** | **bool** | Problem flag. | 
**problem** | **str** | Problem text. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_update_order_problem_request import TransportDeliveriesRequestUpdateOrderProblemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestUpdateOrderProblemRequest from a JSON string
transport_deliveries_request_update_order_problem_request_instance = TransportDeliveriesRequestUpdateOrderProblemRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestUpdateOrderProblemRequest.to_json())

# convert the object into a dict
transport_deliveries_request_update_order_problem_request_dict = transport_deliveries_request_update_order_problem_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestUpdateOrderProblemRequest from a dict
transport_deliveries_request_update_order_problem_request_from_dict = TransportDeliveriesRequestUpdateOrderProblemRequest.from_dict(transport_deliveries_request_update_order_problem_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


