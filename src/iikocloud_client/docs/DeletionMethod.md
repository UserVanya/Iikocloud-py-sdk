# DeletionMethod

Deletion method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment. | [optional] 
**id** | **str** | ID. | 
**removal_type** | [**DeliveryOrderResponseRemovalType**](DeliveryOrderResponseRemovalType.md) | Write-off type. | 

## Example

```python
from iikocloud_client.models.deletion_method import DeletionMethod

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionMethod from a JSON string
deletion_method_instance = DeletionMethod.from_json(json)
# print the JSON string representation of the object
print(DeletionMethod.to_json())

# convert the object into a dict
deletion_method_dict = deletion_method_instance.to_dict()
# create an instance of DeletionMethod from a dict
deletion_method_from_dict = DeletionMethod.from_dict(deletion_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


