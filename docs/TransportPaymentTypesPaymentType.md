# TransportPaymentTypesPaymentType

DTO for payment type in iikoRMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Payment type ID | [optional] 
**code** | **str** | Payment type code | [optional] 
**name** | **str** | Payment type name | [optional] 
**comment** | **str** | Payment type comment | [optional] 
**combinable** | **bool** | Combinability attribute | [optional] 
**external_revision** | **int** | External system revision number. | [optional] 
**applicable_marketing_campaigns** | **List[str]** | Array of marketing campaigns associated with LoyaltyApp payment type applicable to this organization. | 
**is_deleted** | **bool** | IsDeleted attribute of payment type. | [optional] 
**print_cheque** | **bool** | If true, payment type is fiscal and bill will be printed. | [optional] 
**payment_processing_type** | [**TransportPaymentTypesPaymentProcessingType**](TransportPaymentTypesPaymentProcessingType.md) | Describes operation processing type. | [optional] 
**payment_type_kind** | [**TransportPaymentTypesPaymentTypeKind**](TransportPaymentTypesPaymentTypeKind.md) | Payment type category. | [optional] 
**terminal_groups** | [**List[TransportTerminalsTerminalGroup]**](TransportTerminalsTerminalGroup.md) | Terminal groups where this payment type is available. | 

## Example

```python
from iiko_cloud_client.models.transport_payment_types_payment_type import TransportPaymentTypesPaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of TransportPaymentTypesPaymentType from a JSON string
transport_payment_types_payment_type_instance = TransportPaymentTypesPaymentType.from_json(json)
# print the JSON string representation of the object
print(TransportPaymentTypesPaymentType.to_json())

# convert the object into a dict
transport_payment_types_payment_type_dict = transport_payment_types_payment_type_instance.to_dict()
# create an instance of TransportPaymentTypesPaymentType from a dict
transport_payment_types_payment_type_from_dict = TransportPaymentTypesPaymentType.from_dict(transport_payment_types_payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


