# TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest

Request to identify suitable terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. Deprecated, use \&quot;organizationIds\&quot;. | [optional] 
**organization_ids** | **List[str]** | Organization IDs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**delivery_address** | [**TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress**](TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.md) | Delivery address. | [optional] 
**order_location** | [**TransportDeliveryRestrictionsAllowedRestrictionsOrderLocation**](TransportDeliveryRestrictionsAllowedRestrictionsOrderLocation.md) | Order location. | [optional] 
**order_items** | [**List[TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem]**](TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.md) | Order list. | [optional] 
**is_courier_delivery** | **bool** | Type of delivery service. | 
**delivery_date** | **str** | Delivery date (Local for delivery terminal). | [optional] 
**delivery_sum** | **float** | Sum. | [optional] 
**discount_sum** | **float** | Discounts sum. | [optional] 

## Example

```python
from iikocloud_client.models.transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request import TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest from a JSON string
transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_instance = TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.to_json())

# convert the object into a dict
transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_dict = transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest from a dict
transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_from_dict = TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.from_dict(transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


