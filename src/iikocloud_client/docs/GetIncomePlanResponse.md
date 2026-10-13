# GetIncomePlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IncomePlanItem]**](IncomePlanItem.md) | Daily planned values | [optional] 

## Example

```python
from iikocloud_client.models.get_income_plan_response import GetIncomePlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetIncomePlanResponse from a JSON string
get_income_plan_response_instance = GetIncomePlanResponse.from_json(json)
# print the JSON string representation of the object
print(GetIncomePlanResponse.to_json())

# convert the object into a dict
get_income_plan_response_dict = get_income_plan_response_instance.to_dict()
# create an instance of GetIncomePlanResponse from a dict
get_income_plan_response_from_dict = GetIncomePlanResponse.from_dict(get_income_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


