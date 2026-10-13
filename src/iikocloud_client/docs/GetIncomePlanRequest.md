# GetIncomePlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **date** | Period start date (inclusive) | 
**date_to** | **date** | Period end date (inclusive) | 
**organization_id** | **UUID** | Organization (department) identifier; used to resolve the plan | 

## Example

```python
from iikocloud_client.models.get_income_plan_request import GetIncomePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetIncomePlanRequest from a JSON string
get_income_plan_request_instance = GetIncomePlanRequest.from_json(json)
# print the JSON string representation of the object
print(GetIncomePlanRequest.to_json())

# convert the object into a dict
get_income_plan_request_dict = get_income_plan_request_instance.to_dict()
# create an instance of GetIncomePlanRequest from a dict
get_income_plan_request_from_dict = GetIncomePlanRequest.from_dict(get_income_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


