# OrdersWithRevisionResponse

Wrapping object (external) for return of delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**max_revision** | **int** | Maximum revision value per all orders. | 
**orders_by_organizations** | [**List[OrdersByOrganization]**](OrdersByOrganization.md) | Orders. | 

## Example

```python
from iikocloud_client.models.orders_with_revision_response import OrdersWithRevisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersWithRevisionResponse from a JSON string
orders_with_revision_response_instance = OrdersWithRevisionResponse.from_json(json)
# print the JSON string representation of the object
print(OrdersWithRevisionResponse.to_json())

# convert the object into a dict
orders_with_revision_response_dict = orders_with_revision_response_instance.to_dict()
# create an instance of OrdersWithRevisionResponse from a dict
orders_with_revision_response_from_dict = OrdersWithRevisionResponse.from_dict(orders_with_revision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


