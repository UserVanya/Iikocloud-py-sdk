# CustomerChangeCategoryForCustomerRequest

Change category for customer request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | 
**category_id** | **UUID** | Guest category id. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_change_category_for_customer_request import CustomerChangeCategoryForCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerChangeCategoryForCustomerRequest from a JSON string
customer_change_category_for_customer_request_instance = CustomerChangeCategoryForCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerChangeCategoryForCustomerRequest.to_json())

# convert the object into a dict
customer_change_category_for_customer_request_dict = customer_change_category_for_customer_request_instance.to_dict()
# create an instance of CustomerChangeCategoryForCustomerRequest from a dict
customer_change_category_for_customer_request_from_dict = CustomerChangeCategoryForCustomerRequest.from_dict(customer_change_category_for_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


