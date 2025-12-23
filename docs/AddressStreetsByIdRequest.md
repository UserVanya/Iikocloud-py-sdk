# AddressStreetsByIdRequest

Organization and city request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization Id. | 
**ids** | **List[str]** | Street Ids. | [optional] 
**classifier_ids** | **List[str]** | Street classifierIds. | [optional] 

## Example

```python
from iikocloud_client.models.address_streets_by_id_request import AddressStreetsByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressStreetsByIdRequest from a JSON string
address_streets_by_id_request_instance = AddressStreetsByIdRequest.from_json(json)
# print the JSON string representation of the object
print(AddressStreetsByIdRequest.to_json())

# convert the object into a dict
address_streets_by_id_request_dict = address_streets_by_id_request_instance.to_dict()
# create an instance of AddressStreetsByIdRequest from a dict
address_streets_by_id_request_from_dict = AddressStreetsByIdRequest.from_dict(address_streets_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


