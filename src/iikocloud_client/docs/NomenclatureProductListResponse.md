# NomenclatureProductListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NomenclatureProductResponse]**](NomenclatureProductResponse.md) | List of nomenclature items on the current page | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of nomenclature items matching the filters | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_list_response import NomenclatureProductListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductListResponse from a JSON string
nomenclature_product_list_response_instance = NomenclatureProductListResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductListResponse.to_json())

# convert the object into a dict
nomenclature_product_list_response_dict = nomenclature_product_list_response_instance.to_dict()
# create an instance of NomenclatureProductListResponse from a dict
nomenclature_product_list_response_from_dict = NomenclatureProductListResponse.from_dict(nomenclature_product_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


