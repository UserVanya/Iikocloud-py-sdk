# DiscountType

Discount type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.discount_type import DiscountType

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountType from a JSON string
discount_type_instance = DiscountType.from_json(json)
# print the JSON string representation of the object
print(DiscountType.to_json())

# convert the object into a dict
discount_type_dict = discount_type_instance.to_dict()
# create an instance of DiscountType from a dict
discount_type_from_dict = DiscountType.from_dict(discount_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


