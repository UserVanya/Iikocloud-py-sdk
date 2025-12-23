# AddressStreet

Street DTO in iikoRMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Name. | 
**external_revision** | **int** | External system revision No. | [optional] 
**classifier_id** | **str** | ID in classifier, e.g., address database. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | 

## Example

```python
from iikocloud_client.models.address_street import AddressStreet

# TODO update the JSON string below
json = "{}"
# create an instance of AddressStreet from a JSON string
address_street_instance = AddressStreet.from_json(json)
# print the JSON string representation of the object
print(AddressStreet.to_json())

# convert the object into a dict
address_street_dict = address_street_instance.to_dict()
# create an instance of AddressStreet from a dict
address_street_from_dict = AddressStreet.from_dict(address_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


