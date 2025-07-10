# NetCustomerChangeUserBalanceRequest

Change user balance request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Customer id. | [optional] 
**wallet_id** | **str** | Wallet id. | [optional] 
**sum** | **float** | Sum of balance change. Must be possible. | [optional] 
**comment** | **str** | Comment. Can be null. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iiko_cloud_client.models.net_customer_change_user_balance_request import NetCustomerChangeUserBalanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerChangeUserBalanceRequest from a JSON string
net_customer_change_user_balance_request_instance = NetCustomerChangeUserBalanceRequest.from_json(json)
# print the JSON string representation of the object
print(NetCustomerChangeUserBalanceRequest.to_json())

# convert the object into a dict
net_customer_change_user_balance_request_dict = net_customer_change_user_balance_request_instance.to_dict()
# create an instance of NetCustomerChangeUserBalanceRequest from a dict
net_customer_change_user_balance_request_from_dict = NetCustomerChangeUserBalanceRequest.from_dict(net_customer_change_user_balance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


