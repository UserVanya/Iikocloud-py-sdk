# StreetsByIdRequest

Organization and city request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classifier_ids** | **List[str]** | Street classifierIds. | [optional] 
**ids** | **List[UUID]** | Street Ids. | [optional] 
**organization_id** | **UUID** | Organization Id. | 

## Example

```python
from iikocloud_client.models.streets_by_id_request import StreetsByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreetsByIdRequest from a JSON string
streets_by_id_request_instance = StreetsByIdRequest.from_json(json)
# print the JSON string representation of the object
print(StreetsByIdRequest.to_json())

# convert the object into a dict
streets_by_id_request_dict = streets_by_id_request_instance.to_dict()
# create an instance of StreetsByIdRequest from a dict
streets_by_id_request_from_dict = StreetsByIdRequest.from_dict(streets_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


