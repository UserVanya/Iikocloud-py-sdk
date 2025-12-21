# DeliveriesRequestCreateOrderAddress

Order delivery address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_address import DeliveriesRequestCreateOrderAddress

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderAddress from a JSON string
deliveries_request_create_order_address_instance = DeliveriesRequestCreateOrderAddress.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderAddress.to_json())

# convert the object into a dict
deliveries_request_create_order_address_dict = deliveries_request_create_order_address_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderAddress from a dict
deliveries_request_create_order_address_from_dict = DeliveriesRequestCreateOrderAddress.from_dict(deliveries_request_create_order_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


