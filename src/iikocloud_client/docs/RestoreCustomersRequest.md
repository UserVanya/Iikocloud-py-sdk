# RestoreCustomersRequest

Restore customers request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_ids** | **List[UUID]** | Customer IDs to recover. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.restore_customers_request import RestoreCustomersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreCustomersRequest from a JSON string
restore_customers_request_instance = RestoreCustomersRequest.from_json(json)
# print the JSON string representation of the object
print(RestoreCustomersRequest.to_json())

# convert the object into a dict
restore_customers_request_dict = restore_customers_request_instance.to_dict()
# create an instance of RestoreCustomersRequest from a dict
restore_customers_request_from_dict = RestoreCustomersRequest.from_dict(restore_customers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


