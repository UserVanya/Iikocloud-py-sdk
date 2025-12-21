# IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse

Wrapping object to retrieve list of active courier locations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**active_courier_locations** | [**List[RmsItemsResponseWrapperEmployeesActiveCourierLocation]**](RmsItemsResponseWrapperEmployeesActiveCourierLocation.md) | List of courier&#39;s locations. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_active_courier_locations_response import IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse from a JSON string
iiko_transport_public_api_contracts_employees_active_courier_locations_response_instance = IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_active_courier_locations_response_dict = iiko_transport_public_api_contracts_employees_active_courier_locations_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse from a dict
iiko_transport_public_api_contracts_employees_active_courier_locations_response_from_dict = IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse.from_dict(iiko_transport_public_api_contracts_employees_active_courier_locations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


