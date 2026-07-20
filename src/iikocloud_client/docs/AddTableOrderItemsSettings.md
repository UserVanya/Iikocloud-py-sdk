# AddTableOrderItemsSettings

Add table order items options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_print** | **bool** | Auto service print is needed. | [optional] 

## Example

```python
from iikocloud_client.models.add_table_order_items_settings import AddTableOrderItemsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AddTableOrderItemsSettings from a JSON string
add_table_order_items_settings_instance = AddTableOrderItemsSettings.from_json(json)
# print the JSON string representation of the object
print(AddTableOrderItemsSettings.to_json())

# convert the object into a dict
add_table_order_items_settings_dict = add_table_order_items_settings_instance.to_dict()
# create an instance of AddTableOrderItemsSettings from a dict
add_table_order_items_settings_from_dict = AddTableOrderItemsSettings.from_dict(add_table_order_items_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


