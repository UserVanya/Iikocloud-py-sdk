# InternalTransferCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**num** | **int** | Item sequence number | 
**product** | **str** | Product identifier (GUID) | 

## Example

```python
from iikocloud_client.models.internal_transfer_create_item import InternalTransferCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransferCreateItem from a JSON string
internal_transfer_create_item_instance = InternalTransferCreateItem.from_json(json)
# print the JSON string representation of the object
print(InternalTransferCreateItem.to_json())

# convert the object into a dict
internal_transfer_create_item_dict = internal_transfer_create_item_instance.to_dict()
# create an instance of InternalTransferCreateItem from a dict
internal_transfer_create_item_from_dict = InternalTransferCreateItem.from_dict(internal_transfer_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


