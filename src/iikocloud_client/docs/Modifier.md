# Modifier

Modifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Quantity. | 
**position_id** | **UUID** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 
**price** | **float** | Unit price. | [optional] 
**product_group_id** | **UUID** | Modifiers group ID (for group modifier). Required for a group modifier.                Can be obtained by &#x60;/api/1/nomenclature&#x60; operation. | [optional] 
**product_id** | **UUID** | Modifier item ID.                Can be obtained by &#x60;/api/1/nomenclature&#x60; operation. | 

## Example

```python
from iikocloud_client.models.modifier import Modifier

# TODO update the JSON string below
json = "{}"
# create an instance of Modifier from a JSON string
modifier_instance = Modifier.from_json(json)
# print the JSON string representation of the object
print(Modifier.to_json())

# convert the object into a dict
modifier_dict = modifier_instance.to_dict()
# create an instance of Modifier from a dict
modifier_from_dict = Modifier.from_dict(modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


