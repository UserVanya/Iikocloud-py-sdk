# ReservesAddOrderPaymentsToBanquetRequest

Request for add order payments to banquet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserve_id** | **UUID** | Reserve ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**payments** | [**List[DeliveriesRequestCreateOrderPayment]**](DeliveriesRequestCreateOrderPayment.md) | Order payments. | 

## Example

```python
from iikocloud_client.models.reserves_add_order_payments_to_banquet_request import ReservesAddOrderPaymentsToBanquetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesAddOrderPaymentsToBanquetRequest from a JSON string
reserves_add_order_payments_to_banquet_request_instance = ReservesAddOrderPaymentsToBanquetRequest.from_json(json)
# print the JSON string representation of the object
print(ReservesAddOrderPaymentsToBanquetRequest.to_json())

# convert the object into a dict
reserves_add_order_payments_to_banquet_request_dict = reserves_add_order_payments_to_banquet_request_instance.to_dict()
# create an instance of ReservesAddOrderPaymentsToBanquetRequest from a dict
reserves_add_order_payments_to_banquet_request_from_dict = ReservesAddOrderPaymentsToBanquetRequest.from_dict(reserves_add_order_payments_to_banquet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


