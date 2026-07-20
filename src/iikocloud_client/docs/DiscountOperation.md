# DiscountOperation

Discount operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount. | [optional] 
**code** | [**OperationCode**](OperationCode.md) | Operation Type Code.  &lt;br&gt;0 - fixed discount for the entire order,&lt;br /&gt;1 - fixed discount for the item,&lt;br /&gt;2 - free product,&lt;br /&gt;3 - other type of discounts. | [optional] 
**comment** | **str** | Comment. Can be null. | [optional] 
**discount_sum** | **float** | Discount sum. | [optional] 
**order_item_id** | **UUID** | Deprecated, use positionId. | [optional] 
**position_id** | **UUID** | Id of item the discount is applied to. If null - discount applied to whole orders. | [optional] 

## Example

```python
from iikocloud_client.models.discount_operation import DiscountOperation

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountOperation from a JSON string
discount_operation_instance = DiscountOperation.from_json(json)
# print the JSON string representation of the object
print(DiscountOperation.to_json())

# convert the object into a dict
discount_operation_dict = discount_operation_instance.to_dict()
# create an instance of DiscountOperation from a dict
discount_operation_from_dict = DiscountOperation.from_dict(discount_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


