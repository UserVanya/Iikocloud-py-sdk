# IikoTransportPublicApiContractsPaymentTypesPaymentType

DTO for payment type in iikoRMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Payment type ID | [optional] 
**code** | **str** | Payment type code | [optional] 
**name** | **str** | Payment type name | [optional] 
**comment** | **str** | Payment type comment | [optional] 
**combinable** | **bool** | Combinability attribute | [optional] 
**external_revision** | **int** | External system revision number. | [optional] 
**applicable_marketing_campaigns** | **List[UUID]** | Array of marketing campaigns associated with LoyaltyApp payment type applicable to this organization. | 
**is_deleted** | **bool** | IsDeleted attribute of payment type. | [optional] 
**print_cheque** | **bool** | If true, payment type is fiscal and bill will be printed. | [optional] 
**payment_processing_type** | [**IikoTransportPublicApiContractsPaymentTypesPaymentProcessingType**](IikoTransportPublicApiContractsPaymentTypesPaymentProcessingType.md) | Describes operation processing type. | [optional] 
**payment_type_kind** | [**IikoTransportPublicApiContractsPaymentTypesPaymentTypeKind**](IikoTransportPublicApiContractsPaymentTypesPaymentTypeKind.md) | Payment type category. | [optional] 
**terminal_groups** | [**List[IikoTransportPublicApiContractsTerminalsTerminalGroup]**](IikoTransportPublicApiContractsTerminalsTerminalGroup.md) | Terminal groups where this payment type is available. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_payment_types_payment_type import IikoTransportPublicApiContractsPaymentTypesPaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsPaymentTypesPaymentType from a JSON string
iiko_transport_public_api_contracts_payment_types_payment_type_instance = IikoTransportPublicApiContractsPaymentTypesPaymentType.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsPaymentTypesPaymentType.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_payment_types_payment_type_dict = iiko_transport_public_api_contracts_payment_types_payment_type_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsPaymentTypesPaymentType from a dict
iiko_transport_public_api_contracts_payment_types_payment_type_from_dict = IikoTransportPublicApiContractsPaymentTypesPaymentType.from_dict(iiko_transport_public_api_contracts_payment_types_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


