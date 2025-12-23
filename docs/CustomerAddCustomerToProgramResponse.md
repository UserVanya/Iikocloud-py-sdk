# CustomerAddCustomerToProgramResponse

Add customer to program response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_wallet_id** | **str** | User wallet id. | [optional] 

## Example

```python
from iikocloud_client.models.customer_add_customer_to_program_response import CustomerAddCustomerToProgramResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerAddCustomerToProgramResponse from a JSON string
customer_add_customer_to_program_response_instance = CustomerAddCustomerToProgramResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerAddCustomerToProgramResponse.to_json())

# convert the object into a dict
customer_add_customer_to_program_response_dict = customer_add_customer_to_program_response_instance.to_dict()
# create an instance of CustomerAddCustomerToProgramResponse from a dict
customer_add_customer_to_program_response_from_dict = CustomerAddCustomerToProgramResponse.from_dict(customer_add_customer_to_program_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


