# CheckSmsStatusRequest

Check sms status request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | 
**sms_ids** | **List[UUID]** | Sms IDs for checking. | 

## Example

```python
from iikocloud_client.models.check_sms_status_request import CheckSmsStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSmsStatusRequest from a JSON string
check_sms_status_request_instance = CheckSmsStatusRequest.from_json(json)
# print the JSON string representation of the object
print(CheckSmsStatusRequest.to_json())

# convert the object into a dict
check_sms_status_request_dict = check_sms_status_request_instance.to_dict()
# create an instance of CheckSmsStatusRequest from a dict
check_sms_status_request_from_dict = CheckSmsStatusRequest.from_dict(check_sms_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


