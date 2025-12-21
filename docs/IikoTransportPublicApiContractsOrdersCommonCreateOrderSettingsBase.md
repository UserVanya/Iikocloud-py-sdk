# IikoTransportPublicApiContractsOrdersCommonCreateOrderSettingsBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_to_front_timeout** | **int** | Timeout in seconds that specifies how much time is given for order to reach iikoFront.   After this time, order is nullified if iikoFront doesn&#39;t take it. By default - 8 seconds. | [optional] 
**check_stop_list** | **bool** | Flag indicating whether there&#39;s need to check order items in out-of-stock list.                Unable if &#x60;terminalGroupId&#x60; is null. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_orders_common_create_order_settings_base import IikoTransportPublicApiContractsOrdersCommonCreateOrderSettingsBase

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrdersCommonCreateOrderSettingsBase from a JSON string
iiko_transport_public_api_contracts_orders_common_create_order_settings_base_instance = IikoTransportPublicApiContractsOrdersCommonCreateOrderSettingsBase.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrdersCommonCreateOrderSettingsBase.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_orders_common_create_order_settings_base_dict = iiko_transport_public_api_contracts_orders_common_create_order_settings_base_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrdersCommonCreateOrderSettingsBase from a dict
iiko_transport_public_api_contracts_orders_common_create_order_settings_base_from_dict = IikoTransportPublicApiContractsOrdersCommonCreateOrderSettingsBase.from_dict(iiko_transport_public_api_contracts_orders_common_create_order_settings_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


