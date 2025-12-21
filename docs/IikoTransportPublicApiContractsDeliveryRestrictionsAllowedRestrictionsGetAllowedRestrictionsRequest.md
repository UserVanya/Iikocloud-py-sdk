# IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest

Request to identify suitable terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID. Deprecated, use \&quot;organizationIds\&quot;. | [optional] 
**organization_ids** | **List[UUID]** | Organization IDs.                Can be obtained by &#x60;/organizations&#x60; operation. | [optional] 
**delivery_address** | [**IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.md) | Delivery address. | [optional] 
**order_location** | [**IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsOrderLocation**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsOrderLocation.md) | Order location. | [optional] 
**order_items** | [**List[IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem]**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.md) | Order list. | [optional] 
**is_courier_delivery** | **bool** | Type of delivery service. | 
**delivery_date** | **str** | Delivery date (Local for delivery terminal). | [optional] 
**delivery_sum** | **float** | Sum. | [optional] 
**discount_sum** | **float** | Discounts sum. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request import IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_instance = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_dict = iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest from a dict
iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


