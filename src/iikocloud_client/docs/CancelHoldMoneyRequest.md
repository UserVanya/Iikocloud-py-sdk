# CancelHoldMoneyRequest

Cancel hold money request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | 
**transaction_id** | **UUID** | Transaction id. | 

## Example

```python
from iikocloud_client.models.cancel_hold_money_request import CancelHoldMoneyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelHoldMoneyRequest from a JSON string
cancel_hold_money_request_instance = CancelHoldMoneyRequest.from_json(json)
# print the JSON string representation of the object
print(CancelHoldMoneyRequest.to_json())

# convert the object into a dict
cancel_hold_money_request_dict = cancel_hold_money_request_instance.to_dict()
# create an instance of CancelHoldMoneyRequest from a dict
cancel_hold_money_request_from_dict = CancelHoldMoneyRequest.from_dict(cancel_hold_money_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


