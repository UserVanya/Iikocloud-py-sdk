# IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest

Request for add order items to banquet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserve_id** | **UUID** | Banquet ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**combos** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request import IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest from a JSON string
iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request_instance = IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request_dict = iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest from a dict
iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request_from_dict = IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest.from_dict(iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


