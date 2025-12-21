# PaymentTypesPaymentTypesRequest

Request for payment types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which payment types have to be returned.                 Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.payment_types_payment_types_request import PaymentTypesPaymentTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypesPaymentTypesRequest from a JSON string
payment_types_payment_types_request_instance = PaymentTypesPaymentTypesRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentTypesPaymentTypesRequest.to_json())

# convert the object into a dict
payment_types_payment_types_request_dict = payment_types_payment_types_request_instance.to_dict()
# create an instance of PaymentTypesPaymentTypesRequest from a dict
payment_types_payment_types_request_from_dict = PaymentTypesPaymentTypesRequest.from_dict(payment_types_payment_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


