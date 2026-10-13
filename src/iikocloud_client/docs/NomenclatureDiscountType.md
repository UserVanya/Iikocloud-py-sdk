# NomenclatureDiscountType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated** | **bool** | Whether the discount type is active | [optional] 
**apply_before_excluded_vat** | **bool** | Apply the discount before VAT is excluded | [optional] 
**apply_only_in_period** | **bool** | Apply only within the configured validity period | [optional] 
**can_apply_by_card_number** | **bool** | Whether the discount can be applied by card number | [optional] 
**created_at** | **datetime** | Date and time when the discount type was created. ISO 8601 | [optional] 
**deleted_date** | **datetime** | Date and time when the discount type was deleted. null if the type is not deleted. ISO 8601 | [optional] 
**discount_period** | **str** | Validity period of the discount/surcharge | [optional] 
**id** | **UUID** | UUID of the directory entry | [optional] 
**is_automatic** | **bool** | Whether the discount/surcharge is applied automatically | [optional] 
**is_card** | **bool** | Whether the discount/surcharge is card-based | [optional] 
**is_combinable** | **bool** | Whether the discount can be combined with other discounts | [optional] 
**is_confirmation_required** | **bool** | Whether confirmation is required to apply the discount/surcharge | [optional] 
**is_deleted** | **bool** | Whether the directory entry is deleted | [optional] 
**is_manual** | **bool** | Whether the discount/surcharge is applied manually | [optional] 
**last_modify_node** | **str** | Node where the discount type was last modified | [optional] 
**local_id** | **int** | Local identifier of the discount type in RMS | [optional] 
**match_period_for_each_dish** | **bool** | Whether the validity period is matched for each dish separately | [optional] 
**modified_at** | **datetime** | Date and time of the last modification. ISO 8601 | [optional] 
**name** | **str** | Name of the directory entry | [optional] 
**revision** | **int** | Discount type revision | [optional] 
**short_name** | **str** | Short name of the discount type | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_discount_type import NomenclatureDiscountType

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureDiscountType from a JSON string
nomenclature_discount_type_instance = NomenclatureDiscountType.from_json(json)
# print the JSON string representation of the object
print(NomenclatureDiscountType.to_json())

# convert the object into a dict
nomenclature_discount_type_dict = nomenclature_discount_type_instance.to_dict()
# create an instance of NomenclatureDiscountType from a dict
nomenclature_discount_type_from_dict = NomenclatureDiscountType.from_dict(nomenclature_discount_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


