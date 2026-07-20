# ChangeUserBalanceRequest

Change user balance request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment. Can be null. | [optional] 
**customer_id** | **UUID** | Customer id. | [optional] 
**organization_id** | **UUID** | Organization id. | 
**sum** | **float** | Sum of balance change. Must be positive. | [optional] 
**wallet_id** | **UUID** | Wallet id. | [optional] 

## Example

```python
from iikocloud_client.models.change_user_balance_request import ChangeUserBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeUserBalanceRequest from a JSON string
change_user_balance_request_instance = ChangeUserBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeUserBalanceRequest.to_json())

# convert the object into a dict
change_user_balance_request_dict = change_user_balance_request_instance.to_dict()
# create an instance of ChangeUserBalanceRequest from a dict
change_user_balance_request_from_dict = ChangeUserBalanceRequest.from_dict(change_user_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


