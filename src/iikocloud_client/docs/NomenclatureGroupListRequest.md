# NomenclatureGroupListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[NomenclatureGroupV2Filter]**](NomenclatureGroupV2Filter.md) | Request filters. All filters are applied simultaneously (AND). See the method description for the list of supported filter fields | 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | 

## Example

```python
from iikocloud_client.models.nomenclature_group_list_request import NomenclatureGroupListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupListRequest from a JSON string
nomenclature_group_list_request_instance = NomenclatureGroupListRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupListRequest.to_json())

# convert the object into a dict
nomenclature_group_list_request_dict = nomenclature_group_list_request_instance.to_dict()
# create an instance of NomenclatureGroupListRequest from a dict
nomenclature_group_list_request_from_dict = NomenclatureGroupListRequest.from_dict(nomenclature_group_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


