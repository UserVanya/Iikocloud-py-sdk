# DeliveriesCommonExternalPaymentAdditionalData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data** | **str** | Payment custom data. | 

## Example

```python
from iikocloud_client.models.deliveries_common_external_payment_additional_data import DeliveriesCommonExternalPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesCommonExternalPaymentAdditionalData from a JSON string
deliveries_common_external_payment_additional_data_instance = DeliveriesCommonExternalPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(DeliveriesCommonExternalPaymentAdditionalData.to_json())

# convert the object into a dict
deliveries_common_external_payment_additional_data_dict = deliveries_common_external_payment_additional_data_instance.to_dict()
# create an instance of DeliveriesCommonExternalPaymentAdditionalData from a dict
deliveries_common_external_payment_additional_data_from_dict = DeliveriesCommonExternalPaymentAdditionalData.from_dict(deliveries_common_external_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


