# DeliveriesResponseOrdersResponse

Wrapping object (external) for return of delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**orders** | [**List[DeliveriesResponseOrderOrderInfo]**](DeliveriesResponseOrderOrderInfo.md) | Orders. | 

## Example

```python
from iikocloud_client.models.deliveries_response_orders_response import DeliveriesResponseOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrdersResponse from a JSON string
deliveries_response_orders_response_instance = DeliveriesResponseOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrdersResponse.to_json())

# convert the object into a dict
deliveries_response_orders_response_dict = deliveries_response_orders_response_instance.to_dict()
# create an instance of DeliveriesResponseOrdersResponse from a dict
deliveries_response_orders_response_from_dict = DeliveriesResponseOrdersResponse.from_dict(deliveries_response_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


