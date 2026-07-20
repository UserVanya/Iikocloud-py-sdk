# ListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** | Period start date (YYYY-MM-DD format) | 
**organization_id** | **str** | Organization identifier (GUID) | 
**to** | **str** | Period end date (YYYY-MM-DD format) | 

## Example

```python
from iikocloud_client.models.list_request import ListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListRequest from a JSON string
list_request_instance = ListRequest.from_json(json)
# print the JSON string representation of the object
print(ListRequest.to_json())

# convert the object into a dict
list_request_dict = list_request_instance.to_dict()
# create an instance of ListRequest from a dict
list_request_from_dict = ListRequest.from_dict(list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


