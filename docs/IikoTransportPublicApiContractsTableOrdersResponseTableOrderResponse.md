# IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse

Wrapping object (external) for a delivery order return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order_info** | [**IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo**](IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo.md) | Order. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_response_table_order_response import IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse from a JSON string
iiko_transport_public_api_contracts_table_orders_response_table_order_response_instance = IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_table_orders_response_table_order_response_dict = iiko_transport_public_api_contracts_table_orders_response_table_order_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse from a dict
iiko_transport_public_api_contracts_table_orders_response_table_order_response_from_dict = IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse.from_dict(iiko_transport_public_api_contracts_table_orders_response_table_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


