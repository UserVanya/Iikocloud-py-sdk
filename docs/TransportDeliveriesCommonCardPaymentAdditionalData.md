# TransportDeliveriesCommonCardPaymentAdditionalData

Additional data for Card payment item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_data** | **str** | Custom data.  &gt; If this property is set, the above &#x60;number&#x60; property is ignored.   &gt; Allowed from version &#x60;8.8.6&#x60;. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_common_card_payment_additional_data import TransportDeliveriesCommonCardPaymentAdditionalData

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesCommonCardPaymentAdditionalData from a JSON string
transport_deliveries_common_card_payment_additional_data_instance = TransportDeliveriesCommonCardPaymentAdditionalData.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesCommonCardPaymentAdditionalData.to_json())

# convert the object into a dict
transport_deliveries_common_card_payment_additional_data_dict = transport_deliveries_common_card_payment_additional_data_instance.to_dict()
# create an instance of TransportDeliveriesCommonCardPaymentAdditionalData from a dict
transport_deliveries_common_card_payment_additional_data_from_dict = TransportDeliveriesCommonCardPaymentAdditionalData.from_dict(transport_deliveries_common_card_payment_additional_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


