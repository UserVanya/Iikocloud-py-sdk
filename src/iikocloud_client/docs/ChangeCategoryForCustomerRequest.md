# ChangeCategoryForCustomerRequest

Change category for customer request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **UUID** | Guest category id. | 
**customer_id** | **UUID** | Customer id. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.change_category_for_customer_request import ChangeCategoryForCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeCategoryForCustomerRequest from a JSON string
change_category_for_customer_request_instance = ChangeCategoryForCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeCategoryForCustomerRequest.to_json())

# convert the object into a dict
change_category_for_customer_request_dict = change_category_for_customer_request_instance.to_dict()
# create an instance of ChangeCategoryForCustomerRequest from a dict
change_category_for_customer_request_from_dict = ChangeCategoryForCustomerRequest.from_dict(change_category_for_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


