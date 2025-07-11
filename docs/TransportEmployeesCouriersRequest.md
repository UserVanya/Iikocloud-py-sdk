# TransportEmployeesCouriersRequest

Request for list of drivers for organizations in OrganizationIds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | List of organizations. | 

## Example

```python
from iikocloud_client.models.transport_employees_couriers_request import TransportEmployeesCouriersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesCouriersRequest from a JSON string
transport_employees_couriers_request_instance = TransportEmployeesCouriersRequest.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesCouriersRequest.to_json())

# convert the object into a dict
transport_employees_couriers_request_dict = transport_employees_couriers_request_instance.to_dict()
# create an instance of TransportEmployeesCouriersRequest from a dict
transport_employees_couriers_request_from_dict = TransportEmployeesCouriersRequest.from_dict(transport_employees_couriers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


