# Conception

Concept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code. | 
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.conception import Conception

# TODO update the JSON string below
json = "{}"
# create an instance of Conception from a JSON string
conception_instance = Conception.from_json(json)
# print the JSON string representation of the object
print(Conception.to_json())

# convert the object into a dict
conception_dict = conception_instance.to_dict()
# create an instance of Conception from a dict
conception_from_dict = Conception.from_dict(conception_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


