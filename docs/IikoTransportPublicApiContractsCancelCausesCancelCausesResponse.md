# IikoTransportPublicApiContractsCancelCausesCancelCausesResponse

Response with delivery cancel causes (reasons for deletion) list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**cancel_causes** | [**List[IikoTransportPublicApiContractsCancelCausesCancelCause]**](IikoTransportPublicApiContractsCancelCausesCancelCause.md) | List of delivery cancel causes. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_cancel_causes_cancel_causes_response import IikoTransportPublicApiContractsCancelCausesCancelCausesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsCancelCausesCancelCausesResponse from a JSON string
iiko_transport_public_api_contracts_cancel_causes_cancel_causes_response_instance = IikoTransportPublicApiContractsCancelCausesCancelCausesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsCancelCausesCancelCausesResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_cancel_causes_cancel_causes_response_dict = iiko_transport_public_api_contracts_cancel_causes_cancel_causes_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsCancelCausesCancelCausesResponse from a dict
iiko_transport_public_api_contracts_cancel_causes_cancel_causes_response_from_dict = IikoTransportPublicApiContractsCancelCausesCancelCausesResponse.from_dict(iiko_transport_public_api_contracts_cancel_causes_cancel_causes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


