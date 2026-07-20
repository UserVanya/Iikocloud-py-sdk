# RejectItem

Rejected item info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reject_code** | [**DeliveryRestrictionRejectCode**](DeliveryRestrictionRejectCode.md) | Reject cause code. | 
**reject_hint** | **str** | Reject hint. | 
**reject_item_data** | [**RejectItemData**](RejectItemData.md) | Reject additional information. | [optional] 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**zone** | **str** | Delivery zone name which this TerminalGroupId belongs to. | [optional] 

## Example

```python
from iikocloud_client.models.reject_item import RejectItem

# TODO update the JSON string below
json = "{}"
# create an instance of RejectItem from a JSON string
reject_item_instance = RejectItem.from_json(json)
# print the JSON string representation of the object
print(RejectItem.to_json())

# convert the object into a dict
reject_item_dict = reject_item_instance.to_dict()
# create an instance of RejectItem from a dict
reject_item_from_dict = RejectItem.from_dict(reject_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


