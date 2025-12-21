# IikoTransportPublicApiContractsEmployeesEmployee

Employee DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Employee ID. | 
**first_name** | **str** | Name of user. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**display_name** | **str** | Displayed name (system name). | [optional] 
**code** | **str** | Code. | [optional] 
**is_deleted** | **bool** | User deletion flag. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employee import IikoTransportPublicApiContractsEmployeesEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesEmployee from a JSON string
iiko_transport_public_api_contracts_employees_employee_instance = IikoTransportPublicApiContractsEmployeesEmployee.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesEmployee.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_employee_dict = iiko_transport_public_api_contracts_employees_employee_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesEmployee from a dict
iiko_transport_public_api_contracts_employees_employee_from_dict = IikoTransportPublicApiContractsEmployeesEmployee.from_dict(iiko_transport_public_api_contracts_employees_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


