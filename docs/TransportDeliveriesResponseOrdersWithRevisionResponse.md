# TransportDeliveriesResponseOrdersWithRevisionResponse

Wrapping object (external) for return of delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**max_revision** | **int** | Maximum revision value per all orders. | 
**orders_by_organizations** | [**List[TransportDeliveriesResponseOrdersByOrganization]**](TransportDeliveriesResponseOrdersByOrganization.md) | Orders. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_orders_with_revision_response import TransportDeliveriesResponseOrdersWithRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrdersWithRevisionResponse from a JSON string
transport_deliveries_response_orders_with_revision_response_instance = TransportDeliveriesResponseOrdersWithRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrdersWithRevisionResponse.to_json())

# convert the object into a dict
transport_deliveries_response_orders_with_revision_response_dict = transport_deliveries_response_orders_with_revision_response_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrdersWithRevisionResponse from a dict
transport_deliveries_response_orders_with_revision_response_from_dict = TransportDeliveriesResponseOrdersWithRevisionResponse.from_dict(transport_deliveries_response_orders_with_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


