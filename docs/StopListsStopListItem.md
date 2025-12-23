# StopListsStopListItem

Out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | Product balance. | 
**product_id** | **str** | Out-of-stock list product ID. | 
**size_id** | **str** | Product size. | [optional] 
**sku** | **str** | Stock keeping unit. | [optional] 
**date_add** | **str** | Date the product was added to the out-of-stock list (UTC). | [optional] 

## Example

```python
from iikocloud_client.models.stop_lists_stop_list_item import StopListsStopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsStopListItem from a JSON string
stop_lists_stop_list_item_instance = StopListsStopListItem.from_json(json)
# print the JSON string representation of the object
print(StopListsStopListItem.to_json())

# convert the object into a dict
stop_lists_stop_list_item_dict = stop_lists_stop_list_item_instance.to_dict()
# create an instance of StopListsStopListItem from a dict
stop_lists_stop_list_item_from_dict = StopListsStopListItem.from_dict(stop_lists_stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


