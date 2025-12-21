# IikoTransportPublicApiContractsDeliveriesResponseOrdersByOrganization

Orders grouped by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**orders** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderInfo]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderInfo.md) | List of orders by organization. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_orders_by_organization import IikoTransportPublicApiContractsDeliveriesResponseOrdersByOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrdersByOrganization from a JSON string
iiko_transport_public_api_contracts_deliveries_response_orders_by_organization_instance = IikoTransportPublicApiContractsDeliveriesResponseOrdersByOrganization.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrdersByOrganization.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_orders_by_organization_dict = iiko_transport_public_api_contracts_deliveries_response_orders_by_organization_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrdersByOrganization from a dict
iiko_transport_public_api_contracts_deliveries_response_orders_by_organization_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrdersByOrganization.from_dict(iiko_transport_public_api_contracts_deliveries_response_orders_by_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


