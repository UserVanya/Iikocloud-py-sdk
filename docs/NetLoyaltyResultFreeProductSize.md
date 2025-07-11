# NetLoyaltyResultFreeProductSize

Free item size info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of size. | [optional] 
**name** | **str** | Name. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_free_product_size import NetLoyaltyResultFreeProductSize

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultFreeProductSize from a JSON string
net_loyalty_result_free_product_size_instance = NetLoyaltyResultFreeProductSize.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultFreeProductSize.to_json())

# convert the object into a dict
net_loyalty_result_free_product_size_dict = net_loyalty_result_free_product_size_instance.to_dict()
# create an instance of NetLoyaltyResultFreeProductSize from a dict
net_loyalty_result_free_product_size_from_dict = NetLoyaltyResultFreeProductSize.from_dict(net_loyalty_result_free_product_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


