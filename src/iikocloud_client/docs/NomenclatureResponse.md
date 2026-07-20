# NomenclatureResponse

Response with stock lists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**groups** | [**List[ProductsGroupInfo]**](ProductsGroupInfo.md) | Stock list group. | 
**product_categories** | [**List[ProductCategoryInfo]**](ProductCategoryInfo.md) | Menu item category. | 
**products** | [**List[ProductInfo]**](ProductInfo.md) | Menu items and modifiers. | 
**revision** | **int** | The revison (version) of the menu recevied in the response of the request.  This value should be saved by the integration and passed in the &#x60;startRevision&#x60; field  of the next menu request. If the values in &#x60;revision&#x60; and &#x60;startRevision&#x60; are the same,  it means there have been no changes to the menu since the previous request.  In this case, the &#x60;groups&#x60;, &#x60;productCategories&#x60;, &#x60;products&#x60; and &#x60;sizes&#x60; fields  will not contain any data. | 
**sizes** | [**List[Size]**](Size.md) | Item sizes. | 

## Example

```python
from iikocloud_client.models.nomenclature_response import NomenclatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureResponse from a JSON string
nomenclature_response_instance = NomenclatureResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureResponse.to_json())

# convert the object into a dict
nomenclature_response_dict = nomenclature_response_instance.to_dict()
# create an instance of NomenclatureResponse from a dict
nomenclature_response_from_dict = NomenclatureResponse.from_dict(nomenclature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


