# InternalTransferGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**amount_unit** | **str** | Unit of measure identifier (GUID) | [optional] 
**container_id** | **str** | Container identifier (GUID) | [optional] 
**num** | **int** | Item sequence number | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.internal_transfer_get_item import InternalTransferGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransferGetItem from a JSON string
internal_transfer_get_item_instance = InternalTransferGetItem.from_json(json)
# print the JSON string representation of the object
print(InternalTransferGetItem.to_json())

# convert the object into a dict
internal_transfer_get_item_dict = internal_transfer_get_item_instance.to_dict()
# create an instance of InternalTransferGetItem from a dict
internal_transfer_get_item_from_dict = InternalTransferGetItem.from_dict(internal_transfer_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


