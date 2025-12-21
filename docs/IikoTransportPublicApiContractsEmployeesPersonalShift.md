# IikoTransportPublicApiContractsEmployeesPersonalShift

Employee personal shift info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Employee ID. | 
**role_id** | **UUID** | Employee Role ID. | [optional] 
**opened** | **bool** | Personal shift state flag (true - shift is opened, false - shift is closed). | 
**terminal_group_id** | **UUID** | ID of the terminal group where the personal shift is opened/closed. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_personal_shift import IikoTransportPublicApiContractsEmployeesPersonalShift

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesPersonalShift from a JSON string
iiko_transport_public_api_contracts_employees_personal_shift_instance = IikoTransportPublicApiContractsEmployeesPersonalShift.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesPersonalShift.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_personal_shift_dict = iiko_transport_public_api_contracts_employees_personal_shift_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesPersonalShift from a dict
iiko_transport_public_api_contracts_employees_personal_shift_from_dict = IikoTransportPublicApiContractsEmployeesPersonalShift.from_dict(iiko_transport_public_api_contracts_employees_personal_shift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


