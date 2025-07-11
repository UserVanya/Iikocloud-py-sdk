# NetCustomerCancelHoldMoneyRequest

Cancel hold money request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Transaction id. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_customer_cancel_hold_money_request import NetCustomerCancelHoldMoneyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerCancelHoldMoneyRequest from a JSON string
net_customer_cancel_hold_money_request_instance = NetCustomerCancelHoldMoneyRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerCancelHoldMoneyRequest.to_json())

# convert the object into a dict
net_customer_cancel_hold_money_request_dict = net_customer_cancel_hold_money_request_instance.to_dict()
# create an instance of NetCustomerCancelHoldMoneyRequest from a dict
net_customer_cancel_hold_money_request_from_dict = NetCustomerCancelHoldMoneyRequest.from_dict(net_customer_cancel_hold_money_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


