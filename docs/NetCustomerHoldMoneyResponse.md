# NetCustomerHoldMoneyResponse

Hold money response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Holding money transaction id. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_customer_hold_money_response import NetCustomerHoldMoneyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerHoldMoneyResponse from a JSON string
net_customer_hold_money_response_instance = NetCustomerHoldMoneyResponse.from_json(json)
# print the JSON string representation of the object
print(NetCustomerHoldMoneyResponse.to_json())

# convert the object into a dict
net_customer_hold_money_response_dict = net_customer_hold_money_response_instance.to_dict()
# create an instance of NetCustomerHoldMoneyResponse from a dict
net_customer_hold_money_response_from_dict = NetCustomerHoldMoneyResponse.from_dict(net_customer_hold_money_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


