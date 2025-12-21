# IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem

Discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountType**](IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountType.md) | Discount type.                 Can be obtained by &#x60;/discounts&#x60; operation. | 
**sum** | **float** | Total. | 
**selective_positions** | **List[UUID]** | Order item positions. | [optional] 
**selective_positions_with_sum** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderPositionWithSum]**](IikoTransportPublicApiContractsDeliveriesResponseOrderPositionWithSum.md) | Order item positions with position discount sum.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_discount_item import IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_discount_item_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_discount_item_dict = iiko_transport_public_api_contracts_deliveries_response_order_discount_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem from a dict
iiko_transport_public_api_contracts_deliveries_response_order_discount_item_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderDiscountItem.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_discount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


