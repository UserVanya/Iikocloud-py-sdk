# AmountUnitListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AmountUnit]**](AmountUnit.md) | List of directory entries | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of directory entries | [optional] 

## Example

```python
from iikocloud_client.models.amount_unit_list_response import AmountUnitListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AmountUnitListResponse from a JSON string
amount_unit_list_response_instance = AmountUnitListResponse.from_json(json)
# print the JSON string representation of the object
print(AmountUnitListResponse.to_json())

# convert the object into a dict
amount_unit_list_response_dict = amount_unit_list_response_instance.to_dict()
# create an instance of AmountUnitListResponse from a dict
amount_unit_list_response_from_dict = AmountUnitListResponse.from_dict(amount_unit_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


