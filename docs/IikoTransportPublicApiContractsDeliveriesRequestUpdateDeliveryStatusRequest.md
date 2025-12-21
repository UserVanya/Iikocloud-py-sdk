# IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest

Request for delivery status update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**delivery_status** | [**IikoTransportPublicApiContractsDeliveriesCommonDeliveryStatusForUpdate**](IikoTransportPublicApiContractsDeliveriesCommonDeliveryStatusForUpdate.md) | Delivery status. Can be only switched between these three statuses. | 
**delivery_date** | **str** | The date and time when the order was received by the guest (Local for delivery terminal). | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


