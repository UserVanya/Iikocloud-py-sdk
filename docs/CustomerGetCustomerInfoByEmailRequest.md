# CustomerGetCustomerInfoByEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Customer email. | [optional] 

## Example

```python
from iikocloud_client.models.customer_get_customer_info_by_email_request import CustomerGetCustomerInfoByEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCustomerInfoByEmailRequest from a JSON string
customer_get_customer_info_by_email_request_instance = CustomerGetCustomerInfoByEmailRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCustomerInfoByEmailRequest.to_json())

# convert the object into a dict
customer_get_customer_info_by_email_request_dict = customer_get_customer_info_by_email_request_instance.to_dict()
# create an instance of CustomerGetCustomerInfoByEmailRequest from a dict
customer_get_customer_info_by_email_request_from_dict = CustomerGetCustomerInfoByEmailRequest.from_dict(customer_get_customer_info_by_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


