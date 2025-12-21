# CustomerGetCustomerInfoByPhoneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Customer phone number. | [optional] 

## Example

```python
from iikocloud_client.models.customer_get_customer_info_by_phone_request import CustomerGetCustomerInfoByPhoneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCustomerInfoByPhoneRequest from a JSON string
customer_get_customer_info_by_phone_request_instance = CustomerGetCustomerInfoByPhoneRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCustomerInfoByPhoneRequest.to_json())

# convert the object into a dict
customer_get_customer_info_by_phone_request_dict = customer_get_customer_info_by_phone_request_instance.to_dict()
# create an instance of CustomerGetCustomerInfoByPhoneRequest from a dict
customer_get_customer_info_by_phone_request_from_dict = CustomerGetCustomerInfoByPhoneRequest.from_dict(customer_get_customer_info_by_phone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


