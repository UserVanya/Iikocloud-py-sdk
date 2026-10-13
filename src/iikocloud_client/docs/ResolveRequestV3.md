# ResolveRequestV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date to resolve the chart representation for (YYYY-MM-DD) | [optional] 
**organization_id** | **UUID** | UUID of the organization (department) to build the representation in the context of. Optional | [optional] 
**product_id** | **UUID** | UUID of the product (dish, modifier, semi-finished product) to resolve the chart representation for | [optional] 
**view** | **str** | Chart representation: assembled — top-level chart, prepared — breakdown to store items, tree — recipe tree | [optional] 

## Example

```python
from iikocloud_client.models.resolve_request_v3 import ResolveRequestV3

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveRequestV3 from a JSON string
resolve_request_v3_instance = ResolveRequestV3.from_json(json)
# print the JSON string representation of the object
print(ResolveRequestV3.to_json())

# convert the object into a dict
resolve_request_v3_dict = resolve_request_v3_instance.to_dict()
# create an instance of ResolveRequestV3 from a dict
resolve_request_v3_from_dict = ResolveRequestV3.from_dict(resolve_request_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


