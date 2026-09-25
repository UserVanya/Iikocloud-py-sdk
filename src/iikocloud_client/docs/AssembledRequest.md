# AssembledRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | Date to retrieve the assembly chart for (YYYY-MM-DD) | [optional] 
**organization_id** | **UUID** | UUID of the organization (department) to build the assembly chart in the context of. Optional | [optional] 
**product_id** | **UUID** | UUID of the product to retrieve the assembly chart for | [optional] 

## Example

```python
from iikocloud_client.models.assembled_request import AssembledRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssembledRequest from a JSON string
assembled_request_instance = AssembledRequest.from_json(json)
# print the JSON string representation of the object
print(AssembledRequest.to_json())

# convert the object into a dict
assembled_request_dict = assembled_request_instance.to_dict()
# create an instance of AssembledRequest from a dict
assembled_request_from_dict = AssembledRequest.from_dict(assembled_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


