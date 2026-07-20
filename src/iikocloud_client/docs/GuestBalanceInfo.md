# GuestBalanceInfo

Information about guest balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | Wallet balance. | [optional] 
**id** | **UUID** | Wallet id. | [optional] 
**name** | **str** | Wallet name. | [optional] 
**type** | [**ProgramType**](ProgramType.md) | Wallet type.  &lt;br&gt;0 - deposit or corporate nutrition,&lt;br /&gt;1 - bonus program,&lt;br /&gt;2 - products program,&lt;br /&gt;3 - discount program,&lt;br /&gt;4 - certificate program. | [optional] 

## Example

```python
from iikocloud_client.models.guest_balance_info import GuestBalanceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GuestBalanceInfo from a JSON string
guest_balance_info_instance = GuestBalanceInfo.from_json(json)
# print the JSON string representation of the object
print(GuestBalanceInfo.to_json())

# convert the object into a dict
guest_balance_info_dict = guest_balance_info_instance.to_dict()
# create an instance of GuestBalanceInfo from a dict
guest_balance_info_from_dict = GuestBalanceInfo.from_dict(guest_balance_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


