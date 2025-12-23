# ReservesReservesByIdRequest

Request for information about banquets/reserves using IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_ids** | **List[str]** | IDs of banquets/reserves information on which is required. | 
**source_keys** | **List[str]** | Source keys. | [optional] 

## Example

```python
from iikocloud_client.models.reserves_reserves_by_id_request import ReservesReservesByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesReservesByIdRequest from a JSON string
reserves_reserves_by_id_request_instance = ReservesReservesByIdRequest.from_json(json)
# print the JSON string representation of the object
print(ReservesReservesByIdRequest.to_json())

# convert the object into a dict
reserves_reserves_by_id_request_dict = reserves_reserves_by_id_request_instance.to_dict()
# create an instance of ReservesReservesByIdRequest from a dict
reserves_reserves_by_id_request_from_dict = ReservesReservesByIdRequest.from_dict(reserves_reserves_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


