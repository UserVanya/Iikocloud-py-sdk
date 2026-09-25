# StoreSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverse** | **bool** | true — specification applies to all departments EXCEPT the listed ones | [optional] 
**organization_ids** | **List[UUID]** | UUIDs of organizations (structural units) the specification applies to | [optional] 

## Example

```python
from iikocloud_client.models.store_specification import StoreSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of StoreSpecification from a JSON string
store_specification_instance = StoreSpecification.from_json(json)
# print the JSON string representation of the object
print(StoreSpecification.to_json())

# convert the object into a dict
store_specification_dict = store_specification_instance.to_dict()
# create an instance of StoreSpecification from a dict
store_specification_from_dict = StoreSpecification.from_dict(store_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


