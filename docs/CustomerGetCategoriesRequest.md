# CustomerGetCategoriesRequest

Get categories request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_get_categories_request import CustomerGetCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCategoriesRequest from a JSON string
customer_get_categories_request_instance = CustomerGetCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCategoriesRequest.to_json())

# convert the object into a dict
customer_get_categories_request_dict = customer_get_categories_request_instance.to_dict()
# create an instance of CustomerGetCategoriesRequest from a dict
customer_get_categories_request_from_dict = CustomerGetCategoriesRequest.from_dict(customer_get_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


