# IikoTransportPublicApiContractsDiscountsDiscountCardTypeInfo

Discount/surcharge DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Discount ID in RMS. | 
**name** | **str** | Discount name. | 
**percent** | **float** | Total discount rate.  &gt; Ignored if \&quot;isCategorisedDiscount\&quot; specified. | 
**is_categorised_discount** | **bool** | Whether it is category discount or not.  &gt; If true, \&quot;productCategoryDiscounts\&quot; discounts will apply. | 
**product_category_discounts** | [**List[IikoTransportPublicApiContractsDiscountsProductCategoryDiscount]**](IikoTransportPublicApiContractsDiscountsProductCategoryDiscount.md) | Category discount. | 
**comment** | **str** | Comment. | [optional] 
**can_be_applied_selectively** | **bool** | Whether discount allows for selected application to individual items at user&#39;s discretion. | 
**min_order_sum** | **float** | Minimum order amount required for discount application.  If order amount is less than specified threshold, discount does not apply. | [optional] 
**mode** | [**IikoTransportPublicApiContractsDiscountsDiscountCardMode**](IikoTransportPublicApiContractsDiscountsDiscountCardMode.md) | Discount type.     Can be obtained by &#x60;/discounts&#x60; operation. | 
**sum** | **float** | Fixed amount.  &gt; Triggers if fixed amount has been specified. | 
**can_apply_by_card_number** | **bool** | Can be applied by card No.  &gt; If true, it&#39;s enough to enter discount card No. (card swiping not required) | 
**is_manual** | **bool** | Created manually. | 
**is_card** | **bool** | Executed by card. | 
**is_automatic** | **bool** | Created automatically. | 
**is_deleted** | **bool** | IsDeleted. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_discounts_discount_card_type_info import IikoTransportPublicApiContractsDiscountsDiscountCardTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDiscountsDiscountCardTypeInfo from a JSON string
iiko_transport_public_api_contracts_discounts_discount_card_type_info_instance = IikoTransportPublicApiContractsDiscountsDiscountCardTypeInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDiscountsDiscountCardTypeInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_discounts_discount_card_type_info_dict = iiko_transport_public_api_contracts_discounts_discount_card_type_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDiscountsDiscountCardTypeInfo from a dict
iiko_transport_public_api_contracts_discounts_discount_card_type_info_from_dict = IikoTransportPublicApiContractsDiscountsDiscountCardTypeInfo.from_dict(iiko_transport_public_api_contracts_discounts_discount_card_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


