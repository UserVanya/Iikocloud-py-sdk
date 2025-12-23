# CustomerGetCustomerInfoRequest

Base class for customer info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**organization_id** | **str** | Organization id. | [optional] 

## Example

```python
from iikocloud_client.models.customer_get_customer_info_request import CustomerGetCustomerInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCustomerInfoRequest from a JSON string
customer_get_customer_info_request_instance = CustomerGetCustomerInfoRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCustomerInfoRequest.to_json())

# convert the object into a dict
customer_get_customer_info_request_dict = customer_get_customer_info_request_instance.to_dict()
# create an instance of CustomerGetCustomerInfoRequest from a dict
customer_get_customer_info_request_from_dict = CustomerGetCustomerInfoRequest.from_dict(customer_get_customer_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


