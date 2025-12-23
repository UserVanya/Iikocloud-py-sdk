# CustomerCancelHoldMoneyRequest

Cancel hold money request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction id. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_cancel_hold_money_request import CustomerCancelHoldMoneyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerCancelHoldMoneyRequest from a JSON string
customer_cancel_hold_money_request_instance = CustomerCancelHoldMoneyRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerCancelHoldMoneyRequest.to_json())

# convert the object into a dict
customer_cancel_hold_money_request_dict = customer_cancel_hold_money_request_instance.to_dict()
# create an instance of CustomerCancelHoldMoneyRequest from a dict
customer_cancel_hold_money_request_from_dict = CustomerCancelHoldMoneyRequest.from_dict(customer_cancel_hold_money_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


