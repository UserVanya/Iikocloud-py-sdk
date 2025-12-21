# IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**status** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemStatus**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemStatus.md) | Item cooking status. | 
**deleted** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderItemDeletedInfo**](IikoTransportPublicApiContractsDeliveriesResponseOrderItemDeletedInfo.md) | Item deletion details. If filled up, item is deleted. | [optional] 
**amount** | **float** | Quantity. | 
**comment** | **str** | Comment. | [optional] 
**when_printed** | **str** | Printing time (Local for the terminal). | [optional] 
**size** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderProductSize**](IikoTransportPublicApiContractsDeliveriesResponseOrderProductSize.md) | Size. | [optional] 
**combo_information** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderComboItemInformation**](IikoTransportPublicApiContractsDeliveriesResponseOrderComboItemInformation.md) | Combo details, if order item is part of combo. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_order_item import IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_order_item_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_item_dict = iiko_transport_public_api_contracts_deliveries_response_order_order_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem from a dict
iiko_transport_public_api_contracts_deliveries_response_order_order_item_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItem.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


