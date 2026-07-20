# SmsSendingPossibilityResponse

Sms sending possibility response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_sms_count** | **int** | Available sms count. | [optional] 
**status** | [**NotificationSendingCapabilityCheckStatus**](NotificationSendingCapabilityCheckStatus.md) | Notification sending capability check status. | [optional] 

## Example

```python
from iikocloud_client.models.sms_sending_possibility_response import SmsSendingPossibilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmsSendingPossibilityResponse from a JSON string
sms_sending_possibility_response_instance = SmsSendingPossibilityResponse.from_json(json)
# print the JSON string representation of the object
print(SmsSendingPossibilityResponse.to_json())

# convert the object into a dict
sms_sending_possibility_response_dict = sms_sending_possibility_response_instance.to_dict()
# create an instance of SmsSendingPossibilityResponse from a dict
sms_sending_possibility_response_from_dict = SmsSendingPossibilityResponse.from_dict(sms_sending_possibility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


