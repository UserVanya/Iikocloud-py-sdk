# DeliveriesResponseOrderDeletionMethod

Deletion method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**comment** | **str** | Comment. | [optional] 
**removal_type** | [**DeliveriesResponseOrderRemovalType**](DeliveriesResponseOrderRemovalType.md) | Write-off type. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_deletion_method import DeliveriesResponseOrderDeletionMethod

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderDeletionMethod from a JSON string
deliveries_response_order_deletion_method_instance = DeliveriesResponseOrderDeletionMethod.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderDeletionMethod.to_json())

# convert the object into a dict
deliveries_response_order_deletion_method_dict = deliveries_response_order_deletion_method_instance.to_dict()
# create an instance of DeliveriesResponseOrderDeletionMethod from a dict
deliveries_response_order_deletion_method_from_dict = DeliveriesResponseOrderDeletionMethod.from_dict(deliveries_response_order_deletion_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


