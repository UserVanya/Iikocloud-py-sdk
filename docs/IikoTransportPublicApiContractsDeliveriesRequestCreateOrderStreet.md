# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderStreet

Street.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classifier_id** | **str** | Street ID in classifier, e.g., address database.  \\n &gt; For using in the Russian Federation only. | [optional] 
**id** | **UUID** | ID.                 Can be obtained by &#x60;/streets/by_city&#x60; operation. | [optional] 
**name** | **str** | Name. | [optional] 
**city** | **str** | City name. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_street import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderStreet

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderStreet from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_street_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderStreet.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderStreet.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_street_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_street_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderStreet from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_street_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderStreet.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_street_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


