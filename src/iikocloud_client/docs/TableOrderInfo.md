# TableOrderInfo

Order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_status** | [**CreationStatus**](CreationStatus.md) | Order creation status. In case of asynchronous creation, it allows to track the instance an order was validated/created in iikoFront. | 
**error_info** | [**ErrorInfo**](ErrorInfo.md) | Order creation error details.  &gt; Required only if \&quot;creationStatus\&quot;&#x3D;\&quot;Error\&quot;. | [optional] 
**external_number** | **str** | Order external number. | [optional] 
**id** | **UUID** | Order ID. | 
**order** | [**TableOrderResponsePayload**](TableOrderResponsePayload.md) | Order creation details.  &gt; Field is filled up if \&quot;creationStatus\&quot;&#x3D;\&quot;Success\&quot;. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**pos_id** | **UUID** | POS order ID. | [optional] 
**timestamp** | **int** | Timestamp of most recent order change that took place on iikoTransport server. | 

## Example

```python
from iikocloud_client.models.table_order_info import TableOrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrderInfo from a JSON string
table_order_info_instance = TableOrderInfo.from_json(json)
# print the JSON string representation of the object
print(TableOrderInfo.to_json())

# convert the object into a dict
table_order_info_dict = table_order_info_instance.to_dict()
# create an instance of TableOrderInfo from a dict
table_order_info_from_dict = TableOrderInfo.from_dict(table_order_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


