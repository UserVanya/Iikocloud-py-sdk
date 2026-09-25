# TreeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Date to retrieve the assembly chart for (YYYY-MM-DD) | [optional] 
**organization_id** | **UUID** | UUID of the organization (department) to build the assembly chart in the context of. Optional | [optional] 
**product_id** | **UUID** | UUID of the product to retrieve the assembly chart for | [optional] 

## Example

```python
from iikocloud_client.models.tree_request import TreeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TreeRequest from a JSON string
tree_request_instance = TreeRequest.from_json(json)
# print the JSON string representation of the object
print(TreeRequest.to_json())

# convert the object into a dict
tree_request_dict = tree_request_instance.to_dict()
# create an instance of TreeRequest from a dict
tree_request_from_dict = TreeRequest.from_dict(tree_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


