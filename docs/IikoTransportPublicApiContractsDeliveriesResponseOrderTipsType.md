# IikoTransportPublicApiContractsDeliveriesResponseOrderTipsType

The tips type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Tips type ID.                Can be obtained by &#x60;/tips_types&#x60; operation. | 
**name** | **str** | Tips type name. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_tips_type import IikoTransportPublicApiContractsDeliveriesResponseOrderTipsType

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderTipsType from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_tips_type_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderTipsType.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderTipsType.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_tips_type_dict = iiko_transport_public_api_contracts_deliveries_response_order_tips_type_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderTipsType from a dict
iiko_transport_public_api_contracts_deliveries_response_order_tips_type_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderTipsType.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_tips_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


