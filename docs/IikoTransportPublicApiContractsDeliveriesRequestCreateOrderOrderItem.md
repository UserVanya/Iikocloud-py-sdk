# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**amount** | **float** | Quantity. | 
**product_size_id** | **UUID** | Size ID. Required if a stock list item has a size scale. | [optional] 
**combo_information** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderComboItemInformation**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderComboItemInformation.md) | Combo details if combo includes order item. | [optional] 
**comment** | **str** | Comment. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_order_item import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_order_item_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_order_item_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_order_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_order_item_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrderItem.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


