# CustomerDeleteCustomersRequest

Delete customers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ids** | **List[str]** | Customer IDs for logical deletion. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_delete_customers_request import CustomerDeleteCustomersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerDeleteCustomersRequest from a JSON string
customer_delete_customers_request_instance = CustomerDeleteCustomersRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerDeleteCustomersRequest.to_json())

# convert the object into a dict
customer_delete_customers_request_dict = customer_delete_customers_request_instance.to_dict()
# create an instance of CustomerDeleteCustomersRequest from a dict
customer_delete_customers_request_from_dict = CustomerDeleteCustomersRequest.from_dict(customer_delete_customers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


