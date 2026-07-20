# Price

Price per this item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_price** | **float** | Current price. | 
**is_included_in_menu** | **bool** | Is on the menu. | 
**next_date_price** | **str** | New price validity start date (Local for the terminal). | [optional] 
**next_included_in_menu** | **bool** | Will be on the menu in the future. | 
**next_price** | **float** | New price | [optional] 

## Example

```python
from iikocloud_client.models.price import Price

# TODO update the JSON string below
json = "{}"
# create an instance of Price from a JSON string
price_instance = Price.from_json(json)
# print the JSON string representation of the object
print(Price.to_json())

# convert the object into a dict
price_dict = price_instance.to_dict()
# create an instance of Price from a dict
price_from_dict = Price.from_dict(price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


