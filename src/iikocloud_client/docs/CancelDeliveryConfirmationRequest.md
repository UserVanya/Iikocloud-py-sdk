# CancelDeliveryConfirmationRequest

Request for cancel delivery confirmation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.cancel_delivery_confirmation_request import CancelDeliveryConfirmationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelDeliveryConfirmationRequest from a JSON string
cancel_delivery_confirmation_request_instance = CancelDeliveryConfirmationRequest.from_json(json)
# print the JSON string representation of the object
print(CancelDeliveryConfirmationRequest.to_json())

# convert the object into a dict
cancel_delivery_confirmation_request_dict = cancel_delivery_confirmation_request_instance.to_dict()
# create an instance of CancelDeliveryConfirmationRequest from a dict
cancel_delivery_confirmation_request_from_dict = CancelDeliveryConfirmationRequest.from_dict(cancel_delivery_confirmation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


