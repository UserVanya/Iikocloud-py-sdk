# CustomerHoldMoneyResponse

Hold money response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **UUID** | Holding money transaction id. | [optional] 

## Example

```python
from iikocloud_client.models.customer_hold_money_response import CustomerHoldMoneyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerHoldMoneyResponse from a JSON string
customer_hold_money_response_instance = CustomerHoldMoneyResponse.from_json(json)
# print the JSON string representation of the object
print(CustomerHoldMoneyResponse.to_json())

# convert the object into a dict
customer_hold_money_response_dict = customer_hold_money_response_instance.to_dict()
# create an instance of CustomerHoldMoneyResponse from a dict
customer_hold_money_response_from_dict = CustomerHoldMoneyResponse.from_dict(customer_hold_money_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


