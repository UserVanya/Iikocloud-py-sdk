# ChangeDriverInfoRequest

Request for change driver info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_id** | **UUID** | Driver ID.                Can be obtained by &#x60;/api/1/employees/couriers&#x60; operation. | [optional] 
**estimated_time** | **str** | Delivery estimated time. | [optional] 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.change_driver_info_request import ChangeDriverInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeDriverInfoRequest from a JSON string
change_driver_info_request_instance = ChangeDriverInfoRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeDriverInfoRequest.to_json())

# convert the object into a dict
change_driver_info_request_dict = change_driver_info_request_instance.to_dict()
# create an instance of ChangeDriverInfoRequest from a dict
change_driver_info_request_from_dict = ChangeDriverInfoRequest.from_dict(change_driver_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


