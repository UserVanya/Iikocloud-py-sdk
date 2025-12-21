# EmployeesCouriersRequest

Request for list of drivers for organizations in OrganizationIds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | List of organizations. | 

## Example

```python
from iikocloud_client.models.employees_couriers_request import EmployeesCouriersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesCouriersRequest from a JSON string
employees_couriers_request_instance = EmployeesCouriersRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeesCouriersRequest.to_json())

# convert the object into a dict
employees_couriers_request_dict = employees_couriers_request_instance.to_dict()
# create an instance of EmployeesCouriersRequest from a dict
employees_couriers_request_from_dict = EmployeesCouriersRequest.from_dict(employees_couriers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


