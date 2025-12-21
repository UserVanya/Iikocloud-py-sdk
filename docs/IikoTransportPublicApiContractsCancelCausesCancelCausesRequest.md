# IikoTransportPublicApiContractsCancelCausesCancelCausesRequest

Request for organization's delivery cancel causes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations ids which delivery cancel causes needs to be returned.                 Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request import IikoTransportPublicApiContractsCancelCausesCancelCausesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsCancelCausesCancelCausesRequest from a JSON string
iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request_instance = IikoTransportPublicApiContractsCancelCausesCancelCausesRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsCancelCausesCancelCausesRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request_dict = iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsCancelCausesCancelCausesRequest from a dict
iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request_from_dict = IikoTransportPublicApiContractsCancelCausesCancelCausesRequest.from_dict(iiko_transport_public_api_contracts_cancel_causes_cancel_causes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


