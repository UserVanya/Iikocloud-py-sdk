# DiscountTypeListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NomenclatureDiscountType]**](NomenclatureDiscountType.md) | List of directory entries | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of directory entries | [optional] 

## Example

```python
from iikocloud_client.models.discount_type_list_response import DiscountTypeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountTypeListResponse from a JSON string
discount_type_list_response_instance = DiscountTypeListResponse.from_json(json)
# print the JSON string representation of the object
print(DiscountTypeListResponse.to_json())

# convert the object into a dict
discount_type_list_response_dict = discount_type_list_response_instance.to_dict()
# create an instance of DiscountTypeListResponse from a dict
discount_type_list_response_from_dict = DiscountTypeListResponse.from_dict(discount_type_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


