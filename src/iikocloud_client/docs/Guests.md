# Guests

Information on guests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of persons in order. This field defines the number of cutlery sets | 
**split_between_persons** | **bool** | Attribute that shows whether order must be split among guests. | [optional] 

## Example

```python
from iikocloud_client.models.guests import Guests

# TODO update the JSON string below
json = "{}"
# create an instance of Guests from a JSON string
guests_instance = Guests.from_json(json)
# print the JSON string representation of the object
print(Guests.to_json())

# convert the object into a dict
guests_dict = guests_instance.to_dict()
# create an instance of Guests from a dict
guests_from_dict = Guests.from_dict(guests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


