# NetCustomerGetCategoriesResponse

Get categories response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_categories** | [**List[NetCustomerGuestCategoryShortInfo]**](NetCustomerGuestCategoryShortInfo.md) | Guest categories for organization. | [optional] 

## Example

```python
from iikocloud_client.models.net_customer_get_categories_response import NetCustomerGetCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGetCategoriesResponse from a JSON string
net_customer_get_categories_response_instance = NetCustomerGetCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGetCategoriesResponse.to_json())

# convert the object into a dict
net_customer_get_categories_response_dict = net_customer_get_categories_response_instance.to_dict()
# create an instance of NetCustomerGetCategoriesResponse from a dict
net_customer_get_categories_response_from_dict = NetCustomerGetCategoriesResponse.from_dict(net_customer_get_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


