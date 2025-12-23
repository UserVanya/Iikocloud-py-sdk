# CustomerCreateOrUpdateCustomerResponse

Create or update customer response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Customer id. | [optional] 

## Example

```python
from iikocloud_client.models.customer_create_or_update_customer_response import CustomerCreateOrUpdateCustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerCreateOrUpdateCustomerResponse from a JSON string
customer_create_or_update_customer_response_instance = CustomerCreateOrUpdateCustomerResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerCreateOrUpdateCustomerResponse.to_json())

# convert the object into a dict
customer_create_or_update_customer_response_dict = customer_create_or_update_customer_response_instance.to_dict()
# create an instance of CustomerCreateOrUpdateCustomerResponse from a dict
customer_create_or_update_customer_response_from_dict = CustomerCreateOrUpdateCustomerResponse.from_dict(customer_create_or_update_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


