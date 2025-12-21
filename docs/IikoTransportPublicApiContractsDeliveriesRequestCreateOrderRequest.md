# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest

Order creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID of the new order.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Front group ID the order must be sent to.    Can be obtained by &#x60;/terminal_groups&#x60; operation. | [optional] 
**create_order_settings** | [**IikoTransportPublicApiContractsOrdersCommonCreateOrderSettings**](IikoTransportPublicApiContractsOrdersCommonCreateOrderSettings.md) | Order creation parameters. | [optional] 
**order** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryOrder**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDeliveryOrder.md) | Order. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_request import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_request_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_request_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


