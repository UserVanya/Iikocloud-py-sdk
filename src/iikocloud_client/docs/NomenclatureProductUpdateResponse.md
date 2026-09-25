# NomenclatureProductUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message confirming successful update | [optional] 
**product_article** | **str** | Article of the updated product | [optional] 
**product_id** | **UUID** | UUID of the updated product | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_update_response import NomenclatureProductUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductUpdateResponse from a JSON string
nomenclature_product_update_response_instance = NomenclatureProductUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductUpdateResponse.to_json())

# convert the object into a dict
nomenclature_product_update_response_dict = nomenclature_product_update_response_instance.to_dict()
# create an instance of NomenclatureProductUpdateResponse from a dict
nomenclature_product_update_response_from_dict = NomenclatureProductUpdateResponse.from_dict(nomenclature_product_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


