# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderGuests

Information on guests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of persons in order. This field defines the number of cutlery sets | 
**split_between_persons** | **bool** | Attribute that shows whether order must be split among guests. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_guests import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderGuests

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderGuests from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_guests_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderGuests.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderGuests.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_guests_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_guests_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderGuests from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_guests_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderGuests.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_guests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


