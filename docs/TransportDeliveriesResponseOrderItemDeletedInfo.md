# TransportDeliveriesResponseOrderItemDeletedInfo

Order cancellation details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletion_method** | [**TransportDeliveriesResponseOrderDeletionMethod**](TransportDeliveriesResponseOrderDeletionMethod.md) | Deletion method. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_item_deleted_info import TransportDeliveriesResponseOrderItemDeletedInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderItemDeletedInfo from a JSON string
transport_deliveries_response_order_item_deleted_info_instance = TransportDeliveriesResponseOrderItemDeletedInfo.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderItemDeletedInfo.to_json())

# convert the object into a dict
transport_deliveries_response_order_item_deleted_info_dict = transport_deliveries_response_order_item_deleted_info_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderItemDeletedInfo from a dict
transport_deliveries_response_order_item_deleted_info_from_dict = TransportDeliveriesResponseOrderItemDeletedInfo.from_dict(transport_deliveries_response_order_item_deleted_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


