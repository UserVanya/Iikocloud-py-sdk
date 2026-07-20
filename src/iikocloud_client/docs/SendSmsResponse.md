# SendSmsResponse

Send sms response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_id** | **UUID** | Sms id. | [optional] 

## Example

```python
from iikocloud_client.models.send_sms_response import SendSmsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendSmsResponse from a JSON string
send_sms_response_instance = SendSmsResponse.from_json(json)
# print the JSON string representation of the object
print(SendSmsResponse.to_json())

# convert the object into a dict
send_sms_response_dict = send_sms_response_instance.to_dict()
# create an instance of SendSmsResponse from a dict
send_sms_response_from_dict = SendSmsResponse.from_dict(send_sms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


