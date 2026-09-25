# TaxCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Tax category UUID. string (UUID) | [optional] 
**is_deleted** | **bool** | Deleted flag | [optional] 
**name** | **str** | Display name | [optional] 

## Example

```python
from iikocloud_client.models.tax_category import TaxCategory

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCategory from a JSON string
tax_category_instance = TaxCategory.from_json(json)
# print the JSON string representation of the object
print(TaxCategory.to_json())

# convert the object into a dict
tax_category_dict = tax_category_instance.to_dict()
# create an instance of TaxCategory from a dict
tax_category_from_dict = TaxCategory.from_dict(tax_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


