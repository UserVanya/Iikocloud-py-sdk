# DeliveryRestrictionsHousesRange

Range of house numbers in the delivery zone.  It can work in two modes:  a) HousesRangeType.SpecificNumbers - list of house numbers. If the house is on this list - it is in the range  b) Rest HousesRangeType. Defines a range of numbers from StartingNumber to MaxNumber.  Since it is necessary to compare numbers - only supports numeric house numbers.  Type determines the admissibility of even/odd numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DeliveryRestrictionsHousesRangeType**](DeliveryRestrictionsHousesRangeType.md) | Type of house number range. | 
**starting_number** | **int** | Starting house number. | 
**max_number** | **int** | Maximum house number. | 
**is_unlimited_range** | **bool** | Unlimited range. | 
**specific_numbers** | **List[str]** | Specific numbers. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_houses_range import DeliveryRestrictionsHousesRange

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsHousesRange from a JSON string
delivery_restrictions_houses_range_instance = DeliveryRestrictionsHousesRange.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsHousesRange.to_json())

# convert the object into a dict
delivery_restrictions_houses_range_dict = delivery_restrictions_houses_range_instance.to_dict()
# create an instance of DeliveryRestrictionsHousesRange from a dict
delivery_restrictions_houses_range_from_dict = DeliveryRestrictionsHousesRange.from_dict(delivery_restrictions_houses_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


