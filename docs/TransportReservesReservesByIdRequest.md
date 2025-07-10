# TransportReservesReservesByIdRequest

Request for information about banquets/reserves using IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_ids** | **List[str]** | IDs of banquets/reserves information on which is required. | 
**source_keys** | **List[str]** | Source keys. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_reserves_reserves_by_id_request import TransportReservesReservesByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesReservesByIdRequest from a JSON string
transport_reserves_reserves_by_id_request_instance = TransportReservesReservesByIdRequest.from_json(json)
# print the JSON string representation of the object
print(TransportReservesReservesByIdRequest.to_json())

# convert the object into a dict
transport_reserves_reserves_by_id_request_dict = transport_reserves_reserves_by_id_request_instance.to_dict()
# create an instance of TransportReservesReservesByIdRequest from a dict
transport_reserves_reserves_by_id_request_from_dict = TransportReservesReservesByIdRequest.from_dict(transport_reserves_reserves_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


