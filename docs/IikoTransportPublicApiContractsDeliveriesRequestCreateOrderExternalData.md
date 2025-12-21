# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData

Order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key. | 
**value** | **str** | Value. | 
**is_public** | **bool** | The transmitted data may contain both technical identifiers and information useful for the restaurant employee.  If it is necessary for the data to be included in the sales report, then this parameter must be set to TRUE, otherwise to FALSE. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_external_data import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_external_data_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_external_data_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_external_data_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_external_data_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_external_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


