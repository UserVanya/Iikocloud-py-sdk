# AddressCity

City DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | City ID in RMS. | 
**name** | **str** | Name. | 
**external_revision** | **int** | External revision. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | 
**classifier_id** | **str** | ID in classifier, e.g., address database. | [optional] 
**additional_info** | **str** | City additional information. | [optional] 

## Example

```python
from iikocloud_client.models.address_city import AddressCity

# TODO update the JSON string below
json = "{}"
# create an instance of AddressCity from a JSON string
address_city_instance = AddressCity.from_json(json)
# print the JSON string representation of the object
print(AddressCity.to_json())

# convert the object into a dict
address_city_dict = address_city_instance.to_dict()
# create an instance of AddressCity from a dict
address_city_from_dict = AddressCity.from_dict(address_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


