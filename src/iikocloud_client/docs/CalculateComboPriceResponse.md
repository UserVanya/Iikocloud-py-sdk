# CalculateComboPriceResponse

Calculate combo price response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incorrectly_filled_groups** | **List[UUID]** | Ids of incorrectly filled groups. If not empty - price will be 0. | [optional] 
**price** | **float** | Calculated price of combo item. | [optional] 

## Example

```python
from iikocloud_client.models.calculate_combo_price_response import CalculateComboPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateComboPriceResponse from a JSON string
calculate_combo_price_response_instance = CalculateComboPriceResponse.from_json(json)
# print the JSON string representation of the object
print(CalculateComboPriceResponse.to_json())

# convert the object into a dict
calculate_combo_price_response_dict = calculate_combo_price_response_instance.to_dict()
# create an instance of CalculateComboPriceResponse from a dict
calculate_combo_price_response_from_dict = CalculateComboPriceResponse.from_dict(calculate_combo_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


