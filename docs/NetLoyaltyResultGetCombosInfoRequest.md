# NetLoyaltyResultGetCombosInfoRequest

Get combos info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_data** | **bool** | Extra data. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_loyalty_result_get_combos_info_request import NetLoyaltyResultGetCombosInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultGetCombosInfoRequest from a JSON string
net_loyalty_result_get_combos_info_request_instance = NetLoyaltyResultGetCombosInfoRequest.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultGetCombosInfoRequest.to_json())

# convert the object into a dict
net_loyalty_result_get_combos_info_request_dict = net_loyalty_result_get_combos_info_request_instance.to_dict()
# create an instance of NetLoyaltyResultGetCombosInfoRequest from a dict
net_loyalty_result_get_combos_info_request_from_dict = NetLoyaltyResultGetCombosInfoRequest.from_dict(net_loyalty_result_get_combos_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


