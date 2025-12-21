# IikoTransportPublicApiContractsDeliveryRestrictionsHousesRange

Range of house numbers in the delivery zone.  It can work in two modes:  a) HousesRangeType.SpecificNumbers - list of house numbers. If the house is on this list - it is in the range  b) Rest HousesRangeType. Defines a range of numbers from StartingNumber to MaxNumber.  Since it is necessary to compare numbers - only supports numeric house numbers.  Type determines the admissibility of even/odd numbers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**IikoTransportPublicApiContractsDeliveryRestrictionsHousesRangeType**](IikoTransportPublicApiContractsDeliveryRestrictionsHousesRangeType.md) | Type of house number range. | 
**starting_number** | **int** | Starting house number. | 
**max_number** | **int** | Maximum house number. | 
**is_unlimited_range** | **bool** | Unlimited range. | 
**specific_numbers** | **List[str]** | Specific numbers. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_houses_range import IikoTransportPublicApiContractsDeliveryRestrictionsHousesRange

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsHousesRange from a JSON string
iiko_transport_public_api_contracts_delivery_restrictions_houses_range_instance = IikoTransportPublicApiContractsDeliveryRestrictionsHousesRange.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveryRestrictionsHousesRange.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_delivery_restrictions_houses_range_dict = iiko_transport_public_api_contracts_delivery_restrictions_houses_range_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveryRestrictionsHousesRange from a dict
iiko_transport_public_api_contracts_delivery_restrictions_houses_range_from_dict = IikoTransportPublicApiContractsDeliveryRestrictionsHousesRange.from_dict(iiko_transport_public_api_contracts_delivery_restrictions_houses_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


