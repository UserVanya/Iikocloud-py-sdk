# OrdersCommonAddOrderPaymentsRequest

Request for add order payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID. | 
**tips** | [**List[DeliveriesRequestCreateOrderTipsPayment]**](DeliveriesRequestCreateOrderTipsPayment.md) | Order tips. | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**payments** | [**List[DeliveriesRequestCreateOrderPayment]**](DeliveriesRequestCreateOrderPayment.md) | Order payments. | 

## Example

```python
from iikocloud_client.models.orders_common_add_order_payments_request import OrdersCommonAddOrderPaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersCommonAddOrderPaymentsRequest from a JSON string
orders_common_add_order_payments_request_instance = OrdersCommonAddOrderPaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersCommonAddOrderPaymentsRequest.to_json())

# convert the object into a dict
orders_common_add_order_payments_request_dict = orders_common_add_order_payments_request_instance.to_dict()
# create an instance of OrdersCommonAddOrderPaymentsRequest from a dict
orders_common_add_order_payments_request_from_dict = OrdersCommonAddOrderPaymentsRequest.from_dict(orders_common_add_order_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


