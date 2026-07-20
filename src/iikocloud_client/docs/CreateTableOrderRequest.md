# CreateTableOrderRequest

Order creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_order_settings** | [**CreateTableOrderSettings**](CreateTableOrderSettings.md) | Order creation parameters. | [optional] 
**order** | [**TableOrderRequest**](TableOrderRequest.md) | Order. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Front group ID an order must be sent to.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.create_table_order_request import CreateTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTableOrderRequest from a JSON string
create_table_order_request_instance = CreateTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTableOrderRequest.to_json())

# convert the object into a dict
create_table_order_request_dict = create_table_order_request_instance.to_dict()
# create an instance of CreateTableOrderRequest from a dict
create_table_order_request_from_dict = CreateTableOrderRequest.from_dict(create_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


