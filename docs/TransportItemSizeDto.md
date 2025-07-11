# TransportItemSizeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prices** | [**List[TransportPriceDto]**](TransportPriceDto.md) |  | [optional] 
**item_modifier_groups** | [**List[TransportModifierGroupDto]**](TransportModifierGroupDto.md) |  | [optional] 
**sku** | **str** | Unique size code, consists of the product code and the name of the size, if the product has one size, then the size code will be equal to the product code | [optional] 
**size_code** | **str** |  | [optional] 
**size_name** | **str** | Name of the product size, the name can be empty if there is only one size in the list | [optional] 
**is_default** | **bool** | Whether it is a default size of the product. If the product has one size, then the parameter will be true, if the product has several sizes, none of them can be default. | [optional] 
**portion_weight_grams** | **float** | Size&#39;s weight | [optional] 
**size_id** | **str** | ID size, can be empty if the default size is selected and it is the only size in the list | [optional] 
**nutrition_per_hundred_grams** | **object** |  | [optional] 
**button_image_url** | **str** | links to images | [optional] 
**button_image_cropped_url** | **List[str]** |  | [optional] 

## Example

```python
from iikocloud_client.models.transport_item_size_dto import TransportItemSizeDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransportItemSizeDto from a JSON string
transport_item_size_dto_instance = TransportItemSizeDto.from_json(json)
# print the JSON string representation of the object
print(TransportItemSizeDto.to_json())

# convert the object into a dict
transport_item_size_dto_dict = transport_item_size_dto_instance.to_dict()
# create an instance of TransportItemSizeDto from a dict
transport_item_size_dto_from_dict = TransportItemSizeDto.from_dict(transport_item_size_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


