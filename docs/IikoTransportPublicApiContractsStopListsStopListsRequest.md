# IikoTransportPublicApiContractsStopListsStopListsRequest

DTO of out-of-stock lists request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations for which out-of-stock lists will be requested.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**return_size** | **bool** | Flag indicating the need to return the sizes of the dish. | [optional] 
**terminal_groups_ids** | **List[UUID]** | List of terminal groups for which you need to get out-of-stock lists.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_stop_lists_request import IikoTransportPublicApiContractsStopListsStopListsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsStopListsRequest from a JSON string
iiko_transport_public_api_contracts_stop_lists_stop_lists_request_instance = IikoTransportPublicApiContractsStopListsStopListsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsStopListsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_stop_lists_request_dict = iiko_transport_public_api_contracts_stop_lists_stop_lists_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsStopListsRequest from a dict
iiko_transport_public_api_contracts_stop_lists_stop_lists_request_from_dict = IikoTransportPublicApiContractsStopListsStopListsRequest.from_dict(iiko_transport_public_api_contracts_stop_lists_stop_lists_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


