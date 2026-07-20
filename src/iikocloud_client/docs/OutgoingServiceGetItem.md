# OutgoingServiceGetItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | [optional] 
**discount_sum** | **float** | Discount amount | [optional] 
**num** | **int** | Item sequence number | [optional] 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**price_without_vat** | **float** | Price excluding VAT | [optional] 
**product** | **str** | Product identifier (GUID) | [optional] 
**product_article** | **str** | Nomenclature article | [optional] 
**revenue_account** | **str** | Revenue account identifier (GUID) | [optional] 
**split_vat** | **bool** | Split VAT accounting flag | [optional] 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**sum_without_vat** | **float** | Amount excluding VAT | [optional] 
**vat_percent** | **float** | VAT percentage | [optional] 

## Example

```python
from iikocloud_client.models.outgoing_service_get_item import OutgoingServiceGetItem

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingServiceGetItem from a JSON string
outgoing_service_get_item_instance = OutgoingServiceGetItem.from_json(json)
# print the JSON string representation of the object
print(OutgoingServiceGetItem.to_json())

# convert the object into a dict
outgoing_service_get_item_dict = outgoing_service_get_item_instance.to_dict()
# create an instance of OutgoingServiceGetItem from a dict
outgoing_service_get_item_from_dict = OutgoingServiceGetItem.from_dict(outgoing_service_get_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


