# PaymentTypesPaymentTypesResponse

Response to request for payment types by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**payment_types** | [**List[PaymentTypesPaymentType]**](PaymentTypesPaymentType.md) | List of payment types and terminal groups where they are available. | 

## Example

```python
from iikocloud_client.models.payment_types_payment_types_response import PaymentTypesPaymentTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypesPaymentTypesResponse from a JSON string
payment_types_payment_types_response_instance = PaymentTypesPaymentTypesResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentTypesPaymentTypesResponse.to_json())

# convert the object into a dict
payment_types_payment_types_response_dict = payment_types_payment_types_response_instance.to_dict()
# create an instance of PaymentTypesPaymentTypesResponse from a dict
payment_types_payment_types_response_from_dict = PaymentTypesPaymentTypesResponse.from_dict(payment_types_payment_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


