# DeliveryAttentionNotificationRequest

Request to notify external systems (iikoFront and iikoWeb) about a delivery requiring attention.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | Additional info about the problem. | 
**order_id** | **UUID** | Order ID. | 
**order_source** | **str** | Order source. | 
**organization_id** | **UUID** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.delivery_attention_notification_request import DeliveryAttentionNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryAttentionNotificationRequest from a JSON string
delivery_attention_notification_request_instance = DeliveryAttentionNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveryAttentionNotificationRequest.to_json())

# convert the object into a dict
delivery_attention_notification_request_dict = delivery_attention_notification_request_instance.to_dict()
# create an instance of DeliveryAttentionNotificationRequest from a dict
delivery_attention_notification_request_from_dict = DeliveryAttentionNotificationRequest.from_dict(delivery_attention_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


