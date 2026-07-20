# DeleteCustomersRequest

Delete customers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ids** | **List[UUID]** | Customer IDs for logical deletion. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.delete_customers_request import DeleteCustomersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCustomersRequest from a JSON string
delete_customers_request_instance = DeleteCustomersRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteCustomersRequest.to_json())

# convert the object into a dict
delete_customers_request_dict = delete_customers_request_instance.to_dict()
# create an instance of DeleteCustomersRequest from a dict
delete_customers_request_from_dict = DeleteCustomersRequest.from_dict(delete_customers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


