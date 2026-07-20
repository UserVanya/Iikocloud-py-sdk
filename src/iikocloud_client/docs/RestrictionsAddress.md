# RestrictionsAddress

Address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building** | **str** | Building. | [optional] 
**city** | **str** | City. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**house** | **str** | House. | [optional] 
**index** | **str** | Post index. | [optional] 
**line1** | **str** | Address line 1.  Contains the primary address information. | [optional] 
**street_id** | **UUID** | Street ID. | [optional] 
**street_name** | **str** | Street. | [optional] 

## Example

```python
from iikocloud_client.models.restrictions_address import RestrictionsAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictionsAddress from a JSON string
restrictions_address_instance = RestrictionsAddress.from_json(json)
# print the JSON string representation of the object
print(RestrictionsAddress.to_json())

# convert the object into a dict
restrictions_address_dict = restrictions_address_instance.to_dict()
# create an instance of RestrictionsAddress from a dict
restrictions_address_from_dict = RestrictionsAddress.from_dict(restrictions_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


