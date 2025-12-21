# IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse

Wrapping object (external) for return of orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**orders** | [**List[IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo]**](IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo.md) | Orders. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_response_table_orders_response import IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse from a JSON string
iiko_transport_public_api_contracts_table_orders_response_table_orders_response_instance = IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_table_orders_response_table_orders_response_dict = iiko_transport_public_api_contracts_table_orders_response_table_orders_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse from a dict
iiko_transport_public_api_contracts_table_orders_response_table_orders_response_from_dict = IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse.from_dict(iiko_transport_public_api_contracts_table_orders_response_table_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


