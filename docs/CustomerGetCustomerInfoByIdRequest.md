# CustomerGetCustomerInfoByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Customer id. | [optional] 

## Example

```python
from iikocloud_client.models.customer_get_customer_info_by_id_request import CustomerGetCustomerInfoByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCustomerInfoByIdRequest from a JSON string
customer_get_customer_info_by_id_request_instance = CustomerGetCustomerInfoByIdRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCustomerInfoByIdRequest.to_json())

# convert the object into a dict
customer_get_customer_info_by_id_request_dict = customer_get_customer_info_by_id_request_instance.to_dict()
# create an instance of CustomerGetCustomerInfoByIdRequest from a dict
customer_get_customer_info_by_id_request_from_dict = CustomerGetCustomerInfoByIdRequest.from_dict(customer_get_customer_info_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


