# DeliveriesRequestCloseTableOrderRequest

Request for close table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cheque_additional_info** | [**DeliveriesCommonChequeAdditionalInfo**](DeliveriesCommonChequeAdditionalInfo.md) | Cheque additional information according to russian federal law #54. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.deliveries_request_close_table_order_request import DeliveriesRequestCloseTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCloseTableOrderRequest from a JSON string
deliveries_request_close_table_order_request_instance = DeliveriesRequestCloseTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCloseTableOrderRequest.to_json())

# convert the object into a dict
deliveries_request_close_table_order_request_dict = deliveries_request_close_table_order_request_instance.to_dict()
# create an instance of DeliveriesRequestCloseTableOrderRequest from a dict
deliveries_request_close_table_order_request_from_dict = DeliveriesRequestCloseTableOrderRequest.from_dict(deliveries_request_close_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


