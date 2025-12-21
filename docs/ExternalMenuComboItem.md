# ExternalMenuComboItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sizes** | [**List[ExternalMenuComboItemSize]**](ExternalMenuComboItemSize.md) |  | 
**groups** | [**List[ComboGroupDto4]**](ComboGroupDto4.md) |  | [optional] 
**price_strategy** | **str** | Price strategy | [optional] [default to 'BY_COMPONENT']
**sku** | **str** | Product code | [optional] [default to '']
**name** | **str** | Product name | [optional] [default to '']
**description** | **str** | Product description | [optional] [default to '']
**is_marked** | **bool** | Marking flag | [optional] [default to False]
**barcodes** | [**List[BarcodeDto4]**](BarcodeDto4.md) |  | [optional] 
**type** | **str** |  | 
**id** | **str** | Product ID | 

## Example

```python
from iikocloud_client.models.external_menu_combo_item import ExternalMenuComboItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuComboItem from a JSON string
external_menu_combo_item_instance = ExternalMenuComboItem.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuComboItem.to_json())

# convert the object into a dict
external_menu_combo_item_dict = external_menu_combo_item_instance.to_dict()
# create an instance of ExternalMenuComboItem from a dict
external_menu_combo_item_from_dict = ExternalMenuComboItem.from_dict(external_menu_combo_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


