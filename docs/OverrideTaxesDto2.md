# OverrideTaxesDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_type** | **str** | Order type GUID | [optional] [default to '']
**base_tax_category** | **str** | Base tax category GUID | [optional] [default to '']
**new_tax_category** | **str** | New tax category GUID | [optional] [default to '']

## Example

```python
from iikocloud_client.models.override_taxes_dto2 import OverrideTaxesDto2

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideTaxesDto2 from a JSON string
override_taxes_dto2_instance = OverrideTaxesDto2.from_json(json)
# print the JSON string representation of the object
print(OverrideTaxesDto2.to_json())

# convert the object into a dict
override_taxes_dto2_dict = override_taxes_dto2_instance.to_dict()
# create an instance of OverrideTaxesDto2 from a dict
override_taxes_dto2_from_dict = OverrideTaxesDto2.from_dict(override_taxes_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


