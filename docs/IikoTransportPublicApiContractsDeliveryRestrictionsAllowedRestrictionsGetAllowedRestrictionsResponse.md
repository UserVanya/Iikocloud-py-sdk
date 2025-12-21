# IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse

Response for a request to identify suitable terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**is_allowed** | **bool** | A sign of successful verification. | 
**reject_cause** | **str** | Reject cause. | 
**address_external_id** | **str** | Delivery address ID in external mapping system. | 
**location** | [**IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsOrderLocation**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsOrderLocation.md) | Coordinates returned by geocoding service. | 
**allowed_items** | [**List[IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration]**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsAllowedItemWithDuration.md) | Suitable terminal groups with a delivery duration for them. | 
**rejected_items** | [**List[IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItem]**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRejectItem.md) | Rejected items with cause. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response import IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_instance = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_dict = iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse from a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


