# IikoTransportPublicApiContractsStopListsCheckStopListResponse

Response for check items in out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**rejected_items** | [**List[IikoTransportPublicApiContractsStopListsStopListItem]**](IikoTransportPublicApiContractsStopListsStopListItem.md) | Set of items in out-of-stock list.                If null, none of requested items are in out-of-stock list.  &gt; Present in response only if **not null**. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_check_stop_list_response import IikoTransportPublicApiContractsStopListsCheckStopListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsCheckStopListResponse from a JSON string
iiko_transport_public_api_contracts_stop_lists_check_stop_list_response_instance = IikoTransportPublicApiContractsStopListsCheckStopListResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsCheckStopListResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_check_stop_list_response_dict = iiko_transport_public_api_contracts_stop_lists_check_stop_list_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsCheckStopListResponse from a dict
iiko_transport_public_api_contracts_stop_lists_check_stop_list_response_from_dict = IikoTransportPublicApiContractsStopListsCheckStopListResponse.from_dict(iiko_transport_public_api_contracts_stop_lists_check_stop_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


