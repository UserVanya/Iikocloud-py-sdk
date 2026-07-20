# CalculateComboPriceRequest

Calculate combo price request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DeliveryOrderCreateItem]**](DeliveryOrderCreateItem.md) | Items with modifiers included in combo. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.calculate_combo_price_request import CalculateComboPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateComboPriceRequest from a JSON string
calculate_combo_price_request_instance = CalculateComboPriceRequest.from_json(json)
# print the JSON string representation of the object
print(CalculateComboPriceRequest.to_json())

# convert the object into a dict
calculate_combo_price_request_dict = calculate_combo_price_request_instance.to_dict()
# create an instance of CalculateComboPriceRequest from a dict
calculate_combo_price_request_from_dict = CalculateComboPriceRequest.from_dict(calculate_combo_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


