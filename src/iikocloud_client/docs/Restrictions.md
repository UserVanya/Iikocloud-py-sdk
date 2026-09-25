# Restrictions

Modifier selection restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_quantity** | **float** | Default quantity. | [optional] 
**free_quantity** | **float** | Free quantity. | [optional] 
**hide_if_default_quantity** | **bool** | Hide if quantity equals default quantity. | [optional] 
**max_quantity** | **float** | Maximum quantity. | [optional] 
**min_quantity** | **float** | Minimum quantity. | [optional] 

## Example

```python
from iikocloud_client.models.restrictions import Restrictions

# TODO update the JSON string below
json = "{}"
# create an instance of Restrictions from a JSON string
restrictions_instance = Restrictions.from_json(json)
# print the JSON string representation of the object
print(Restrictions.to_json())

# convert the object into a dict
restrictions_dict = restrictions_instance.to_dict()
# create an instance of Restrictions from a dict
restrictions_from_dict = Restrictions.from_dict(restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


