# IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItemData

Reject additional information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Point work time start. | [optional] 
**date_to** | **str** | Point work time end. | [optional] 
**allowed_week_days** | **List[str]** | Allowed week days. | [optional] 
**min_sum** | **float** | Order min sum. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_data import IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItemData

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItemData from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_data_instance = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItemData.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItemData.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_data_dict = iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_data_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItemData from a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_data_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItemData.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_reject_item_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


