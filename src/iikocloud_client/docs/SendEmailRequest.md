# SendEmailRequest

Send email request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | Message body. Can be null. | 
**organization_id** | **UUID** | Organization id. | 
**receiver** | **str** | Email address. Can be null. | 
**subject** | **str** | Message subject. Can be null. | 

## Example

```python
from iikocloud_client.models.send_email_request import SendEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendEmailRequest from a JSON string
send_email_request_instance = SendEmailRequest.from_json(json)
# print the JSON string representation of the object
print(SendEmailRequest.to_json())

# convert the object into a dict
send_email_request_dict = send_email_request_instance.to_dict()
# create an instance of SendEmailRequest from a dict
send_email_request_from_dict = SendEmailRequest.from_dict(send_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


