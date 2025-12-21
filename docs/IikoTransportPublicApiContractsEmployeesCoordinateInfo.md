# IikoTransportPublicApiContractsEmployeesCoordinateInfo

DTO of map coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 
**server_timestamp** | **int** | Time of coordinate saving on server in the Unix timestamp format. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_coordinate_info import IikoTransportPublicApiContractsEmployeesCoordinateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesCoordinateInfo from a JSON string
iiko_transport_public_api_contracts_employees_coordinate_info_instance = IikoTransportPublicApiContractsEmployeesCoordinateInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesCoordinateInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_coordinate_info_dict = iiko_transport_public_api_contracts_employees_coordinate_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesCoordinateInfo from a dict
iiko_transport_public_api_contracts_employees_coordinate_info_from_dict = IikoTransportPublicApiContractsEmployeesCoordinateInfo.from_dict(iiko_transport_public_api_contracts_employees_coordinate_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


