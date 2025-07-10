# NetCustomerGetCategoriesRequest

Get categories request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization id. | 

## Example

```python
from iiko_cloud_client.models.net_customer_get_categories_request import NetCustomerGetCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGetCategoriesRequest from a JSON string
net_customer_get_categories_request_instance = NetCustomerGetCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGetCategoriesRequest.to_json())

# convert the object into a dict
net_customer_get_categories_request_dict = net_customer_get_categories_request_instance.to_dict()
# create an instance of NetCustomerGetCategoriesRequest from a dict
net_customer_get_categories_request_from_dict = NetCustomerGetCategoriesRequest.from_dict(net_customer_get_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


