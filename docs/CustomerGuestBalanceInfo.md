# CustomerGuestBalanceInfo

Information about guest balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Wallet id. | [optional] 
**name** | **str** | Wallet name. | [optional] 
**type** | [**ProgramType**](ProgramType.md) | Wallet type.  &lt;br&gt;0 - deposit or corporate nutrition,&lt;br /&gt;1 - bonus program,&lt;br /&gt;2 - products program,&lt;br /&gt;3 - discount program,&lt;br /&gt;4 - certificate program. | [optional] 
**balance** | **float** | Wallet balance. | [optional] 

## Example

```python
from iikocloud_client.models.customer_guest_balance_info import CustomerGuestBalanceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGuestBalanceInfo from a JSON string
customer_guest_balance_info_instance = CustomerGuestBalanceInfo.from_json(json)
# print the JSON string representation of the object
print(CustomerGuestBalanceInfo.to_json())

# convert the object into a dict
customer_guest_balance_info_dict = customer_guest_balance_info_instance.to_dict()
# create an instance of CustomerGuestBalanceInfo from a dict
customer_guest_balance_info_from_dict = CustomerGuestBalanceInfo.from_dict(customer_guest_balance_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


