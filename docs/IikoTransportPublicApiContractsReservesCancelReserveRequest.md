# IikoTransportPublicApiContractsReservesCancelReserveRequest

Request for canceling the reservation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID of the reserve.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Reserve ID to cancel. | 
**cancel_reason** | [**IikoTransportPublicApiContractsReservesReserveCancelReason**](IikoTransportPublicApiContractsReservesReserveCancelReason.md) | Reason to cancel planned event. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_cancel_reserve_request import IikoTransportPublicApiContractsReservesCancelReserveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesCancelReserveRequest from a JSON string
iiko_transport_public_api_contracts_reserves_cancel_reserve_request_instance = IikoTransportPublicApiContractsReservesCancelReserveRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesCancelReserveRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_cancel_reserve_request_dict = iiko_transport_public_api_contracts_reserves_cancel_reserve_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesCancelReserveRequest from a dict
iiko_transport_public_api_contracts_reserves_cancel_reserve_request_from_dict = IikoTransportPublicApiContractsReservesCancelReserveRequest.from_dict(iiko_transport_public_api_contracts_reserves_cancel_reserve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


