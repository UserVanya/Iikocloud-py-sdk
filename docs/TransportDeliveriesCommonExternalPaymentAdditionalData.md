# TransportDeliveriesCommonExternalPaymentAdditionalData

Additional data for external payment item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data** | **str** | Payment custom data. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_common_external_payment_additional_data import TransportDeliveriesCommonExternalPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesCommonExternalPaymentAdditionalData from a JSON string
transport_deliveries_common_external_payment_additional_data_instance = TransportDeliveriesCommonExternalPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesCommonExternalPaymentAdditionalData.to_json())

# convert the object into a dict
transport_deliveries_common_external_payment_additional_data_dict = transport_deliveries_common_external_payment_additional_data_instance.to_dict()
# create an instance of TransportDeliveriesCommonExternalPaymentAdditionalData from a dict
transport_deliveries_common_external_payment_additional_data_from_dict = TransportDeliveriesCommonExternalPaymentAdditionalData.from_dict(transport_deliveries_common_external_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


