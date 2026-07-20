# CheckSmsStatusResponse

Check sms status response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**List[SmsSendingStatusInfo]**](SmsSendingStatusInfo.md) | Information about the status of sending SMS. | 

## Example

```python
from iikocloud_client.models.check_sms_status_response import CheckSmsStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckSmsStatusResponse from a JSON string
check_sms_status_response_instance = CheckSmsStatusResponse.from_json(json)
# print the JSON string representation of the object
print(CheckSmsStatusResponse.to_json())

# convert the object into a dict
check_sms_status_response_dict = check_sms_status_response_instance.to_dict()
# create an instance of CheckSmsStatusResponse from a dict
check_sms_status_response_from_dict = CheckSmsStatusResponse.from_dict(check_sms_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


