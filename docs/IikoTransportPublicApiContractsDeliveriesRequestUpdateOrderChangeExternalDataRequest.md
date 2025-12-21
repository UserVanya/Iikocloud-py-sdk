# IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest

Request for change of delivery or table order external data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID. | 
**order_id** | **UUID** | Order ID. | 
**external_data** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderExternalData.md) | External data to change. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request_instance = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request_dict = iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


