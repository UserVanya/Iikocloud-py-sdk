# CustomerGetCategoriesResponse

Get categories response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_categories** | [**List[CustomerGuestCategoryShortInfo]**](CustomerGuestCategoryShortInfo.md) | Guest categories for organization. | [optional] 

## Example

```python
from iikocloud_client.models.customer_get_categories_response import CustomerGetCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCategoriesResponse from a JSON string
customer_get_categories_response_instance = CustomerGetCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCategoriesResponse.to_json())

# convert the object into a dict
customer_get_categories_response_dict = customer_get_categories_response_instance.to_dict()
# create an instance of CustomerGetCategoriesResponse from a dict
customer_get_categories_response_from_dict = CustomerGetCategoriesResponse.from_dict(customer_get_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


