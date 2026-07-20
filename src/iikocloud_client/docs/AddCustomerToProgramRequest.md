# AddCustomerToProgramRequest

Add customer to program request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | [optional] 
**organization_id** | **UUID** | Organization id. | 
**program_id** | **UUID** | Program id. | [optional] 

## Example

```python
from iikocloud_client.models.add_customer_to_program_request import AddCustomerToProgramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCustomerToProgramRequest from a JSON string
add_customer_to_program_request_instance = AddCustomerToProgramRequest.from_json(json)
# print the JSON string representation of the object
print(AddCustomerToProgramRequest.to_json())

# convert the object into a dict
add_customer_to_program_request_dict = add_customer_to_program_request_instance.to_dict()
# create an instance of AddCustomerToProgramRequest from a dict
add_customer_to_program_request_from_dict = AddCustomerToProgramRequest.from_dict(add_customer_to_program_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


