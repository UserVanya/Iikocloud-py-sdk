# UpdateTrackingLinkRequest

Request to update tracking link of a delivery order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Delivery order id. | 
**organization_id** | **UUID** | OrganizationId. | 
**tracking_link** | **str** | Tracking link of a delivery order. | [optional] 

## Example

```python
from iikocloud_client.models.update_tracking_link_request import UpdateTrackingLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTrackingLinkRequest from a JSON string
update_tracking_link_request_instance = UpdateTrackingLinkRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTrackingLinkRequest.to_json())

# convert the object into a dict
update_tracking_link_request_dict = update_tracking_link_request_instance.to_dict()
# create an instance of UpdateTrackingLinkRequest from a dict
update_tracking_link_request_from_dict = UpdateTrackingLinkRequest.from_dict(update_tracking_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


