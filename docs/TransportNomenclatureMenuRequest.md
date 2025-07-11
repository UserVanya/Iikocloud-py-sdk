# TransportNomenclatureMenuRequest

Request for menu by id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_menu_id** | **str** | External menu id                Can be obtained by &#x60;api/2/menu&#x60; operation. | 
**organization_ids** | **List[str]** | Organization IDs.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**price_category_id** | **str** | Price category id.                Can be obtained by &#x60;api/2/menu&#x60; operation. | [optional] 
**version** | **int** | Version of the result data model. | [optional] 
**language** | **str** | Language of the external menu. | [optional] 
**async_mode** | **bool** | Async Mode. | [optional] 
**start_revision** | **int** | Start revision. | [optional] 

## Example

```python
from iikocloud_client.models.transport_nomenclature_menu_request import TransportNomenclatureMenuRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNomenclatureMenuRequest from a JSON string
transport_nomenclature_menu_request_instance = TransportNomenclatureMenuRequest.from_json(json)
# print the JSON string representation of the object
print(TransportNomenclatureMenuRequest.to_json())

# convert the object into a dict
transport_nomenclature_menu_request_dict = transport_nomenclature_menu_request_instance.to_dict()
# create an instance of TransportNomenclatureMenuRequest from a dict
transport_nomenclature_menu_request_from_dict = TransportNomenclatureMenuRequest.from_dict(transport_nomenclature_menu_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


