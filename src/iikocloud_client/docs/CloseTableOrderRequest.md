# CloseTableOrderRequest

Request for close table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cheque_additional_info** | [**ChequeAdditionalInfo**](ChequeAdditionalInfo.md) | Cheque additional information according to russian federal law #54. | [optional] 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.close_table_order_request import CloseTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloseTableOrderRequest from a JSON string
close_table_order_request_instance = CloseTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CloseTableOrderRequest.to_json())

# convert the object into a dict
close_table_order_request_dict = close_table_order_request_instance.to_dict()
# create an instance of CloseTableOrderRequest from a dict
close_table_order_request_from_dict = CloseTableOrderRequest.from_dict(close_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


