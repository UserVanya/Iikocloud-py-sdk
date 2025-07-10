# TransportDeliveryRestrictionsHousesRange

Range of house numbers in the delivery zone.  It can work in two modes:  a) HousesRangeType.SpecificNumbers - list of house numbers. If the house is on this list - it is in the range  b) Rest HousesRangeType. Defines a range of numbers from StartingNumber to MaxNumber.  Since it is necessary to compare numbers - only supports numeric house numbers.  Type determines the admissibility of even/odd numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TransportDeliveryRestrictionsHousesRangeType**](TransportDeliveryRestrictionsHousesRangeType.md) | Type of house number range. | 
**starting_number** | **int** | Starting house number. | 
**max_number** | **int** | Maximum house number. | 
**is_unlimited_range** | **bool** | Unlimited range. | 
**specific_numbers** | **List[str]** | Specific numbers. | 

## Example

```python
from iiko_cloud_client.models.transport_delivery_restrictions_houses_range import TransportDeliveryRestrictionsHousesRange

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsHousesRange from a JSON string
transport_delivery_restrictions_houses_range_instance = TransportDeliveryRestrictionsHousesRange.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsHousesRange.to_json())

# convert the object into a dict
transport_delivery_restrictions_houses_range_dict = transport_delivery_restrictions_houses_range_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsHousesRange from a dict
transport_delivery_restrictions_houses_range_from_dict = TransportDeliveryRestrictionsHousesRange.from_dict(transport_delivery_restrictions_houses_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


