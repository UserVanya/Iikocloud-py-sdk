# DeliveriesResponseOrdersByOrganization

Orders grouped by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**orders** | [**List[DeliveriesResponseOrderOrderInfo]**](DeliveriesResponseOrderOrderInfo.md) | List of orders by organization. | 

## Example

```python
from iikocloud_client.models.deliveries_response_orders_by_organization import DeliveriesResponseOrdersByOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrdersByOrganization from a JSON string
deliveries_response_orders_by_organization_instance = DeliveriesResponseOrdersByOrganization.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrdersByOrganization.to_json())

# convert the object into a dict
deliveries_response_orders_by_organization_dict = deliveries_response_orders_by_organization_instance.to_dict()
# create an instance of DeliveriesResponseOrdersByOrganization from a dict
deliveries_response_orders_by_organization_from_dict = DeliveriesResponseOrdersByOrganization.from_dict(deliveries_response_orders_by_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


