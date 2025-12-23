# DeliveriesResponseOrdersWithRevisionResponse

Wrapping object (external) for return of delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**max_revision** | **int** | Maximum revision value per all orders. | 
**orders_by_organizations** | [**List[DeliveriesResponseOrdersByOrganization]**](DeliveriesResponseOrdersByOrganization.md) | Orders. | 

## Example

```python
from iikocloud_client.models.deliveries_response_orders_with_revision_response import DeliveriesResponseOrdersWithRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrdersWithRevisionResponse from a JSON string
deliveries_response_orders_with_revision_response_instance = DeliveriesResponseOrdersWithRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrdersWithRevisionResponse.to_json())

# convert the object into a dict
deliveries_response_orders_with_revision_response_dict = deliveries_response_orders_with_revision_response_instance.to_dict()
# create an instance of DeliveriesResponseOrdersWithRevisionResponse from a dict
deliveries_response_orders_with_revision_response_from_dict = DeliveriesResponseOrdersWithRevisionResponse.from_dict(deliveries_response_orders_with_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


