# AddressCity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doorphone** | **str** | Intercom. | [optional] 
**entrance** | **str** | Entrance. | [optional] 
**flat** | **str** | Apartment. | [optional] 
**floor** | **str** | Floor. | [optional] 
**line1** | **str** | Address line 1.  Contains the primary address information.   &gt; Allowed from version &#x60;8.7.6&#x60;. | 
**region_id** | **UUID** | Delivery area ID. | [optional] 

## Example

```python
from iikocloud_client.models.address_city import AddressCity

# TODO update the JSON string below
json = "{}"
# create an instance of AddressCity from a JSON string
address_city_instance = AddressCity.from_json(json)
# print the JSON string representation of the object
print(AddressCity.to_json())

# convert the object into a dict
address_city_dict = address_city_instance.to_dict()
# create an instance of AddressCity from a dict
address_city_from_dict = AddressCity.from_dict(address_city_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


