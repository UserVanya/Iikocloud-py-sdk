# IikoTransportPublicApiContractsDiscountsProductCategoryDiscount

Product category discount details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **UUID** | Category ID. | 
**category_name** | **str** | Category name. | 
**percent** | **float** | This category discount %. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_discounts_product_category_discount import IikoTransportPublicApiContractsDiscountsProductCategoryDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDiscountsProductCategoryDiscount from a JSON string
iiko_transport_public_api_contracts_discounts_product_category_discount_instance = IikoTransportPublicApiContractsDiscountsProductCategoryDiscount.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDiscountsProductCategoryDiscount.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_discounts_product_category_discount_dict = iiko_transport_public_api_contracts_discounts_product_category_discount_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDiscountsProductCategoryDiscount from a dict
iiko_transport_public_api_contracts_discounts_product_category_discount_from_dict = IikoTransportPublicApiContractsDiscountsProductCategoryDiscount.from_dict(iiko_transport_public_api_contracts_discounts_product_category_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


