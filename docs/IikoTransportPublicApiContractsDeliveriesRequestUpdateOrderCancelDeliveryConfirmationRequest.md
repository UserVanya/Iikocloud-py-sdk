# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest

Request for cancel delivery confirmation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


