# SmsSendingStatusInfo

Sms sending status info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_error** | **str** | Sms sending internal error. Can be null. | [optional] 
**sms_id** | **UUID** | Sms id. | 
**status** | [**SmsSendingStatus**](SmsSendingStatus.md) | Sms sending status. | 

## Example

```python
from iikocloud_client.models.sms_sending_status_info import SmsSendingStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SmsSendingStatusInfo from a JSON string
sms_sending_status_info_instance = SmsSendingStatusInfo.from_json(json)
# print the JSON string representation of the object
print(SmsSendingStatusInfo.to_json())

# convert the object into a dict
sms_sending_status_info_dict = sms_sending_status_info_instance.to_dict()
# create an instance of SmsSendingStatusInfo from a dict
sms_sending_status_info_from_dict = SmsSendingStatusInfo.from_dict(sms_sending_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


