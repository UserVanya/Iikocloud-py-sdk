# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest

Request for order problem update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**has_problem** | **bool** | Problem flag. | 
**problem** | **str** | Problem text. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


