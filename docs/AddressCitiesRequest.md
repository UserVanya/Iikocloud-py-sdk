# AddressCitiesRequest

Organization request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | IDs of organizations that require data return.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**include_deleted** | **bool** | Include deleted cities in response. | [optional] 

## Example

```python
from iikocloud_client.models.address_cities_request import AddressCitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressCitiesRequest from a JSON string
address_cities_request_instance = AddressCitiesRequest.from_json(json)
# print the JSON string representation of the object
print(AddressCitiesRequest.to_json())

# convert the object into a dict
address_cities_request_dict = address_cities_request_instance.to_dict()
# create an instance of AddressCitiesRequest from a dict
address_cities_request_from_dict = AddressCitiesRequest.from_dict(address_cities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


