# CustomerRestoreCustomersRequest

Restore customers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ids** | **List[UUID]** | Customer IDs to recover. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_restore_customers_request import CustomerRestoreCustomersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerRestoreCustomersRequest from a JSON string
customer_restore_customers_request_instance = CustomerRestoreCustomersRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerRestoreCustomersRequest.to_json())

# convert the object into a dict
customer_restore_customers_request_dict = customer_restore_customers_request_instance.to_dict()
# create an instance of CustomerRestoreCustomersRequest from a dict
customer_restore_customers_request_from_dict = CustomerRestoreCustomersRequest.from_dict(customer_restore_customers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


