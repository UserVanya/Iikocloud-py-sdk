# IikoTransportPublicApiContractsStopListsClearStopListRequest

Request to clear out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request import IikoTransportPublicApiContractsStopListsClearStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsClearStopListRequest from a JSON string
iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request_instance = IikoTransportPublicApiContractsStopListsClearStopListRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsClearStopListRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request_dict = iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsClearStopListRequest from a dict
iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request_from_dict = IikoTransportPublicApiContractsStopListsClearStopListRequest.from_dict(iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


