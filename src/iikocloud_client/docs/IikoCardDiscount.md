# IikoCardDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_items** | [**List[IikoCardDiscountItem]**](IikoCardDiscountItem.md) | Discount information for order items. | 
**program_id** | **UUID** | Card program ID. | 
**program_name** | **str** | Card program name. | 

## Example

```python
from iikocloud_client.models.iiko_card_discount import IikoCardDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of IikoCardDiscount from a JSON string
iiko_card_discount_instance = IikoCardDiscount.from_json(json)
# print the JSON string representation of the object
print(IikoCardDiscount.to_json())

# convert the object into a dict
iiko_card_discount_dict = iiko_card_discount_instance.to_dict()
# create an instance of IikoCardDiscount from a dict
iiko_card_discount_from_dict = IikoCardDiscount.from_dict(iiko_card_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


