# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderOrderPaymentItem

Payments details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum** | **float** | Amount due | 
**payment_type_id** | **UUID** | Payment type ID. | 
**is_processed_externally** | **bool** | Payment item is processed by external payment system. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_order_payment_item import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderOrderPaymentItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderOrderPaymentItem from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_order_payment_item_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderOrderPaymentItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderOrderPaymentItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_order_payment_item_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_order_payment_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderOrderPaymentItem from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_order_payment_item_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderOrderPaymentItem.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_order_payment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


