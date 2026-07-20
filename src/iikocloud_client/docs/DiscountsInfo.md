# DiscountsInfo

Information on discounts/surcharges to be applied to order.  <remarks>  Whether map or non-blank list of discounts must be set.  </remarks>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**DiscountCard**](DiscountCard.md) | Track of discount card to be applied to order. | [optional] 
**discounts** | [**List[Discount]**](Discount.md) | Discounts/surcharges.   &gt; Type **iikoCard** allowed from version &#x60;7.4.4&#x60;. | [optional] 
**fixed_loyalty_discounts** | **bool** | Whether loyalty discounts should be fixed. | [optional] 

## Example

```python
from iikocloud_client.models.discounts_info import DiscountsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountsInfo from a JSON string
discounts_info_instance = DiscountsInfo.from_json(json)
# print the JSON string representation of the object
print(DiscountsInfo.to_json())

# convert the object into a dict
discounts_info_dict = discounts_info_instance.to_dict()
# create an instance of DiscountsInfo from a dict
discounts_info_from_dict = DiscountsInfo.from_dict(discounts_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


