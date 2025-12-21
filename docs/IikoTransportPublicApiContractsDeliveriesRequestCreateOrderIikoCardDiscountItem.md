# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscountItem

Card discount/surcharge item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **UUID** | Position ID of order item. | 
**sum** | **float** | Discount/surcharge sum. | 
**amount** | **float** | Amount. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_item import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscountItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscountItem from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_item_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscountItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscountItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_item_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscountItem from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_item_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscountItem.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


