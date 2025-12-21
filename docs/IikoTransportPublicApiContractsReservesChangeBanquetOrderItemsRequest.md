# IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest

Request to change banquet order items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Banquet ID. | 
**items** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | [optional] 
**combos** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderCombo.md) | Combos. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request import IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest from a JSON string
iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request_instance = IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request_dict = iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest from a dict
iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request_from_dict = IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest.from_dict(iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


