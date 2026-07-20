# HousesRange

Range of house numbers in the delivery zone.  It can work in two modes:  a) HousesRangeType.SpecificNumbers - list of house numbers. If the house is on this list - it is in the range  b) Rest HousesRangeType. Defines a range of numbers from StartingNumber to MaxNumber.  Since it is necessary to compare numbers - only supports numeric house numbers.  Type determines the admissibility of even/odd numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_unlimited_range** | **bool** | Unlimited range. | 
**max_number** | **int** | Maximum house number. | 
**specific_numbers** | **List[str]** | Specific numbers. | 
**starting_number** | **int** | Starting house number. | 
**type** | [**HousesRangeType**](HousesRangeType.md) | Type of house number range. | 

## Example

```python
from iikocloud_client.models.houses_range import HousesRange

# TODO update the JSON string below
json = "{}"
# create an instance of HousesRange from a JSON string
houses_range_instance = HousesRange.from_json(json)
# print the JSON string representation of the object
print(HousesRange.to_json())

# convert the object into a dict
houses_range_dict = houses_range_instance.to_dict()
# create an instance of HousesRange from a dict
houses_range_from_dict = HousesRange.from_dict(houses_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


