# CorporationSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crm_id** | **str** | Corporation identifier in CRM as represented; null if not set | [optional] 
**currency** | **object** | Corporation currency settings in the structure received from internal API server; null if no settings | [optional] 
**default_deviation_action** | **str** | Action when the price deviates from the internal price list, if the supplier has no own price list: NOT_NOTIFY — do not warn, NOTIFY — warn, DISABLE — forbid posting, DISABLE_GREATER — forbid posting when the price is exceeded | [optional] 
**default_distribution_algorithm** | **str** | Default service cost distribution algorithm: DISTRIBUTION_BY_SUM — by amount, DISTRIBUTION_BY_AMOUNT — by quantity, DISTRIBUTION_NOT_SPECIFIED — not specified | [optional] 
**delete_zero_production_order_items** | **bool** | Flag for deleting items with zero quantity in internal production orders when saving | [optional] 
**deleted** | **bool** | Flag indicating that the corporation is logically deleted | [optional] 
**description** | **str** | Text description of the corporation; null if the description is not filled in | [optional] 
**document_settings** | **object** | Corporation document settings in the structure received from internal API server; null if no settings | [optional] 
**gln** | **str** | Global Location Number (GLN) of the corporation; null if the number is not set | [optional] 
**id** | **str** | Corporation entity identifier | [optional] 
**local_id** | **str** | Local corporation identifier; null if not set | [optional] 
**money_precision** | **int** | Number of decimal places to which internal API server rounds monetary values and monetary calculation results | [optional] 
**name** | **str** | Display name of the corporation; null if the name is not filled in | [optional] 
**parent** | **str** | Identifier of the parent entity; null if the corporation is a root entity | [optional] 
**personal_data_processing_settings** | **object** | Personal data processing and notification settings; null if no settings | [optional] 
**round_cost_for_guests** | **bool** | Flag for rounding the order cost to a whole number in favor of the guest | [optional] 
**round_price_per_unit_for_guests** | **bool** | Flag for rounding the unit price down | [optional] 
**vat_accounting** | **str** | VAT accounting mode in the price of incoming goods: VAT_INCLUDED_IN_PRICE — VAT included, VAT_NOT_INCLUDED_IN_PRICE — VAT not included | [optional] 

## Example

```python
from iikocloud_client.models.corporation_settings import CorporationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of CorporationSettings from a JSON string
corporation_settings_instance = CorporationSettings.from_json(json)
# print the JSON string representation of the object
print(CorporationSettings.to_json())

# convert the object into a dict
corporation_settings_dict = corporation_settings_instance.to_dict()
# create an instance of CorporationSettings from a dict
corporation_settings_from_dict = CorporationSettings.from_dict(corporation_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


