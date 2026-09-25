# NomenclatureProductUndeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_ids** | **List[UUID]** | List of nomenclature product UUIDs to restore | 

## Example

```python
from iikocloud_client.models.nomenclature_product_undelete_request import NomenclatureProductUndeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductUndeleteRequest from a JSON string
nomenclature_product_undelete_request_instance = NomenclatureProductUndeleteRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductUndeleteRequest.to_json())

# convert the object into a dict
nomenclature_product_undelete_request_dict = nomenclature_product_undelete_request_instance.to_dict()
# create an instance of NomenclatureProductUndeleteRequest from a dict
nomenclature_product_undelete_request_from_dict = NomenclatureProductUndeleteRequest.from_dict(nomenclature_product_undelete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


