# CustomerHoldMoneyRequest

Hold money request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | Predefined transaction id. Random if empty. | [optional] 
**customer_id** | **str** | Customer id. | 
**wallet_id** | **str** | Wallet id. | 
**sum** | **float** | Sum. | 
**comment** | **str** | Additional information about holding. Can be null. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.customer_hold_money_request import CustomerHoldMoneyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerHoldMoneyRequest from a JSON string
customer_hold_money_request_instance = CustomerHoldMoneyRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerHoldMoneyRequest.to_json())

# convert the object into a dict
customer_hold_money_request_dict = customer_hold_money_request_instance.to_dict()
# create an instance of CustomerHoldMoneyRequest from a dict
customer_hold_money_request_from_dict = CustomerHoldMoneyRequest.from_dict(customer_hold_money_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


