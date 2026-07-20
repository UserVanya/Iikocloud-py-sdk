# IdentifierCode

Product code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Product code value. | [optional] 

## Example

```python
from iikocloud_client.models.identifier_code import IdentifierCode

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifierCode from a JSON string
identifier_code_instance = IdentifierCode.from_json(json)
# print the JSON string representation of the object
print(IdentifierCode.to_json())

# convert the object into a dict
identifier_code_dict = identifier_code_instance.to_dict()
# create an instance of IdentifierCode from a dict
identifier_code_from_dict = IdentifierCode.from_dict(identifier_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


