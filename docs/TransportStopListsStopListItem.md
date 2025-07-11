# TransportStopListsStopListItem

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
from iikocloud_client.models.transport_stop_lists_stop_list_item import TransportStopListsStopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsStopListItem from a JSON string
transport_stop_lists_stop_list_item_instance = TransportStopListsStopListItem.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsStopListItem.to_json())

# convert the object into a dict
transport_stop_lists_stop_list_item_dict = transport_stop_lists_stop_list_item_instance.to_dict()
# create an instance of TransportStopListsStopListItem from a dict
transport_stop_lists_stop_list_item_from_dict = TransportStopListsStopListItem.from_dict(transport_stop_lists_stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


