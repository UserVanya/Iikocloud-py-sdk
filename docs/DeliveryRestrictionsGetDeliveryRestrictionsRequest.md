# DeliveryRestrictionsGetDeliveryRestrictionsRequest

Request for delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which delivery restrictions have to be returned.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_get_delivery_restrictions_request import DeliveryRestrictionsGetDeliveryRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsGetDeliveryRestrictionsRequest from a JSON string
delivery_restrictions_get_delivery_restrictions_request_instance = DeliveryRestrictionsGetDeliveryRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsGetDeliveryRestrictionsRequest.to_json())

# convert the object into a dict
delivery_restrictions_get_delivery_restrictions_request_dict = delivery_restrictions_get_delivery_restrictions_request_instance.to_dict()
# create an instance of DeliveryRestrictionsGetDeliveryRestrictionsRequest from a dict
delivery_restrictions_get_delivery_restrictions_request_from_dict = DeliveryRestrictionsGetDeliveryRestrictionsRequest.from_dict(delivery_restrictions_get_delivery_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


