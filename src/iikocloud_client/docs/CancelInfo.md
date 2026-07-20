# CancelInfo

Order cancellation details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cause** | [**DeliveryOrderResponseCancelCause**](DeliveryOrderResponseCancelCause.md) | Delivery cancellation reason. | 
**comment** | **str** | Delivery cancellation comment. | [optional] 
**when_cancelled** | **str** | Cancellation time (Local for delivery terminal). | 

## Example

```python
from iikocloud_client.models.cancel_info import CancelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CancelInfo from a JSON string
cancel_info_instance = CancelInfo.from_json(json)
# print the JSON string representation of the object
print(CancelInfo.to_json())

# convert the object into a dict
cancel_info_dict = cancel_info_instance.to_dict()
# create an instance of CancelInfo from a dict
cancel_info_from_dict = CancelInfo.from_dict(cancel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


