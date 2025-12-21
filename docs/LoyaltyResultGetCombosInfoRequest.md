# LoyaltyResultGetCombosInfoRequest

Get combos info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_data** | **bool** | Extra data. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.loyalty_result_get_combos_info_request import LoyaltyResultGetCombosInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultGetCombosInfoRequest from a JSON string
loyalty_result_get_combos_info_request_instance = LoyaltyResultGetCombosInfoRequest.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultGetCombosInfoRequest.to_json())

# convert the object into a dict
loyalty_result_get_combos_info_request_dict = loyalty_result_get_combos_info_request_instance.to_dict()
# create an instance of LoyaltyResultGetCombosInfoRequest from a dict
loyalty_result_get_combos_info_request_from_dict = LoyaltyResultGetCombosInfoRequest.from_dict(loyalty_result_get_combos_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


