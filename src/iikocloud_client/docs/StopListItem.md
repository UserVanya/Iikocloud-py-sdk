# StopListItem

Out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | Product balance. | 
**date_add** | **str** | Date the product was added to the out-of-stock list (UTC). | [optional] 
**product_id** | **UUID** | Out-of-stock list product ID. | 
**size_id** | **UUID** | Product size. | [optional] 
**sku** | **str** | Stock keeping unit. | [optional] 

## Example

```python
from iikocloud_client.models.stop_list_item import StopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of StopListItem from a JSON string
stop_list_item_instance = StopListItem.from_json(json)
# print the JSON string representation of the object
print(StopListItem.to_json())

# convert the object into a dict
stop_list_item_dict = stop_list_item_instance.to_dict()
# create an instance of StopListItem from a dict
stop_list_item_from_dict = StopListItem.from_dict(stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


