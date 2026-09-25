# NomenclatureProductCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message confirming successful creation | [optional] 
**product_article** | **str** | Article of the created product | [optional] 
**product_id** | **UUID** | UUID of the created product | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_create_response import NomenclatureProductCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductCreateResponse from a JSON string
nomenclature_product_create_response_instance = NomenclatureProductCreateResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductCreateResponse.to_json())

# convert the object into a dict
nomenclature_product_create_response_dict = nomenclature_product_create_response_instance.to_dict()
# create an instance of NomenclatureProductCreateResponse from a dict
nomenclature_product_create_response_from_dict = NomenclatureProductCreateResponse.from_dict(nomenclature_product_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


