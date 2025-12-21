# IikoTransportPublicApiContractsStopListsStopListsResponse

Status of out-of-stock lists for a specified organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**terminal_group_stop_lists** | [**List[RmsItemsResponseWrapperStopListsTerminalGroupStopList]**](RmsItemsResponseWrapperStopListsTerminalGroupStopList.md) | Set of out-of-stock lists | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_stop_lists_response import IikoTransportPublicApiContractsStopListsStopListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsStopListsResponse from a JSON string
iiko_transport_public_api_contracts_stop_lists_stop_lists_response_instance = IikoTransportPublicApiContractsStopListsStopListsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsStopListsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_stop_lists_response_dict = iiko_transport_public_api_contracts_stop_lists_stop_lists_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsStopListsResponse from a dict
iiko_transport_public_api_contracts_stop_lists_stop_lists_response_from_dict = IikoTransportPublicApiContractsStopListsStopListsResponse.from_dict(iiko_transport_public_api_contracts_stop_lists_stop_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


