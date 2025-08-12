# TransportOrdersCommonAddOrderPaymentsRequest

Request for add order payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID. | 
**tips** | [**List[TransportDeliveriesRequestCreateOrderTipsPayment]**](TransportDeliveriesRequestCreateOrderTipsPayment.md) | Order tips. | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**payments** | [**List[TransportDeliveriesRequestCreateOrderPayment]**](TransportDeliveriesRequestCreateOrderPayment.md) | Order payments. | 

## Example

```python
from iikocloud_client.models.transport_orders_common_add_order_payments_request import TransportOrdersCommonAddOrderPaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportOrdersCommonAddOrderPaymentsRequest from a JSON string
transport_orders_common_add_order_payments_request_instance = TransportOrdersCommonAddOrderPaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportOrdersCommonAddOrderPaymentsRequest.to_json())

# convert the object into a dict
transport_orders_common_add_order_payments_request_dict = transport_orders_common_add_order_payments_request_instance.to_dict()
# create an instance of TransportOrdersCommonAddOrderPaymentsRequest from a dict
transport_orders_common_add_order_payments_request_from_dict = TransportOrdersCommonAddOrderPaymentsRequest.from_dict(transport_orders_common_add_order_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


