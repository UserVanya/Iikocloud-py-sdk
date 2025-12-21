# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest

Request for order courier update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**employee_id** | **UUID** | Courier ID.                Can be obtained by &#x60;/employees/couriers&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


