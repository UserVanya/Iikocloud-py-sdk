# IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration

Suitable terminal group with delivery duration and other parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**delivery_duration_in_minutes** | **int** | Delivery duration in minutes. | 
**zone** | **str** | Delivery zone name which this TerminalGroupId belongs to. | 
**delivery_service_product_id** | **UUID** | Link to \&quot;delivery service payment\&quot;. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_allowed_item_with_duration import IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_instance = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_dict = iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration from a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_allowed_item_with_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


