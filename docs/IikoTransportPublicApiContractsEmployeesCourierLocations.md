# IikoTransportPublicApiContractsEmployeesCourierLocations

Driver location details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier_id** | **UUID** | Driver ID. | 
**locations** | [**List[IikoTransportPublicApiContractsEmployeesCoordinateInfo]**](IikoTransportPublicApiContractsEmployeesCoordinateInfo.md) | List of locations. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_courier_locations import IikoTransportPublicApiContractsEmployeesCourierLocations

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesCourierLocations from a JSON string
iiko_transport_public_api_contracts_employees_courier_locations_instance = IikoTransportPublicApiContractsEmployeesCourierLocations.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesCourierLocations.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_courier_locations_dict = iiko_transport_public_api_contracts_employees_courier_locations_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesCourierLocations from a dict
iiko_transport_public_api_contracts_employees_courier_locations_from_dict = IikoTransportPublicApiContractsEmployeesCourierLocations.from_dict(iiko_transport_public_api_contracts_employees_courier_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


