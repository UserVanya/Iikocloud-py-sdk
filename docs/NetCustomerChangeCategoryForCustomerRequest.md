# NetCustomerChangeCategoryForCustomerRequest

Change category for customer request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id. | 
**category_id** | **str** | Guest category id. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_customer_change_category_for_customer_request import NetCustomerChangeCategoryForCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerChangeCategoryForCustomerRequest from a JSON string
net_customer_change_category_for_customer_request_instance = NetCustomerChangeCategoryForCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerChangeCategoryForCustomerRequest.to_json())

# convert the object into a dict
net_customer_change_category_for_customer_request_dict = net_customer_change_category_for_customer_request_instance.to_dict()
# create an instance of NetCustomerChangeCategoryForCustomerRequest from a dict
net_customer_change_category_for_customer_request_from_dict = NetCustomerChangeCategoryForCustomerRequest.from_dict(net_customer_change_category_for_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


