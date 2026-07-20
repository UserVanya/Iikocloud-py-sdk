# GetDeliveryRestrictionsRequest

Request for delivery restrictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which delivery restrictions have to be returned.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_delivery_restrictions_request import GetDeliveryRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeliveryRestrictionsRequest from a JSON string
get_delivery_restrictions_request_instance = GetDeliveryRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetDeliveryRestrictionsRequest.to_json())

# convert the object into a dict
get_delivery_restrictions_request_dict = get_delivery_restrictions_request_instance.to_dict()
# create an instance of GetDeliveryRestrictionsRequest from a dict
get_delivery_restrictions_request_from_dict = GetDeliveryRestrictionsRequest.from_dict(get_delivery_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


