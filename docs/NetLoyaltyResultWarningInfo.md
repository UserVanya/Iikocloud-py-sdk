# NetLoyaltyResultWarningInfo

Warning info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of an error. Can be null. | [optional] 
**error_code** | **str** | Error code. Can be null. | [optional] 
**message** | **str** | Description of an error. Can be null. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_warning_info import NetLoyaltyResultWarningInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultWarningInfo from a JSON string
net_loyalty_result_warning_info_instance = NetLoyaltyResultWarningInfo.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultWarningInfo.to_json())

# convert the object into a dict
net_loyalty_result_warning_info_dict = net_loyalty_result_warning_info_instance.to_dict()
# create an instance of NetLoyaltyResultWarningInfo from a dict
net_loyalty_result_warning_info_from_dict = NetLoyaltyResultWarningInfo.from_dict(net_loyalty_result_warning_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


