# IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse

Response to request for payment types by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**payment_types** | [**List[IikoTransportPublicApiContractsPaymentTypesPaymentType]**](IikoTransportPublicApiContractsPaymentTypesPaymentType.md) | List of payment types and terminal groups where they are available. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_payment_types_payment_types_response import IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse from a JSON string
iiko_transport_public_api_contracts_payment_types_payment_types_response_instance = IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_payment_types_payment_types_response_dict = iiko_transport_public_api_contracts_payment_types_payment_types_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse from a dict
iiko_transport_public_api_contracts_payment_types_payment_types_response_from_dict = IikoTransportPublicApiContractsPaymentTypesPaymentTypesResponse.from_dict(iiko_transport_public_api_contracts_payment_types_payment_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


