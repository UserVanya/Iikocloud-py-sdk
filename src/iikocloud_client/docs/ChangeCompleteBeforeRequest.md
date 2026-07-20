# ChangeCompleteBeforeRequest

Request for change time when client wants the order to be delivered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_complete_before** | **str** | New time when client wants the order to be delivered (Local for delivery terminal). | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.change_complete_before_request import ChangeCompleteBeforeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeCompleteBeforeRequest from a JSON string
change_complete_before_request_instance = ChangeCompleteBeforeRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeCompleteBeforeRequest.to_json())

# convert the object into a dict
change_complete_before_request_dict = change_complete_before_request_instance.to_dict()
# create an instance of ChangeCompleteBeforeRequest from a dict
change_complete_before_request_from_dict = ChangeCompleteBeforeRequest.from_dict(change_complete_before_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


