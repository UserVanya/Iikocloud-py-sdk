# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest

Change order's payments request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**payments** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderPayment]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderPayment.md) | Order payments. | 
**tips** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment.md) | Order tips. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


