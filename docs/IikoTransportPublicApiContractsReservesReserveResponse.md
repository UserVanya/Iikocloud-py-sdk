# IikoTransportPublicApiContractsReservesReserveResponse

Wrapping object (external) for return of banquets/reserves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**reserve_info** | [**IikoTransportPublicApiContractsReservesReserveInfo**](IikoTransportPublicApiContractsReservesReserveInfo.md) | Banquet/reserve. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_reserve_response import IikoTransportPublicApiContractsReservesReserveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesReserveResponse from a JSON string
iiko_transport_public_api_contracts_reserves_reserve_response_instance = IikoTransportPublicApiContractsReservesReserveResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesReserveResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_reserve_response_dict = iiko_transport_public_api_contracts_reserves_reserve_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesReserveResponse from a dict
iiko_transport_public_api_contracts_reserves_reserve_response_from_dict = IikoTransportPublicApiContractsReservesReserveResponse.from_dict(iiko_transport_public_api_contracts_reserves_reserve_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


