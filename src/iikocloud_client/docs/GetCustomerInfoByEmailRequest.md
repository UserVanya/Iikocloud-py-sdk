# GetCustomerInfoByEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Customer email. | [optional] 

## Example

```python
from iikocloud_client.models.get_customer_info_by_email_request import GetCustomerInfoByEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerInfoByEmailRequest from a JSON string
get_customer_info_by_email_request_instance = GetCustomerInfoByEmailRequest.from_json(json)
# print the JSON string representation of the object
print(GetCustomerInfoByEmailRequest.to_json())

# convert the object into a dict
get_customer_info_by_email_request_dict = get_customer_info_by_email_request_instance.to_dict()
# create an instance of GetCustomerInfoByEmailRequest from a dict
get_customer_info_by_email_request_from_dict = GetCustomerInfoByEmailRequest.from_dict(get_customer_info_by_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


