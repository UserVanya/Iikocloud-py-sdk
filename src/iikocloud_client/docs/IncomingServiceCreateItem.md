# IncomingServiceCreateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Product quantity | 
**num** | **int** | Item sequence number | 
**price** | **float** | Price including VAT. Required if sum is not specified | [optional] 
**product** | **str** | Product identifier (GUID) | 
**revenue_account** | **str** | Revenue account identifier (GUID) | 
**split_vat** | **bool** | Split VAT accounting flag | [optional] 
**sum** | **float** | Amount including VAT. Required if price is not specified | [optional] 
**vat_percent** | **float** | VAT percentage | 

## Example

```python
from iikocloud_client.models.incoming_service_create_item import IncomingServiceCreateItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingServiceCreateItem from a JSON string
incoming_service_create_item_instance = IncomingServiceCreateItem.from_json(json)
# print the JSON string representation of the object
print(IncomingServiceCreateItem.to_json())

# convert the object into a dict
incoming_service_create_item_dict = incoming_service_create_item_instance.to_dict()
# create an instance of IncomingServiceCreateItem from a dict
incoming_service_create_item_from_dict = IncomingServiceCreateItem.from_dict(incoming_service_create_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


