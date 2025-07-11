# TransportDeliveryRestrictionsAllowedRestrictionsRejectItemData

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
from iikocloud_client.models.transport_delivery_restrictions_allowed_restrictions_reject_item_data import TransportDeliveryRestrictionsAllowedRestrictionsRejectItemData

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsRejectItemData from a JSON string
transport_delivery_restrictions_allowed_restrictions_reject_item_data_instance = TransportDeliveryRestrictionsAllowedRestrictionsRejectItemData.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsAllowedRestrictionsRejectItemData.to_json())

# convert the object into a dict
transport_delivery_restrictions_allowed_restrictions_reject_item_data_dict = transport_delivery_restrictions_allowed_restrictions_reject_item_data_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsRejectItemData from a dict
transport_delivery_restrictions_allowed_restrictions_reject_item_data_from_dict = TransportDeliveryRestrictionsAllowedRestrictionsRejectItemData.from_dict(transport_delivery_restrictions_allowed_restrictions_reject_item_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


