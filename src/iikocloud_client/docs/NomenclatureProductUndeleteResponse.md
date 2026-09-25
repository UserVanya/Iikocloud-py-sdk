# NomenclatureProductUndeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message confirming successful restoration | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_undelete_response import NomenclatureProductUndeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductUndeleteResponse from a JSON string
nomenclature_product_undelete_response_instance = NomenclatureProductUndeleteResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductUndeleteResponse.to_json())

# convert the object into a dict
nomenclature_product_undelete_response_dict = nomenclature_product_undelete_response_instance.to_dict()
# create an instance of NomenclatureProductUndeleteResponse from a dict
nomenclature_product_undelete_response_from_dict = NomenclatureProductUndeleteResponse.from_dict(nomenclature_product_undelete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


