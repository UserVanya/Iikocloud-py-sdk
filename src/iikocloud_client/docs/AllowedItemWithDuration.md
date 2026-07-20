# AllowedItemWithDuration

Suitable terminal group with delivery duration and other parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_duration_in_minutes** | **int** | Delivery duration in minutes. | 
**delivery_service_product_id** | **UUID** | Link to \&quot;delivery service payment\&quot;. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**zone** | **str** | Delivery zone name which this TerminalGroupId belongs to. | 

## Example

```python
from iikocloud_client.models.allowed_item_with_duration import AllowedItemWithDuration

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedItemWithDuration from a JSON string
allowed_item_with_duration_instance = AllowedItemWithDuration.from_json(json)
# print the JSON string representation of the object
print(AllowedItemWithDuration.to_json())

# convert the object into a dict
allowed_item_with_duration_dict = allowed_item_with_duration_instance.to_dict()
# create an instance of AllowedItemWithDuration from a dict
allowed_item_with_duration_from_dict = AllowedItemWithDuration.from_dict(allowed_item_with_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


