# NetLoyaltyResultFreeProductsGroup

Free item to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_action_id** | **str** | Id of action that caused the suggestion. | [optional] 
**description_for_user** | **str** | Description for user. Can be null. | [optional] 
**products** | [**List[NetLoyaltyResultFreeProduct]**](NetLoyaltyResultFreeProduct.md) | Products that should be added to order. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_free_products_group import NetLoyaltyResultFreeProductsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultFreeProductsGroup from a JSON string
net_loyalty_result_free_products_group_instance = NetLoyaltyResultFreeProductsGroup.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultFreeProductsGroup.to_json())

# convert the object into a dict
net_loyalty_result_free_products_group_dict = net_loyalty_result_free_products_group_instance.to_dict()
# create an instance of NetLoyaltyResultFreeProductsGroup from a dict
net_loyalty_result_free_products_group_from_dict = NetLoyaltyResultFreeProductsGroup.from_dict(net_loyalty_result_free_products_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


