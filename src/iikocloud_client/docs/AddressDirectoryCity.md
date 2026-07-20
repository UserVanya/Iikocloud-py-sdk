# AddressDirectoryCity

City DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | City additional information. | [optional] 
**classifier_id** | **str** | ID in classifier, e.g., address database. | [optional] 
**external_revision** | **int** | External revision. | [optional] 
**id** | **UUID** | City ID in RMS. | 
**is_deleted** | **bool** | Is-Deleted attribute. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.address_directory_city import AddressDirectoryCity

# TODO update the JSON string below
json = "{}"
# create an instance of AddressDirectoryCity from a JSON string
address_directory_city_instance = AddressDirectoryCity.from_json(json)
# print the JSON string representation of the object
print(AddressDirectoryCity.to_json())

# convert the object into a dict
address_directory_city_dict = address_directory_city_instance.to_dict()
# create an instance of AddressDirectoryCity from a dict
address_directory_city_from_dict = AddressDirectoryCity.from_dict(address_directory_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


