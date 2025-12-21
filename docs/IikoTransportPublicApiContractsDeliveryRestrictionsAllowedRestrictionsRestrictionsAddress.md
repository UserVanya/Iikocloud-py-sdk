# IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress

Address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City. | [optional] 
**street_name** | **str** | Street. | [optional] 
**street_id** | **UUID** | Street ID. | [optional] 
**house** | **str** | House. | [optional] 
**building** | **str** | Building. | [optional] 
**index** | **str** | Post index. | [optional] 
**line1** | **str** | Address line 1.  Contains the primary address information. | [optional] 
**entrance** | **str** | Entrance. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_address import IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_address_instance = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_address_dict = iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_address_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress from a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_address_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_restrictions_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


