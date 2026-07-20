# ChangeDeliveryPointRequest

Request for change order's delivery point information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_delivery_point** | [**DeliveryOrderCreatePoint**](DeliveryOrderCreatePoint.md) | New address of delivery. | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.change_delivery_point_request import ChangeDeliveryPointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeDeliveryPointRequest from a JSON string
change_delivery_point_request_instance = ChangeDeliveryPointRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeDeliveryPointRequest.to_json())

# convert the object into a dict
change_delivery_point_request_dict = change_delivery_point_request_instance.to_dict()
# create an instance of ChangeDeliveryPointRequest from a dict
change_delivery_point_request_from_dict = ChangeDeliveryPointRequest.from_dict(change_delivery_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


