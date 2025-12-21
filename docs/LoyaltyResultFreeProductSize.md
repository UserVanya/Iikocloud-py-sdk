# LoyaltyResultFreeProductSize

Free item size info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id of size. | [optional] 
**name** | **str** | Name. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_free_product_size import LoyaltyResultFreeProductSize

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultFreeProductSize from a JSON string
loyalty_result_free_product_size_instance = LoyaltyResultFreeProductSize.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultFreeProductSize.to_json())

# convert the object into a dict
loyalty_result_free_product_size_dict = loyalty_result_free_product_size_instance.to_dict()
# create an instance of LoyaltyResultFreeProductSize from a dict
loyalty_result_free_product_size_from_dict = LoyaltyResultFreeProductSize.from_dict(loyalty_result_free_product_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


