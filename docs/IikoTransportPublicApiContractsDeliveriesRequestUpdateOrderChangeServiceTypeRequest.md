# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest

Request for change order's delivery type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_service_type** | **str** |  | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


