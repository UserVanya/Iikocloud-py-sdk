# OrdersByOrganization

Orders grouped by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[OrderInfo]**](OrderInfo.md) | List of orders by organization. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.orders_by_organization import OrdersByOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersByOrganization from a JSON string
orders_by_organization_instance = OrdersByOrganization.from_json(json)
# print the JSON string representation of the object
print(OrdersByOrganization.to_json())

# convert the object into a dict
orders_by_organization_dict = orders_by_organization_instance.to_dict()
# create an instance of OrdersByOrganization from a dict
orders_by_organization_from_dict = OrdersByOrganization.from_dict(orders_by_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


