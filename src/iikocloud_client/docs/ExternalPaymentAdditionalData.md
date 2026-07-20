# ExternalPaymentAdditionalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data** | **str** | Payment custom data. | 

## Example

```python
from iikocloud_client.models.external_payment_additional_data import ExternalPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalPaymentAdditionalData from a JSON string
external_payment_additional_data_instance = ExternalPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(ExternalPaymentAdditionalData.to_json())

# convert the object into a dict
external_payment_additional_data_dict = external_payment_additional_data_instance.to_dict()
# create an instance of ExternalPaymentAdditionalData from a dict
external_payment_additional_data_from_dict = ExternalPaymentAdditionalData.from_dict(external_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


