# IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItem

Rejected item info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**zone** | **str** | Delivery zone name which this TerminalGroupId belongs to. | [optional] 
**reject_code** | [**IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsDeliveryRestrictionRejectCode**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsDeliveryRestrictionRejectCode.md) | Reject cause code. | 
**reject_hint** | **str** | Reject hint. | 
**reject_item_data** | [**IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItemData**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItemData.md) | Reject additional information. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item import IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItem from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_instance = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_dict = iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItem from a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItem.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


