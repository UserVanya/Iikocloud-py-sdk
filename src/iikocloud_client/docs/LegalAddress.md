# LegalAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Legal address as a single string provided by the source; null if not provided | [optional] 
**building** | **str** | Building; null if not provided | [optional] 
**city** | **str** | City; null if not provided | [optional] 
**community** | **str** | Community; null if not provided | [optional] 
**country** | **str** | Country; null if not provided | [optional] 
**district** | **str** | District; null if not provided | [optional] 
**house** | **str** | House; null if not provided | [optional] 
**office** | **str** | Office; null if not provided | [optional] 
**region** | **str** | Region; null if not provided | [optional] 
**street** | **str** | Street; null if not provided | [optional] 
**zip_code** | **str** | Postal code; null if not provided | [optional] 

## Example

```python
from iikocloud_client.models.legal_address import LegalAddress

# TODO update the JSON string below
json = "{}"
# create an instance of LegalAddress from a JSON string
legal_address_instance = LegalAddress.from_json(json)
# print the JSON string representation of the object
print(LegalAddress.to_json())

# convert the object into a dict
legal_address_dict = legal_address_instance.to_dict()
# create an instance of LegalAddress from a dict
legal_address_from_dict = LegalAddress.from_dict(legal_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


