# ConfirmDeliveryRequest

Request for confirm delivery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.confirm_delivery_request import ConfirmDeliveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmDeliveryRequest from a JSON string
confirm_delivery_request_instance = ConfirmDeliveryRequest.from_json(json)
# print the JSON string representation of the object
print(ConfirmDeliveryRequest.to_json())

# convert the object into a dict
confirm_delivery_request_dict = confirm_delivery_request_instance.to_dict()
# create an instance of ConfirmDeliveryRequest from a dict
confirm_delivery_request_from_dict = ConfirmDeliveryRequest.from_dict(confirm_delivery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


