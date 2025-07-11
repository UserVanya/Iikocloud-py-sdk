# TransportReservesAddOrderPaymentsToBanquetRequest

Request for add order payments to banquet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reserve_id** | **str** | Reserve ID. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**payments** | [**List[TransportDeliveriesRequestCreateOrderPayment]**](TransportDeliveriesRequestCreateOrderPayment.md) | Order payments. | 

## Example

```python
from iikocloud_client.models.transport_reserves_add_order_payments_to_banquet_request import TransportReservesAddOrderPaymentsToBanquetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesAddOrderPaymentsToBanquetRequest from a JSON string
transport_reserves_add_order_payments_to_banquet_request_instance = TransportReservesAddOrderPaymentsToBanquetRequest.from_json(json)
# print the JSON string representation of the object
print(TransportReservesAddOrderPaymentsToBanquetRequest.to_json())

# convert the object into a dict
transport_reserves_add_order_payments_to_banquet_request_dict = transport_reserves_add_order_payments_to_banquet_request_instance.to_dict()
# create an instance of TransportReservesAddOrderPaymentsToBanquetRequest from a dict
transport_reserves_add_order_payments_to_banquet_request_from_dict = TransportReservesAddOrderPaymentsToBanquetRequest.from_dict(transport_reserves_add_order_payments_to_banquet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


