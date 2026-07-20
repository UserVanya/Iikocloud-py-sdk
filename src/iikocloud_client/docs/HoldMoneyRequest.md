# HoldMoneyRequest

Hold money request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Additional information about holding. Can be null. | [optional] 
**customer_id** | **UUID** | Customer id. | 
**organization_id** | **UUID** | Organization id. | 
**sum** | **float** | Sum. | 
**transaction_id** | **UUID** | Predefined transaction id. Random if empty. | [optional] 
**wallet_id** | **UUID** | Wallet id. | 

## Example

```python
from iikocloud_client.models.hold_money_request import HoldMoneyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HoldMoneyRequest from a JSON string
hold_money_request_instance = HoldMoneyRequest.from_json(json)
# print the JSON string representation of the object
print(HoldMoneyRequest.to_json())

# convert the object into a dict
hold_money_request_dict = hold_money_request_instance.to_dict()
# create an instance of HoldMoneyRequest from a dict
hold_money_request_from_dict = HoldMoneyRequest.from_dict(hold_money_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


