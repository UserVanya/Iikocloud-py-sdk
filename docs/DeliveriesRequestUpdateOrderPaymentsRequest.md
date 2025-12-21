# DeliveriesRequestUpdateOrderPaymentsRequest

Request for order payment update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**order_id** | **UUID** | Order ID. | 
**payment_items** | [**List[DeliveriesRequestUpdateOrderOrderPaymentItem]**](DeliveriesRequestUpdateOrderOrderPaymentItem.md) | Payment details. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_update_order_payments_request import DeliveriesRequestUpdateOrderPaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestUpdateOrderPaymentsRequest from a JSON string
deliveries_request_update_order_payments_request_instance = DeliveriesRequestUpdateOrderPaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestUpdateOrderPaymentsRequest.to_json())

# convert the object into a dict
deliveries_request_update_order_payments_request_dict = deliveries_request_update_order_payments_request_instance.to_dict()
# create an instance of DeliveriesRequestUpdateOrderPaymentsRequest from a dict
deliveries_request_update_order_payments_request_from_dict = DeliveriesRequestUpdateOrderPaymentsRequest.from_dict(deliveries_request_update_order_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


