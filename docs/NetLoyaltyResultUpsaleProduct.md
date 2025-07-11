# NetLoyaltyResultUpsaleProduct

Product that suggested to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of product. | [optional] 
**code** | **str** | Code of product. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_upsale_product import NetLoyaltyResultUpsaleProduct

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultUpsaleProduct from a JSON string
net_loyalty_result_upsale_product_instance = NetLoyaltyResultUpsaleProduct.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultUpsaleProduct.to_json())

# convert the object into a dict
net_loyalty_result_upsale_product_dict = net_loyalty_result_upsale_product_instance.to_dict()
# create an instance of NetLoyaltyResultUpsaleProduct from a dict
net_loyalty_result_upsale_product_from_dict = NetLoyaltyResultUpsaleProduct.from_dict(net_loyalty_result_upsale_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


