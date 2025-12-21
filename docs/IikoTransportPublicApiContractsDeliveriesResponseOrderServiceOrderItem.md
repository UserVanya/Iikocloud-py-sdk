# IikoTransportPublicApiContractsDeliveriesResponseOrderServiceOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderProduct**](IikoTransportPublicApiContractsDeliveriesResponseOrderProduct.md) | Item. | 
**cost** | **float** | Total cost per item without tax, discounts/surcharges. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_service_order_item import IikoTransportPublicApiContractsDeliveriesResponseOrderServiceOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderServiceOrderItem from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_service_order_item_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderServiceOrderItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderServiceOrderItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_service_order_item_dict = iiko_transport_public_api_contracts_deliveries_response_order_service_order_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderServiceOrderItem from a dict
iiko_transport_public_api_contracts_deliveries_response_order_service_order_item_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderServiceOrderItem.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_service_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


