# TransportReservesCancelReserveRequest

Request for canceling the reservation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID of the reserve.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_id** | **str** | Reserve ID to cancel. | 
**cancel_reason** | [**TransportReservesReserveCancelReason**](TransportReservesReserveCancelReason.md) | Reason to cancel planned event. | 

## Example

```python
from iiko_cloud_client.models.transport_reserves_cancel_reserve_request import TransportReservesCancelReserveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesCancelReserveRequest from a JSON string
transport_reserves_cancel_reserve_request_instance = TransportReservesCancelReserveRequest.from_json(json)
# print the JSON string representation of the object
print(TransportReservesCancelReserveRequest.to_json())

# convert the object into a dict
transport_reserves_cancel_reserve_request_dict = transport_reserves_cancel_reserve_request_instance.to_dict()
# create an instance of TransportReservesCancelReserveRequest from a dict
transport_reserves_cancel_reserve_request_from_dict = TransportReservesCancelReserveRequest.from_dict(transport_reserves_cancel_reserve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


