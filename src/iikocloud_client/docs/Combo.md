# Combo

Combo in order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Quantity. | 
**id** | **UUID** | Combo ID.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid(). | 
**name** | **str** | Name of combo. | 
**price** | **float** | Price of one combo. | 
**program_id** | **UUID** | Card program ID.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**size_id** | **UUID** | Size ID. Required if combo has a size scale.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 
**source_id** | **UUID** | Combo validity ID. | 

## Example

```python
from iikocloud_client.models.combo import Combo

# TODO update the JSON string below
json = "{}"
# create an instance of Combo from a JSON string
combo_instance = Combo.from_json(json)
# print the JSON string representation of the object
print(Combo.to_json())

# convert the object into a dict
combo_dict = combo_instance.to_dict()
# create an instance of Combo from a dict
combo_from_dict = Combo.from_dict(combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


