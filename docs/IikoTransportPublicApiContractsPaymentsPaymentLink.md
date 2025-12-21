# IikoTransportPublicApiContractsPaymentsPaymentLink

Payment link information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique key. | 
**integration_type** | **str** | Integration type code. | [optional] 
**status** | [**IikoTransportPublicApiContractsPaymentsPaymentLinkStatus**](IikoTransportPublicApiContractsPaymentsPaymentLinkStatus.md) | Payment link transport status. | 
**url** | **str** | Payload. | [optional] 
**updated_at** | **str** | Last update date (UTC). | 
**status_text** | **str** | Payment status (equals Payment link status if empty). | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_payments_payment_link import IikoTransportPublicApiContractsPaymentsPaymentLink

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsPaymentsPaymentLink from a JSON string
iiko_transport_public_api_contracts_payments_payment_link_instance = IikoTransportPublicApiContractsPaymentsPaymentLink.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsPaymentsPaymentLink.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_payments_payment_link_dict = iiko_transport_public_api_contracts_payments_payment_link_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsPaymentsPaymentLink from a dict
iiko_transport_public_api_contracts_payments_payment_link_from_dict = IikoTransportPublicApiContractsPaymentsPaymentLink.from_dict(iiko_transport_public_api_contracts_payments_payment_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


