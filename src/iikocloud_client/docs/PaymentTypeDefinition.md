# PaymentTypeDefinition

DTO for payment type in iikoRMS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_marketing_campaigns** | **List[UUID]** | Array of marketing campaigns associated with LoyaltyApp payment type applicable to this organization. | 
**code** | **str** | Payment type code | [optional] 
**combinable** | **bool** | Combinability attribute | [optional] 
**comment** | **str** | Payment type comment | [optional] 
**external_revision** | **int** | External system revision number. | [optional] 
**id** | **UUID** | Payment type ID | [optional] 
**is_deleted** | **bool** | IsDeleted attribute of payment type. | [optional] 
**name** | **str** | Payment type name | [optional] 
**payment_processing_type** | [**PaymentProcessingType**](PaymentProcessingType.md) | Describes operation processing type. | [optional] 
**payment_type_kind** | [**PaymentTypeKindDefinition**](PaymentTypeKindDefinition.md) | Payment type category. | [optional] 
**print_cheque** | **bool** | If true, payment type is fiscal and bill will be printed. | [optional] 
**terminal_groups** | [**List[TerminalGroup]**](TerminalGroup.md) | Terminal groups where this payment type is available. | 

## Example

```python
from iikocloud_client.models.payment_type_definition import PaymentTypeDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypeDefinition from a JSON string
payment_type_definition_instance = PaymentTypeDefinition.from_json(json)
# print the JSON string representation of the object
print(PaymentTypeDefinition.to_json())

# convert the object into a dict
payment_type_definition_dict = payment_type_definition_instance.to_dict()
# create an instance of PaymentTypeDefinition from a dict
payment_type_definition_from_dict = PaymentTypeDefinition.from_dict(payment_type_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


