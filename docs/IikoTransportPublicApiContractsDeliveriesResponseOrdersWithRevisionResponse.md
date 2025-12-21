# IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse

Wrapping object (external) for return of delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**max_revision** | **int** | Maximum revision value per all orders. | 
**orders_by_organizations** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrdersByOrganization]**](IikoTransportPublicApiContractsDeliveriesResponseOrdersByOrganization.md) | Orders. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response import IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse from a JSON string
iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response_instance = IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response_dict = iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse from a dict
iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrdersWithRevisionResponse.from_dict(iiko_transport_public_api_contracts_deliveries_response_orders_with_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


