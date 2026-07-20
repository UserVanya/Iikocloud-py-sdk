# PaymentAdditionalData

Additional payment data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from iikocloud_client.models.payment_additional_data import PaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAdditionalData from a JSON string
payment_additional_data_instance = PaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(PaymentAdditionalData.to_json())

# convert the object into a dict
payment_additional_data_dict = payment_additional_data_instance.to_dict()
# create an instance of PaymentAdditionalData from a dict
payment_additional_data_from_dict = PaymentAdditionalData.from_dict(payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


