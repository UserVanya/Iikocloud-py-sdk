# IikoTransportPublicApiContractsErrorsErrorResponse

Error response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**error_description** | **str** | Error text. | 
**error** | **str** | Error code. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_errors_error_response import IikoTransportPublicApiContractsErrorsErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsErrorsErrorResponse from a JSON string
iiko_transport_public_api_contracts_errors_error_response_instance = IikoTransportPublicApiContractsErrorsErrorResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsErrorsErrorResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_errors_error_response_dict = iiko_transport_public_api_contracts_errors_error_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsErrorsErrorResponse from a dict
iiko_transport_public_api_contracts_errors_error_response_from_dict = IikoTransportPublicApiContractsErrorsErrorResponse.from_dict(iiko_transport_public_api_contracts_errors_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


