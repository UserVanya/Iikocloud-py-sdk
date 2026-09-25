# PriceListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowable_price_deviation** | **float** | Allowable price deviation | [optional] 
**container_id** | **str** | Container/packaging identifier (GUID) | [optional] 
**native_product_code** | **str** | Our product code | [optional] 
**native_product_id** | **str** | Our product identifier (GUID) matched to the supplier product | [optional] 
**native_product_name** | **str** | Our product name | [optional] 
**native_product_num** | **str** | Our product article/number | [optional] 
**price** | **float** | Purchase price | [optional] 
**supplier_product_code** | **str** | Supplier product code | [optional] 
**supplier_product_id** | **str** | Supplier product identifier (GUID) | [optional] 
**supplier_product_name** | **str** | Supplier product name | [optional] 
**supplier_product_num** | **str** | Supplier product article/number | [optional] 

## Example

```python
from iikocloud_client.models.price_list_item import PriceListItem

# TODO update the JSON string below
json = "{}"
# create an instance of PriceListItem from a JSON string
price_list_item_instance = PriceListItem.from_json(json)
# print the JSON string representation of the object
print(PriceListItem.to_json())

# convert the object into a dict
price_list_item_dict = price_list_item_instance.to_dict()
# create an instance of PriceListItem from a dict
price_list_item_from_dict = PriceListItem.from_dict(price_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


