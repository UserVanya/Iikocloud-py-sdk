# DeliveriesResponseOrderItemDeletedInfo

Order cancellation details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletion_method** | [**DeliveriesResponseOrderDeletionMethod**](DeliveriesResponseOrderDeletionMethod.md) | Deletion method. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_item_deleted_info import DeliveriesResponseOrderItemDeletedInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderItemDeletedInfo from a JSON string
deliveries_response_order_item_deleted_info_instance = DeliveriesResponseOrderItemDeletedInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderItemDeletedInfo.to_json())

# convert the object into a dict
deliveries_response_order_item_deleted_info_dict = deliveries_response_order_item_deleted_info_instance.to_dict()
# create an instance of DeliveriesResponseOrderItemDeletedInfo from a dict
deliveries_response_order_item_deleted_info_from_dict = DeliveriesResponseOrderItemDeletedInfo.from_dict(deliveries_response_order_item_deleted_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


