# AddOrderPaymentsToBanquetRequest

Request for add order payments to banquet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**payments** | [**List[Payment]**](Payment.md) | Order payments. | 
**reserve_id** | **UUID** | Reserve ID. | 

## Example

```python
from iikocloud_client.models.add_order_payments_to_banquet_request import AddOrderPaymentsToBanquetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOrderPaymentsToBanquetRequest from a JSON string
add_order_payments_to_banquet_request_instance = AddOrderPaymentsToBanquetRequest.from_json(json)
# print the JSON string representation of the object
print(AddOrderPaymentsToBanquetRequest.to_json())

# convert the object into a dict
add_order_payments_to_banquet_request_dict = add_order_payments_to_banquet_request_instance.to_dict()
# create an instance of AddOrderPaymentsToBanquetRequest from a dict
add_order_payments_to_banquet_request_from_dict = AddOrderPaymentsToBanquetRequest.from_dict(add_order_payments_to_banquet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


