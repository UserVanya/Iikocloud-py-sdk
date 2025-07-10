# TransportNomenclatureNomenclatureResponse

Response with stock lists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**groups** | [**List[TransportNomenclatureProductsGroupInfo]**](TransportNomenclatureProductsGroupInfo.md) | Stock list group. | 
**product_categories** | [**List[TransportNomenclatureProductCategoryInfo]**](TransportNomenclatureProductCategoryInfo.md) | Menu item category. | 
**products** | [**List[TransportNomenclatureProductInfo]**](TransportNomenclatureProductInfo.md) | Menu items and modifiers. | 
**sizes** | [**List[TransportNomenclatureSize]**](TransportNomenclatureSize.md) | Item sizes. | 
**revision** | **int** | The revison (version) of the menu recevied in the response of the request.  This value should be saved by the integration and passed in the &#x60;startRevision&#x60; field  of the next menu request. If the values in &#x60;revision&#x60; and &#x60;startRevision&#x60; are the same,  it means there have been no changes to the menu since the previous request.  In this case, the &#x60;groups&#x60;, &#x60;productCategories&#x60;, &#x60;products&#x60; and &#x60;sizes&#x60; fields  will not contain any data. | 

## Example

```python
from iiko_cloud_client.models.transport_nomenclature_nomenclature_response import TransportNomenclatureNomenclatureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNomenclatureNomenclatureResponse from a JSON string
transport_nomenclature_nomenclature_response_instance = TransportNomenclatureNomenclatureResponse.from_json(json)
# print the JSON string representation of the object
print(TransportNomenclatureNomenclatureResponse.to_json())

# convert the object into a dict
transport_nomenclature_nomenclature_response_dict = transport_nomenclature_nomenclature_response_instance.to_dict()
# create an instance of TransportNomenclatureNomenclatureResponse from a dict
transport_nomenclature_nomenclature_response_from_dict = TransportNomenclatureNomenclatureResponse.from_dict(transport_nomenclature_nomenclature_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


