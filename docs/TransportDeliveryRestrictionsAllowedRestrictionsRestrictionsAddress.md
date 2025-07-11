# TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress

Address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City. | [optional] 
**street_name** | **str** | Street. | [optional] 
**street_id** | **str** | Street ID. | [optional] 
**house** | **str** | House. | [optional] 
**building** | **str** | Building. | [optional] 
**index** | **str** | Post index. | [optional] 
**line1** | **str** | Address line 1.  Contains the primary address information. | [optional] 
**entrance** | **str** | Entrance. | [optional] 

## Example

```python
from iikocloud_client.models.transport_delivery_restrictions_allowed_restrictions_restrictions_address import TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress from a JSON string
transport_delivery_restrictions_allowed_restrictions_restrictions_address_instance = TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.to_json())

# convert the object into a dict
transport_delivery_restrictions_allowed_restrictions_restrictions_address_dict = transport_delivery_restrictions_allowed_restrictions_restrictions_address_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress from a dict
transport_delivery_restrictions_allowed_restrictions_restrictions_address_from_dict = TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.from_dict(transport_delivery_restrictions_allowed_restrictions_restrictions_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


