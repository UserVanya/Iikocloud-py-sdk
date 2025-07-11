# TransportItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_sizes** | [**List[TransportItemSizeDto]**](TransportItemSizeDto.md) |  | [optional] 
**sku** | **str** | Product code | [optional] 
**name** | **str** | Product name | [optional] 
**description** | **str** | Product description | [optional] 
**allergen_groups** | [**List[AllergenGroupDto]**](AllergenGroupDto.md) |  | [optional] 
**item_id** | **str** | Product ID | [optional] 
**modifier_schema_id** | **str** | Modifier schema ID | [optional] 
**tax_category** | [**TaxCategoryDto**](TaxCategoryDto.md) |  | [optional] 
**order_item_type** | **str** | Product or compound. Depends on modifiers scheme existence | [optional] 

## Example

```python
from iikocloud_client.models.transport_item_dto import TransportItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransportItemDto from a JSON string
transport_item_dto_instance = TransportItemDto.from_json(json)
# print the JSON string representation of the object
print(TransportItemDto.to_json())

# convert the object into a dict
transport_item_dto_dict = transport_item_dto_instance.to_dict()
# create an instance of TransportItemDto from a dict
transport_item_dto_from_dict = TransportItemDto.from_dict(transport_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


