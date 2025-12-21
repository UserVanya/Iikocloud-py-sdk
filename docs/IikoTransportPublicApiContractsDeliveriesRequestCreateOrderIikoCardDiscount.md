# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **UUID** | Card program ID. | 
**program_name** | **str** | Card program name. | 
**discount_items** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscountItem]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscountItem.md) | Discount information for order items. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscount from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscount.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscount.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscount from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderIikoCardDiscount.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_iiko_card_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


