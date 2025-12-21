# IikoTransportPublicApiContractsDeliveriesResponseOrderStreet

Street.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 
**city** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCity**](IikoTransportPublicApiContractsDeliveriesResponseOrderCity.md) | City. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_street import IikoTransportPublicApiContractsDeliveriesResponseOrderStreet

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderStreet from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_street_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderStreet.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderStreet.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_street_dict = iiko_transport_public_api_contracts_deliveries_response_order_street_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderStreet from a dict
iiko_transport_public_api_contracts_deliveries_response_order_street_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderStreet.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


