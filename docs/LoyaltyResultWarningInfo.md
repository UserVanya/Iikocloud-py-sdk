# LoyaltyResultWarningInfo

Warning info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of an error. Can be null. | [optional] 
**error_code** | **str** | Error code. Can be null. | [optional] 
**message** | **str** | Description of an error. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_warning_info import LoyaltyResultWarningInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultWarningInfo from a JSON string
loyalty_result_warning_info_instance = LoyaltyResultWarningInfo.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultWarningInfo.to_json())

# convert the object into a dict
loyalty_result_warning_info_dict = loyalty_result_warning_info_instance.to_dict()
# create an instance of LoyaltyResultWarningInfo from a dict
loyalty_result_warning_info_from_dict = LoyaltyResultWarningInfo.from_dict(loyalty_result_warning_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


