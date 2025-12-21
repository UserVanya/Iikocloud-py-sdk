# IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse

DTO containing driver coordinates details for the last N seconds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**courier_locations** | [**List[RmsItemsResponseWrapperEmployeesCourierLocations]**](RmsItemsResponseWrapperEmployeesCourierLocations.md) | List of drivers&#39; coordinates broken down by organizations. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_response import IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse from a JSON string
iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_response_instance = IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_response_dict = iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse from a dict
iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_response_from_dict = IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse.from_dict(iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


