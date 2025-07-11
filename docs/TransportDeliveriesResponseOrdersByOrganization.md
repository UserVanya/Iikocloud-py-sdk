# TransportDeliveriesResponseOrdersByOrganization

Orders grouped by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**orders** | [**List[TransportDeliveriesResponseOrderOrderInfo]**](TransportDeliveriesResponseOrderOrderInfo.md) | List of orders by organization. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_orders_by_organization import TransportDeliveriesResponseOrdersByOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrdersByOrganization from a JSON string
transport_deliveries_response_orders_by_organization_instance = TransportDeliveriesResponseOrdersByOrganization.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrdersByOrganization.to_json())

# convert the object into a dict
transport_deliveries_response_orders_by_organization_dict = transport_deliveries_response_orders_by_organization_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrdersByOrganization from a dict
transport_deliveries_response_orders_by_organization_from_dict = TransportDeliveriesResponseOrdersByOrganization.from_dict(transport_deliveries_response_orders_by_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


