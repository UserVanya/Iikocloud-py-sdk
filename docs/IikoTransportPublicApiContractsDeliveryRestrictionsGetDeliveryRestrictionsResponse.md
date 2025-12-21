# IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse

Response for delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**delivery_restrictions** | [**List[IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryRestrictions]**](IikoTransportPublicApiContractsDeliveryRestrictionsDeliveryRestrictions.md) | Delivery restrictions. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_response import IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_response_instance = IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_response_dict = iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse from a dict
iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_response_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


