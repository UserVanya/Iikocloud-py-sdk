# CustomerAddCustomerToProgramRequest

Add customer to program request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | [optional] 
**program_id** | **UUID** | Program id. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_add_customer_to_program_request import CustomerAddCustomerToProgramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAddCustomerToProgramRequest from a JSON string
customer_add_customer_to_program_request_instance = CustomerAddCustomerToProgramRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerAddCustomerToProgramRequest.to_json())

# convert the object into a dict
customer_add_customer_to_program_request_dict = customer_add_customer_to_program_request_instance.to_dict()
# create an instance of CustomerAddCustomerToProgramRequest from a dict
customer_add_customer_to_program_request_from_dict = CustomerAddCustomerToProgramRequest.from_dict(customer_add_customer_to_program_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


