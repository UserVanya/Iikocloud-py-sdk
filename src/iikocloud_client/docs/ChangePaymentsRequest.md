# ChangePaymentsRequest

Change order's payments request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**payments** | [**List[Payment]**](Payment.md) | Order payments. | 
**tips** | [**List[TipsPayment]**](TipsPayment.md) | Order tips. | [optional] 

## Example

```python
from iikocloud_client.models.change_payments_request import ChangePaymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePaymentsRequest from a JSON string
change_payments_request_instance = ChangePaymentsRequest.from_json(json)
# print the JSON string representation of the object
print(ChangePaymentsRequest.to_json())

# convert the object into a dict
change_payments_request_dict = change_payments_request_instance.to_dict()
# create an instance of ChangePaymentsRequest from a dict
change_payments_request_from_dict = ChangePaymentsRequest.from_dict(change_payments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


