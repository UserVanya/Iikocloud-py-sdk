# IikoTransportPublicApiContractsDeliveriesResponseOrderProblem

Order problem details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_problem** | **bool** | Has problem. | 
**description** | **str** | Problem description. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_problem import IikoTransportPublicApiContractsDeliveriesResponseOrderProblem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderProblem from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_problem_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderProblem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderProblem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_problem_dict = iiko_transport_public_api_contracts_deliveries_response_order_problem_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderProblem from a dict
iiko_transport_public_api_contracts_deliveries_response_order_problem_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderProblem.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_problem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


