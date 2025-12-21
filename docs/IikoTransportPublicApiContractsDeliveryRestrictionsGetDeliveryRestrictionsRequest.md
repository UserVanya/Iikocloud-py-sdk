# IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest

Request for delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which delivery restrictions have to be returned.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request import IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request_instance = IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request_dict = iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest from a dict
iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


