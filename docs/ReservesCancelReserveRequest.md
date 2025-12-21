# ReservesCancelReserveRequest

Request for canceling the reservation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID of the reserve.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Reserve ID to cancel. | 
**cancel_reason** | [**ReservesReserveCancelReason**](ReservesReserveCancelReason.md) | Reason to cancel planned event. | 

## Example

```python
from iikocloud_client.models.reserves_cancel_reserve_request import ReservesCancelReserveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesCancelReserveRequest from a JSON string
reserves_cancel_reserve_request_instance = ReservesCancelReserveRequest.from_json(json)
# print the JSON string representation of the object
print(ReservesCancelReserveRequest.to_json())

# convert the object into a dict
reserves_cancel_reserve_request_dict = reserves_cancel_reserve_request_instance.to_dict()
# create an instance of ReservesCancelReserveRequest from a dict
reserves_cancel_reserve_request_from_dict = ReservesCancelReserveRequest.from_dict(reserves_cancel_reserve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


