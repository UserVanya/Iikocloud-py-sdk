# CheckStopListRequest

Request for check items in out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeliveryOrderCreateItem]**](DeliveryOrderCreateItem.md) | Order items. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Front group ID the order must be sent to.    Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.check_stop_list_request import CheckStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckStopListRequest from a JSON string
check_stop_list_request_instance = CheckStopListRequest.from_json(json)
# print the JSON string representation of the object
print(CheckStopListRequest.to_json())

# convert the object into a dict
check_stop_list_request_dict = check_stop_list_request_instance.to_dict()
# create an instance of CheckStopListRequest from a dict
check_stop_list_request_from_dict = CheckStopListRequest.from_dict(check_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


