# PaymentDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**other_payments_sum** | **float** | Other payments/penalties | [optional] 
**overtime_paid_minutes** | **int** | Overtime paid minutes | [optional] 
**overtime_payment_sum** | **float** | Overtime payment sum | [optional] 
**regular_paid_minutes** | **int** | Regular paid minutes | [optional] 
**regular_payment_sum** | **float** | Regular payment sum | [optional] 

## Example

```python
from iikocloud_client.models.payment_details import PaymentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDetails from a JSON string
payment_details_instance = PaymentDetails.from_json(json)
# print the JSON string representation of the object
print(PaymentDetails.to_json())

# convert the object into a dict
payment_details_dict = payment_details_instance.to_dict()
# create an instance of PaymentDetails from a dict
payment_details_from_dict = PaymentDetails.from_dict(payment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


