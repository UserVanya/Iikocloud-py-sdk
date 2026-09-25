# AmountUnitListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[AmountUnitFilter]**](AmountUnitFilter.md) | Request filters. All filters are applied simultaneously (AND). See the method description for the list of supported filter fields | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 

## Example

```python
from iikocloud_client.models.amount_unit_list_request import AmountUnitListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AmountUnitListRequest from a JSON string
amount_unit_list_request_instance = AmountUnitListRequest.from_json(json)
# print the JSON string representation of the object
print(AmountUnitListRequest.to_json())

# convert the object into a dict
amount_unit_list_request_dict = amount_unit_list_request_instance.to_dict()
# create an instance of AmountUnitListRequest from a dict
amount_unit_list_request_from_dict = AmountUnitListRequest.from_dict(amount_unit_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


