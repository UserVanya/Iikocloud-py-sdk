# OutgoingServiceCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**discount_sum** | **float** | Discount amount | [optional] 
**num** | **int** | Item sequence number | 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**product** | **str** | Product identifier (GUID) | 
**revenue_account** | **str** | Revenue account identifier (GUID) | 
**split_vat** | **bool** | Split VAT accounting flag | [optional] 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**vat_percent** | **float** | VAT percentage | 

## Example

```python
from iikocloud_client.models.outgoing_service_create_item import OutgoingServiceCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingServiceCreateItem from a JSON string
outgoing_service_create_item_instance = OutgoingServiceCreateItem.from_json(json)
# print the JSON string representation of the object
print(OutgoingServiceCreateItem.to_json())

# convert the object into a dict
outgoing_service_create_item_dict = outgoing_service_create_item_instance.to_dict()
# create an instance of OutgoingServiceCreateItem from a dict
outgoing_service_create_item_from_dict = OutgoingServiceCreateItem.from_dict(outgoing_service_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


