# UpdateOrderPaymentsRequest

Request for order payment update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**payment_items** | [**List[OrderPaymentItem]**](OrderPaymentItem.md) | Payment details. | [optional] 

## Example

```python
from iikocloud_client.models.update_order_payments_request import UpdateOrderPaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderPaymentsRequest from a JSON string
update_order_payments_request_instance = UpdateOrderPaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderPaymentsRequest.to_json())

# convert the object into a dict
update_order_payments_request_dict = update_order_payments_request_instance.to_dict()
# create an instance of UpdateOrderPaymentsRequest from a dict
update_order_payments_request_from_dict = UpdateOrderPaymentsRequest.from_dict(update_order_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


