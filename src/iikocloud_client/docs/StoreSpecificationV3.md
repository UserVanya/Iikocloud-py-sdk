# StoreSpecificationV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inverse** | **bool** | true — specification applies to all departments EXCEPT the listed ones | [optional] 
**organization_ids** | **List[UUID]** | UUIDs of organizations (structural units) the specification applies to | [optional] 

## Example

```python
from iikocloud_client.models.store_specification_v3 import StoreSpecificationV3

# TODO update the JSON string below
json = "{}"
# create an instance of StoreSpecificationV3 from a JSON string
store_specification_v3_instance = StoreSpecificationV3.from_json(json)
# print the JSON string representation of the object
print(StoreSpecificationV3.to_json())

# convert the object into a dict
store_specification_v3_dict = store_specification_v3_instance.to_dict()
# create an instance of StoreSpecificationV3 from a dict
store_specification_v3_from_dict = StoreSpecificationV3.from_dict(store_specification_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


