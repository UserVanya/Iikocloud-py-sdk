# TableOrdersResponseTableOrderInfo

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID. | 
**pos_id** | **str** | POS order ID. | [optional] 
**external_number** | **str** | Order external number. | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**timestamp** | **int** | Timestamp of most recent order change that took place on iikoTransport server. | 
**creation_status** | [**DeliveriesResponseOrderCreationStatus**](DeliveriesResponseOrderCreationStatus.md) | Order creation status. In case of asynchronous creation, it allows to track the instance an order was validated/created in iikoFront. | 
**error_info** | [**ErrorsErrorInfo**](ErrorsErrorInfo.md) | Order creation error details.  &gt; Required only if \&quot;creationStatus\&quot;&#x3D;\&quot;Error\&quot;. | [optional] 
**order** | [**TableOrdersResponseTableOrder**](TableOrdersResponseTableOrder.md) | Order creation details.  &gt; Field is filled up if \&quot;creationStatus\&quot;&#x3D;\&quot;Success\&quot;. | [optional] 

## Example

```python
from iikocloud_client.models.table_orders_response_table_order_info import TableOrdersResponseTableOrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersResponseTableOrderInfo from a JSON string
table_orders_response_table_order_info_instance = TableOrdersResponseTableOrderInfo.from_json(json)
# print the JSON string representation of the object
print(TableOrdersResponseTableOrderInfo.to_json())

# convert the object into a dict
table_orders_response_table_order_info_dict = table_orders_response_table_order_info_instance.to_dict()
# create an instance of TableOrdersResponseTableOrderInfo from a dict
table_orders_response_table_order_info_from_dict = TableOrdersResponseTableOrderInfo.from_dict(table_orders_response_table_order_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


