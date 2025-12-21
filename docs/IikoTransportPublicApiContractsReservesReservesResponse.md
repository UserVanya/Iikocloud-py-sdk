# IikoTransportPublicApiContractsReservesReservesResponse

Wrapping object (external) for return of banquets/reserves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**reserves** | [**List[IikoTransportPublicApiContractsReservesReserveInfo]**](IikoTransportPublicApiContractsReservesReserveInfo.md) | Banquets/reserves. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_reserves_response import IikoTransportPublicApiContractsReservesReservesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesReservesResponse from a JSON string
iiko_transport_public_api_contracts_reserves_reserves_response_instance = IikoTransportPublicApiContractsReservesReservesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesReservesResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_reserves_response_dict = iiko_transport_public_api_contracts_reserves_reserves_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesReservesResponse from a dict
iiko_transport_public_api_contracts_reserves_reserves_response_from_dict = IikoTransportPublicApiContractsReservesReservesResponse.from_dict(iiko_transport_public_api_contracts_reserves_reserves_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


