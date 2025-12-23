# DeliveryRestrictionsAllowedRestrictionsRestrictionsAddress

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
from iikocloud_client.models.delivery_restrictions_allowed_restrictions_restrictions_address import DeliveryRestrictionsAllowedRestrictionsRestrictionsAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsAllowedRestrictionsRestrictionsAddress from a JSON string
delivery_restrictions_allowed_restrictions_restrictions_address_instance = DeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.to_json())

# convert the object into a dict
delivery_restrictions_allowed_restrictions_restrictions_address_dict = delivery_restrictions_allowed_restrictions_restrictions_address_instance.to_dict()
# create an instance of DeliveryRestrictionsAllowedRestrictionsRestrictionsAddress from a dict
delivery_restrictions_allowed_restrictions_restrictions_address_from_dict = DeliveryRestrictionsAllowedRestrictionsRestrictionsAddress.from_dict(delivery_restrictions_allowed_restrictions_restrictions_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


