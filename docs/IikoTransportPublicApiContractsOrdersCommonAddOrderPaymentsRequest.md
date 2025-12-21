# IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest

Request for add order payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**tips** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderTipsPayment.md) | Order tips. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**payments** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderPayment]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderPayment.md) | Order payments. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_orders_common_add_order_payments_request import IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest from a JSON string
iiko_transport_public_api_contracts_orders_common_add_order_payments_request_instance = IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_orders_common_add_order_payments_request_dict = iiko_transport_public_api_contracts_orders_common_add_order_payments_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest from a dict
iiko_transport_public_api_contracts_orders_common_add_order_payments_request_from_dict = IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest.from_dict(iiko_transport_public_api_contracts_orders_common_add_order_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


