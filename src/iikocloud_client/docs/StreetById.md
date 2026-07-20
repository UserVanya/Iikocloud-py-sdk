# StreetById

Street by id response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city_id** | **UUID** | City id. | 
**city_name** | **str** | City name. | 
**classifier_id** | **str** | Street classifierId. | [optional] 
**id** | **UUID** | Street id. | 
**street_name** | **str** | Street name. | 

## Example

```python
from iikocloud_client.models.street_by_id import StreetById

# TODO update the JSON string below
json = "{}"
# create an instance of StreetById from a JSON string
street_by_id_instance = StreetById.from_json(json)
# print the JSON string representation of the object
print(StreetById.to_json())

# convert the object into a dict
street_by_id_dict = street_by_id_instance.to_dict()
# create an instance of StreetById from a dict
street_by_id_from_dict = StreetById.from_dict(street_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


