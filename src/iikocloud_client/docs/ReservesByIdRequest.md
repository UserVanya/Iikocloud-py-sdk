# ReservesByIdRequest

Request for information about banquets/reserves using IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_ids** | **List[UUID]** | IDs of banquets/reserves information on which is required. | 
**source_keys** | **List[str]** | Source keys. | [optional] 

## Example

```python
from iikocloud_client.models.reserves_by_id_request import ReservesByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesByIdRequest from a JSON string
reserves_by_id_request_instance = ReservesByIdRequest.from_json(json)
# print the JSON string representation of the object
print(ReservesByIdRequest.to_json())

# convert the object into a dict
reserves_by_id_request_dict = reserves_by_id_request_instance.to_dict()
# create an instance of ReservesByIdRequest from a dict
reserves_by_id_request_from_dict = ReservesByIdRequest.from_dict(reserves_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


