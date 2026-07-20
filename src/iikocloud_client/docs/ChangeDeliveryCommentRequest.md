# ChangeDeliveryCommentRequest

Request for change delivery comment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | New delivery comment. | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID. | 

## Example

```python
from iikocloud_client.models.change_delivery_comment_request import ChangeDeliveryCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeDeliveryCommentRequest from a JSON string
change_delivery_comment_request_instance = ChangeDeliveryCommentRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeDeliveryCommentRequest.to_json())

# convert the object into a dict
change_delivery_comment_request_dict = change_delivery_comment_request_instance.to_dict()
# create an instance of ChangeDeliveryCommentRequest from a dict
change_delivery_comment_request_from_dict = ChangeDeliveryCommentRequest.from_dict(change_delivery_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


