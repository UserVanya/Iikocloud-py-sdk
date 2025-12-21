# IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo

Information about order guests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of persons. | 
**split_between_persons** | **bool** | Attribute that shows whether order must be split among guests. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_guests_info import IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_guests_info_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_guests_info_dict = iiko_transport_public_api_contracts_deliveries_response_order_guests_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo from a dict
iiko_transport_public_api_contracts_deliveries_response_order_guests_info_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderGuestsInfo.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_guests_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


