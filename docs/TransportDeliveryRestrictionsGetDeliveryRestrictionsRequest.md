# TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest

Request for delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations IDs which delivery restrictions have to be returned.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iiko_cloud_client.models.transport_delivery_restrictions_get_delivery_restrictions_request import TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest from a JSON string
transport_delivery_restrictions_get_delivery_restrictions_request_instance = TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest.to_json())

# convert the object into a dict
transport_delivery_restrictions_get_delivery_restrictions_request_dict = transport_delivery_restrictions_get_delivery_restrictions_request_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest from a dict
transport_delivery_restrictions_get_delivery_restrictions_request_from_dict = TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest.from_dict(transport_delivery_restrictions_get_delivery_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


