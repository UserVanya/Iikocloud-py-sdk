# HoldMoneyResponse

Hold money response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **UUID** | Holding money transaction id. | [optional] 

## Example

```python
from iikocloud_client.models.hold_money_response import HoldMoneyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HoldMoneyResponse from a JSON string
hold_money_response_instance = HoldMoneyResponse.from_json(json)
# print the JSON string representation of the object
print(HoldMoneyResponse.to_json())

# convert the object into a dict
hold_money_response_dict = hold_money_response_instance.to_dict()
# create an instance of HoldMoneyResponse from a dict
hold_money_response_from_dict = HoldMoneyResponse.from_dict(hold_money_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


