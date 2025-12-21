# IikoTransportPublicApiContractsReservesReservesByIdRequest

Request for information about banquets/reserves using IDs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID for which an order search will be performed.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**reserve_ids** | **List[UUID]** | IDs of banquets/reserves information on which is required. | 
**source_keys** | **List[str]** | Source keys. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_reserves_by_id_request import IikoTransportPublicApiContractsReservesReservesByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesReservesByIdRequest from a JSON string
iiko_transport_public_api_contracts_reserves_reserves_by_id_request_instance = IikoTransportPublicApiContractsReservesReservesByIdRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesReservesByIdRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_reserves_by_id_request_dict = iiko_transport_public_api_contracts_reserves_reserves_by_id_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesReservesByIdRequest from a dict
iiko_transport_public_api_contracts_reserves_reserves_by_id_request_from_dict = IikoTransportPublicApiContractsReservesReservesByIdRequest.from_dict(iiko_transport_public_api_contracts_reserves_reserves_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


