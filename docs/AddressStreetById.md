# AddressStreetById

Street by id response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Street id. | 
**classifier_id** | **str** | Street classifierId. | [optional] 
**city_id** | **str** | City id. | 
**city_name** | **str** | City name. | 
**street_name** | **str** | Street name. | 

## Example

```python
from iikocloud_client.models.address_street_by_id import AddressStreetById

# TODO update the JSON string below
json = "{}"
# create an instance of AddressStreetById from a JSON string
address_street_by_id_instance = AddressStreetById.from_json(json)
# print the JSON string representation of the object
print(AddressStreetById.to_json())

# convert the object into a dict
address_street_by_id_dict = address_street_by_id_instance.to_dict()
# create an instance of AddressStreetById from a dict
address_street_by_id_from_dict = AddressStreetById.from_dict(address_street_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


