# DeliveriesCommonPaymentAdditionalData

Additional payment data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from iikocloud_client.models.deliveries_common_payment_additional_data import DeliveriesCommonPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesCommonPaymentAdditionalData from a JSON string
deliveries_common_payment_additional_data_instance = DeliveriesCommonPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(DeliveriesCommonPaymentAdditionalData.to_json())

# convert the object into a dict
deliveries_common_payment_additional_data_dict = deliveries_common_payment_additional_data_instance.to_dict()
# create an instance of DeliveriesCommonPaymentAdditionalData from a dict
deliveries_common_payment_additional_data_from_dict = DeliveriesCommonPaymentAdditionalData.from_dict(deliveries_common_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


