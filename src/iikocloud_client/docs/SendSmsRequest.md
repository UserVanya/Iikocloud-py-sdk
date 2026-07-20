# SendSmsRequest

Send sms request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | 
**phone** | **str** | Customer&#39;s phone number. Can be null. | 
**text** | **str** | Message text. Can be null. | 

## Example

```python
from iikocloud_client.models.send_sms_request import SendSmsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendSmsRequest from a JSON string
send_sms_request_instance = SendSmsRequest.from_json(json)
# print the JSON string representation of the object
print(SendSmsRequest.to_json())

# convert the object into a dict
send_sms_request_dict = send_sms_request_instance.to_dict()
# create an instance of SendSmsRequest from a dict
send_sms_request_from_dict = SendSmsRequest.from_dict(send_sms_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


