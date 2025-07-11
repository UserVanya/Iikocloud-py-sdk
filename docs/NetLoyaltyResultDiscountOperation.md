# NetLoyaltyResultDiscountOperation

Discount operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | [**NetLoyaltyResultOperationCode**](NetLoyaltyResultOperationCode.md) | Operation Type Code.  &lt;br&gt;0 - fixed discount for the entire order,&lt;br /&gt;1 - fixed discount for the item,&lt;br /&gt;2 - free product,&lt;br /&gt;3 - other type of discounts. | [optional] 
**order_item_id** | **str** | Deprecated, use positionId. | [optional] 
**position_id** | **str** | Id of item the discount is applied to. If null - discount applied to whole orders. | [optional] 
**discount_sum** | **float** | Discount sum. | [optional] 
**amount** | **float** | Amount. | [optional] 
**comment** | **str** | Comment. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_discount_operation import NetLoyaltyResultDiscountOperation

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultDiscountOperation from a JSON string
net_loyalty_result_discount_operation_instance = NetLoyaltyResultDiscountOperation.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultDiscountOperation.to_json())

# convert the object into a dict
net_loyalty_result_discount_operation_dict = net_loyalty_result_discount_operation_instance.to_dict()
# create an instance of NetLoyaltyResultDiscountOperation from a dict
net_loyalty_result_discount_operation_from_dict = NetLoyaltyResultDiscountOperation.from_dict(net_loyalty_result_discount_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


