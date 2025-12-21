# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest

Request for order payment update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**payment_items** | [**List[IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderOrderPaymentItem]**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderOrderPaymentItem.md) | Payment details. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


