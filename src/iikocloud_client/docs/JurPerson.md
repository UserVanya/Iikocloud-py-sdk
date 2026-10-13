# JurPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[Organization]**](Organization.md) | Child organizations with the same recursive structure; an empty array is returned for a leaf node | [optional] 
**code** | **str** | User-defined legal entity code; null if the code is not set | [optional] 
**jur_person_id** | **str** | Legal entity identifier | [optional] 
**legal_address** | [**LegalAddress**](LegalAddress.md) | Legal address of the legal entity; null if not provided by the source | [optional] 
**name** | **str** | Display name of the legal entity; null if the name is not provided by the source | [optional] 
**responsible_persons** | [**List[ResponsiblePerson]**](ResponsiblePerson.md) | Responsible persons of the legal entity; an empty array if not provided by the source | [optional] 
**taxpayer_id_number** | **str** | Taxpayer identification number (INN) of the legal entity; null if not provided by the source | [optional] 
**type** | **str** | Legal entity node type. Always takes the value JURPERSON | [optional] 

## Example

```python
from iikocloud_client.models.jur_person import JurPerson

# TODO update the JSON string below
json = "{}"
# create an instance of JurPerson from a JSON string
jur_person_instance = JurPerson.from_json(json)
# print the JSON string representation of the object
print(JurPerson.to_json())

# convert the object into a dict
jur_person_dict = jur_person_instance.to_dict()
# create an instance of JurPerson from a dict
jur_person_from_dict = JurPerson.from_dict(jur_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


