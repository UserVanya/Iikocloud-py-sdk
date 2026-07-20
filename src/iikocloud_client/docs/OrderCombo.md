# OrderCombo

Combo in order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Number of combos. | 
**id** | **UUID** | Combo ID. | 
**name** | **str** | Name of combo. | 
**price** | **float** | Price of combo. Given for 1 combo, without regard to amount. | 
**size** | [**ProductSize**](ProductSize.md) | Size. | [optional] 
**source_id** | **UUID** | Combo action ID. | 

## Example

```python
from iikocloud_client.models.order_combo import OrderCombo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCombo from a JSON string
order_combo_instance = OrderCombo.from_json(json)
# print the JSON string representation of the object
print(OrderCombo.to_json())

# convert the object into a dict
order_combo_dict = order_combo_instance.to_dict()
# create an instance of OrderCombo from a dict
order_combo_from_dict = OrderCombo.from_dict(order_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


