# CustomerChangeUserBalanceRequest

Change user balance request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | [optional] 
**wallet_id** | **UUID** | Wallet id. | [optional] 
**sum** | **float** | Sum of balance change. Must be possible. | [optional] 
**comment** | **str** | Comment. Can be null. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_change_user_balance_request import CustomerChangeUserBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerChangeUserBalanceRequest from a JSON string
customer_change_user_balance_request_instance = CustomerChangeUserBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerChangeUserBalanceRequest.to_json())

# convert the object into a dict
customer_change_user_balance_request_dict = customer_change_user_balance_request_instance.to_dict()
# create an instance of CustomerChangeUserBalanceRequest from a dict
customer_change_user_balance_request_from_dict = CustomerChangeUserBalanceRequest.from_dict(customer_change_user_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


