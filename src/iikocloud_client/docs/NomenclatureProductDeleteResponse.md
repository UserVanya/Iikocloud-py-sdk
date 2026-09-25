# NomenclatureProductDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message confirming successful deletion | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_delete_response import NomenclatureProductDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductDeleteResponse from a JSON string
nomenclature_product_delete_response_instance = NomenclatureProductDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductDeleteResponse.to_json())

# convert the object into a dict
nomenclature_product_delete_response_dict = nomenclature_product_delete_response_instance.to_dict()
# create an instance of NomenclatureProductDeleteResponse from a dict
nomenclature_product_delete_response_from_dict = NomenclatureProductDeleteResponse.from_dict(nomenclature_product_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


