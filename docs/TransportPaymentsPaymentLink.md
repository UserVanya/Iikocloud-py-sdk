# TransportPaymentsPaymentLink

Payment link information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique key. | 
**integration_type** | **str** | Integration type code. | [optional] 
**status** | [**TransportPaymentsPaymentLinkStatus**](TransportPaymentsPaymentLinkStatus.md) | Payment link transport status. | 
**url** | **str** | Payload. | [optional] 
**updated_at** | **str** | Last update date (UTC). | 
**status_text** | **str** | Payment status (equals Payment link status if empty). | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_payments_payment_link import TransportPaymentsPaymentLink

# TODO update the JSON string below
json = "{}"
# create an instance of TransportPaymentsPaymentLink from a JSON string
transport_payments_payment_link_instance = TransportPaymentsPaymentLink.from_json(json)
# print the JSON string representation of the object
print(TransportPaymentsPaymentLink.to_json())

# convert the object into a dict
transport_payments_payment_link_dict = transport_payments_payment_link_instance.to_dict()
# create an instance of TransportPaymentsPaymentLink from a dict
transport_payments_payment_link_from_dict = TransportPaymentsPaymentLink.from_dict(transport_payments_payment_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


