# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderComboItemInformation

Combo details if order item belongs to combo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_id** | **UUID** | Created combo ID.  Must be one of combos.id generated values. | 
**combo_source_id** | **UUID** | Action ID that defines combo. | 
**combo_group_id** | **UUID** | Combo group ID to which item belongs. | 
**combo_group_name** | **str** | Combo group name to which item belongs. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_combo_item_information import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderComboItemInformation

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderComboItemInformation from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_combo_item_information_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderComboItemInformation.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderComboItemInformation.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_combo_item_information_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_combo_item_information_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderComboItemInformation from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_combo_item_information_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderComboItemInformation.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_combo_item_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


