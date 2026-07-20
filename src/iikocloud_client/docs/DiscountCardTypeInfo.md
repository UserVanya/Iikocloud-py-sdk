# DiscountCardTypeInfo

Discount/surcharge DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_apply_by_card_number** | **bool** | Can be applied by card No.  &gt; If true, it&#39;s enough to enter discount card No. (card swiping not required) | 
**can_be_applied_selectively** | **bool** | Whether discount allows for selected application to individual items at user&#39;s discretion. | 
**comment** | **str** | Comment. | [optional] 
**id** | **UUID** | Discount ID in RMS. | 
**is_automatic** | **bool** | Created automatically. | 
**is_card** | **bool** | Executed by card. | 
**is_categorised_discount** | **bool** | Whether it is category discount or not.  &gt; If true, \&quot;productCategoryDiscounts\&quot; discounts will apply. | 
**is_deleted** | **bool** | IsDeleted. | [optional] 
**is_manual** | **bool** | Created manually. | 
**min_order_sum** | **float** | Minimum order amount required for discount application.  If order amount is less than specified threshold, discount does not apply. | [optional] 
**mode** | [**DiscountCardMode**](DiscountCardMode.md) | Discount type.     Can be obtained by &#x60;/api/1/discounts&#x60; operation. | 
**name** | **str** | Discount name. | 
**percent** | **float** | Total discount rate.  &gt; Ignored if \&quot;isCategorisedDiscount\&quot; specified. | 
**product_category_discounts** | [**List[ProductCategoryDiscount]**](ProductCategoryDiscount.md) | Category discount. | 
**sum** | **float** | Fixed amount.  &gt; Triggers if fixed amount has been specified. | 

## Example

```python
from iikocloud_client.models.discount_card_type_info import DiscountCardTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountCardTypeInfo from a JSON string
discount_card_type_info_instance = DiscountCardTypeInfo.from_json(json)
# print the JSON string representation of the object
print(DiscountCardTypeInfo.to_json())

# convert the object into a dict
discount_card_type_info_dict = discount_card_type_info_instance.to_dict()
# create an instance of DiscountCardTypeInfo from a dict
discount_card_type_info_from_dict = DiscountCardTypeInfo.from_dict(discount_card_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


