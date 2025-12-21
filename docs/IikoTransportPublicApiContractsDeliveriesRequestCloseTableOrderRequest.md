# IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest

Request for close table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cheque_additional_info** | [**IikoTransportPublicApiContractsDeliveriesCommonChequeAdditionalInfo**](IikoTransportPublicApiContractsDeliveriesCommonChequeAdditionalInfo.md) | Cheque additional information according to russian federal law #54. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_close_table_order_request import IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_close_table_order_request_instance = IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_close_table_order_request_dict = iiko_transport_public_api_contracts_deliveries_request_close_table_order_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_close_table_order_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_close_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


