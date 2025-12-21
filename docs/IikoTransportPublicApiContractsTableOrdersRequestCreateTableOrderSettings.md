# IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderSettings

Table order creation options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_print** | **bool** | Auto service print is needed. | [optional] 
**transport_to_front_timeout** | **int** | Timeout in seconds that specifies how much time is given for order to reach iikoFront.   After this time, order is nullified if iikoFront doesn&#39;t take it. By default - 8 seconds. | [optional] 
**check_stop_list** | **bool** | Flag indicating whether there&#39;s need to check order items in out-of-stock list.                Unable if &#x60;terminalGroupId&#x60; is null. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_create_table_order_settings import IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderSettings

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderSettings from a JSON string
iiko_transport_public_api_contracts_table_orders_request_create_table_order_settings_instance = IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderSettings.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderSettings.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_table_orders_request_create_table_order_settings_dict = iiko_transport_public_api_contracts_table_orders_request_create_table_order_settings_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderSettings from a dict
iiko_transport_public_api_contracts_table_orders_request_create_table_order_settings_from_dict = IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderSettings.from_dict(iiko_transport_public_api_contracts_table_orders_request_create_table_order_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


