# NetLoyaltyResultFreeProduct

Free item to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of product. | [optional] 
**code** | **str** | Code of product. Can be null. | [optional] 
**size** | **List[str]** | Sizes available for that product. | [optional] 
**sizes** | [**List[NetLoyaltyResultFreeProductSize]**](NetLoyaltyResultFreeProductSize.md) | Sizes with IDs available for that product. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_free_product import NetLoyaltyResultFreeProduct

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultFreeProduct from a JSON string
net_loyalty_result_free_product_instance = NetLoyaltyResultFreeProduct.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultFreeProduct.to_json())

# convert the object into a dict
net_loyalty_result_free_product_dict = net_loyalty_result_free_product_instance.to_dict()
# create an instance of NetLoyaltyResultFreeProduct from a dict
net_loyalty_result_free_product_from_dict = NetLoyaltyResultFreeProduct.from_dict(net_loyalty_result_free_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


