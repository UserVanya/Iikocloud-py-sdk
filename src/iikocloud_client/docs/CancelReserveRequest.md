# CancelReserveRequest

Request for canceling the reservation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_reason** | [**ReserveCancelReason**](ReserveCancelReason.md) | Reason to cancel planned event. | 
**organization_id** | **UUID** | Organization ID of the reserve.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Reserve ID to cancel. | 

## Example

```python
from iikocloud_client.models.cancel_reserve_request import CancelReserveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelReserveRequest from a JSON string
cancel_reserve_request_instance = CancelReserveRequest.from_json(json)
# print the JSON string representation of the object
print(CancelReserveRequest.to_json())

# convert the object into a dict
cancel_reserve_request_dict = cancel_reserve_request_instance.to_dict()
# create an instance of CancelReserveRequest from a dict
cancel_reserve_request_from_dict = CancelReserveRequest.from_dict(cancel_reserve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


