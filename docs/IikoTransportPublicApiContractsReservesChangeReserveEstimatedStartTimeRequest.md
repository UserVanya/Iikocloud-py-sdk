# IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest

Request to change reserve/banquet estimated start time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**reserve_id** | **UUID** | Reserve/banquet ID. | 
**new_estimated_start_time** | **str** | New estimated start time of reserve/banquet. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request import IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest from a JSON string
iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request_instance = IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request_dict = iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest from a dict
iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request_from_dict = IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest.from_dict(iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


