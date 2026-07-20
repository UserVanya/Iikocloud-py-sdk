# SmsSendingPossibilityRequest

Sms sending possibility request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.sms_sending_possibility_request import SmsSendingPossibilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SmsSendingPossibilityRequest from a JSON string
sms_sending_possibility_request_instance = SmsSendingPossibilityRequest.from_json(json)
# print the JSON string representation of the object
print(SmsSendingPossibilityRequest.to_json())

# convert the object into a dict
sms_sending_possibility_request_dict = sms_sending_possibility_request_instance.to_dict()
# create an instance of SmsSendingPossibilityRequest from a dict
sms_sending_possibility_request_from_dict = SmsSendingPossibilityRequest.from_dict(sms_sending_possibility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


