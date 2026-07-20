# GetCustomerInfoByPhoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Customer phone number. | [optional] 

## Example

```python
from iikocloud_client.models.get_customer_info_by_phone_request import GetCustomerInfoByPhoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerInfoByPhoneRequest from a JSON string
get_customer_info_by_phone_request_instance = GetCustomerInfoByPhoneRequest.from_json(json)
# print the JSON string representation of the object
print(GetCustomerInfoByPhoneRequest.to_json())

# convert the object into a dict
get_customer_info_by_phone_request_dict = get_customer_info_by_phone_request_instance.to_dict()
# create an instance of GetCustomerInfoByPhoneRequest from a dict
get_customer_info_by_phone_request_from_dict = GetCustomerInfoByPhoneRequest.from_dict(get_customer_info_by_phone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


