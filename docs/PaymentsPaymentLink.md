# PaymentsPaymentLink

Payment link information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique key. | 
**integration_type** | **str** | Integration type code. | [optional] 
**status** | [**PaymentsPaymentLinkStatus**](PaymentsPaymentLinkStatus.md) | Payment link transport status. | 
**url** | **str** | Payload. | [optional] 
**updated_at** | **str** | Last update date (UTC). | 
**status_text** | **str** | Payment status (equals Payment link status if empty). | [optional] 

## Example

```python
from iikocloud_client.models.payments_payment_link import PaymentsPaymentLink

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentsPaymentLink from a JSON string
payments_payment_link_instance = PaymentsPaymentLink.from_json(json)
# print the JSON string representation of the object
print(PaymentsPaymentLink.to_json())

# convert the object into a dict
payments_payment_link_dict = payments_payment_link_instance.to_dict()
# create an instance of PaymentsPaymentLink from a dict
payments_payment_link_from_dict = PaymentsPaymentLink.from_dict(payments_payment_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


