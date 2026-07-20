# AddCustomerToProgramResponse

Add customer to program response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_wallet_id** | **UUID** | User wallet id. | [optional] 
**wallet_id** | **UUID** | Program Wallet id which guest was added to. | [optional] 

## Example

```python
from iikocloud_client.models.add_customer_to_program_response import AddCustomerToProgramResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomerToProgramResponse from a JSON string
add_customer_to_program_response_instance = AddCustomerToProgramResponse.from_json(json)
# print the JSON string representation of the object
print(AddCustomerToProgramResponse.to_json())

# convert the object into a dict
add_customer_to_program_response_dict = add_customer_to_program_response_instance.to_dict()
# create an instance of AddCustomerToProgramResponse from a dict
add_customer_to_program_response_from_dict = AddCustomerToProgramResponse.from_dict(add_customer_to_program_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


