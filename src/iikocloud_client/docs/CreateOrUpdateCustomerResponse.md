# CreateOrUpdateCustomerResponse

Create or update customer response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Customer id. | [optional] 

## Example

```python
from iikocloud_client.models.create_or_update_customer_response import CreateOrUpdateCustomerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateCustomerResponse from a JSON string
create_or_update_customer_response_instance = CreateOrUpdateCustomerResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateCustomerResponse.to_json())

# convert the object into a dict
create_or_update_customer_response_dict = create_or_update_customer_response_instance.to_dict()
# create an instance of CreateOrUpdateCustomerResponse from a dict
create_or_update_customer_response_from_dict = CreateOrUpdateCustomerResponse.from_dict(create_or_update_customer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


