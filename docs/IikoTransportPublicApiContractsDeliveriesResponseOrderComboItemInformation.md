# IikoTransportPublicApiContractsDeliveriesResponseOrderComboItemInformation

Information on order item to combo relation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_id** | **UUID** | New combo ID. | 
**combo_source_id** | **UUID** | Action ID that defines combo. | 
**group_id** | **UUID** | Combo group ID to which item belongs. | 
**group_name** | **str** | Combo group name to which item belongs. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_combo_item_information import IikoTransportPublicApiContractsDeliveriesResponseOrderComboItemInformation

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderComboItemInformation from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_combo_item_information_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderComboItemInformation.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderComboItemInformation.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_combo_item_information_dict = iiko_transport_public_api_contracts_deliveries_response_order_combo_item_information_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderComboItemInformation from a dict
iiko_transport_public_api_contracts_deliveries_response_order_combo_item_information_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderComboItemInformation.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_combo_item_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


