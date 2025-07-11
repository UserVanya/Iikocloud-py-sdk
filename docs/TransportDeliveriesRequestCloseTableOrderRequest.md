# TransportDeliveriesRequestCloseTableOrderRequest

Request for close table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cheque_additional_info** | [**TransportDeliveriesCommonChequeAdditionalInfo**](TransportDeliveriesCommonChequeAdditionalInfo.md) | Cheque additional information according to russian federal law #54. | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **str** | Order ID. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_close_table_order_request import TransportDeliveriesRequestCloseTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCloseTableOrderRequest from a JSON string
transport_deliveries_request_close_table_order_request_instance = TransportDeliveriesRequestCloseTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCloseTableOrderRequest.to_json())

# convert the object into a dict
transport_deliveries_request_close_table_order_request_dict = transport_deliveries_request_close_table_order_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestCloseTableOrderRequest from a dict
transport_deliveries_request_close_table_order_request_from_dict = TransportDeliveriesRequestCloseTableOrderRequest.from_dict(transport_deliveries_request_close_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


