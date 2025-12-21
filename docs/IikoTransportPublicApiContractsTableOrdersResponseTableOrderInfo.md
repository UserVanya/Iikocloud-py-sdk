# IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Order ID. | 
**pos_id** | **UUID** | POS order ID. | [optional] 
**external_number** | **str** | Order external number. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**timestamp** | **int** | Timestamp of most recent order change that took place on iikoTransport server. | 
**creation_status** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCreationStatus**](IikoTransportPublicApiContractsDeliveriesResponseOrderCreationStatus.md) | Order creation status. In case of asynchronous creation, it allows to track the instance an order was validated/created in iikoFront. | 
**error_info** | [**IikoTransportPublicApiContractsErrorsErrorInfo**](IikoTransportPublicApiContractsErrorsErrorInfo.md) | Order creation error details.  &gt; Required only if \&quot;creationStatus\&quot;&#x3D;\&quot;Error\&quot;. | [optional] 
**order** | [**IikoTransportPublicApiContractsTableOrdersResponseTableOrder**](IikoTransportPublicApiContractsTableOrdersResponseTableOrder.md) | Order creation details.  &gt; Field is filled up if \&quot;creationStatus\&quot;&#x3D;\&quot;Success\&quot;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_response_table_order_info import IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo from a JSON string
iiko_transport_public_api_contracts_table_orders_response_table_order_info_instance = IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_table_orders_response_table_order_info_dict = iiko_transport_public_api_contracts_table_orders_response_table_order_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo from a dict
iiko_transport_public_api_contracts_table_orders_response_table_order_info_from_dict = IikoTransportPublicApiContractsTableOrdersResponseTableOrderInfo.from_dict(iiko_transport_public_api_contracts_table_orders_response_table_order_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


