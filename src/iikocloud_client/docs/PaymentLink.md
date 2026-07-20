# PaymentLink

Payment link information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique key. | 
**integration_type** | **str** | Integration type code. | [optional] 
**status** | [**PaymentLinkStatus**](PaymentLinkStatus.md) | Payment link transport status. | 
**status_text** | **str** | Payment status (equals Payment link status if empty). | [optional] 
**updated_at** | **str** | Last update date (UTC). | 
**url** | **str** | Payload. | [optional] 

## Example

```python
from iikocloud_client.models.payment_link import PaymentLink

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentLink from a JSON string
payment_link_instance = PaymentLink.from_json(json)
# print the JSON string representation of the object
print(PaymentLink.to_json())

# convert the object into a dict
payment_link_dict = payment_link_instance.to_dict()
# create an instance of PaymentLink from a dict
payment_link_from_dict = PaymentLink.from_dict(payment_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


