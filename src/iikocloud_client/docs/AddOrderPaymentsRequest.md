# AddOrderPaymentsRequest

Request for add order payments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**payments** | [**List[Payment]**](Payment.md) | Order payments. | 
**tips** | [**List[TipsPayment]**](TipsPayment.md) | Order tips. | [optional] 

## Example

```python
from iikocloud_client.models.add_order_payments_request import AddOrderPaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOrderPaymentsRequest from a JSON string
add_order_payments_request_instance = AddOrderPaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(AddOrderPaymentsRequest.to_json())

# convert the object into a dict
add_order_payments_request_dict = add_order_payments_request_instance.to_dict()
# create an instance of AddOrderPaymentsRequest from a dict
add_order_payments_request_from_dict = AddOrderPaymentsRequest.from_dict(add_order_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


