# ClearStopListRequest

Request to clear out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.clear_stop_list_request import ClearStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClearStopListRequest from a JSON string
clear_stop_list_request_instance = ClearStopListRequest.from_json(json)
# print the JSON string representation of the object
print(ClearStopListRequest.to_json())

# convert the object into a dict
clear_stop_list_request_dict = clear_stop_list_request_instance.to_dict()
# create an instance of ClearStopListRequest from a dict
clear_stop_list_request_from_dict = ClearStopListRequest.from_dict(clear_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


