# IikoTransportPublicApiContractsErrorsErrorInfo

DTO for error details transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**IikoTransportPublicApiContractsErrorsErrorCode**](IikoTransportPublicApiContractsErrorsErrorCode.md) | Error code. | 
**message** | **str** | Localized message. | [optional] 
**description** | **str** | Localized message. | [optional] 
**additional_data** | **object** | Additional information. | [optional] 
**error_reason** | **str** | Error reason. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_errors_error_info import IikoTransportPublicApiContractsErrorsErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsErrorsErrorInfo from a JSON string
iiko_transport_public_api_contracts_errors_error_info_instance = IikoTransportPublicApiContractsErrorsErrorInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsErrorsErrorInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_errors_error_info_dict = iiko_transport_public_api_contracts_errors_error_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsErrorsErrorInfo from a dict
iiko_transport_public_api_contracts_errors_error_info_from_dict = IikoTransportPublicApiContractsErrorsErrorInfo.from_dict(iiko_transport_public_api_contracts_errors_error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


