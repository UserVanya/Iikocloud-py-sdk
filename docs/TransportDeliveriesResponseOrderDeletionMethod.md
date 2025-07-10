# TransportDeliveriesResponseOrderDeletionMethod

Deletion method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**comment** | **str** | Comment. | [optional] 
**removal_type** | [**TransportDeliveriesResponseOrderRemovalType**](TransportDeliveriesResponseOrderRemovalType.md) | Write-off type. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_deletion_method import TransportDeliveriesResponseOrderDeletionMethod

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderDeletionMethod from a JSON string
transport_deliveries_response_order_deletion_method_instance = TransportDeliveriesResponseOrderDeletionMethod.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderDeletionMethod.to_json())

# convert the object into a dict
transport_deliveries_response_order_deletion_method_dict = transport_deliveries_response_order_deletion_method_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderDeletionMethod from a dict
transport_deliveries_response_order_deletion_method_from_dict = TransportDeliveriesResponseOrderDeletionMethod.from_dict(transport_deliveries_response_order_deletion_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


