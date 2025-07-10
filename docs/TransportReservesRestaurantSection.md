# TransportReservesRestaurantSection

Restaurant section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Restaurant section ID. | 
**terminal_group_id** | **str** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**name** | **str** | Name. | 
**tables** | [**List[TransportReservesTable]**](TransportReservesTable.md) | Tables. | 
**var_schema** | [**TransportReservesSectionSchema**](TransportReservesSectionSchema.md) | Table layout. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_reserves_restaurant_section import TransportReservesRestaurantSection

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesRestaurantSection from a JSON string
transport_reserves_restaurant_section_instance = TransportReservesRestaurantSection.from_json(json)
# print the JSON string representation of the object
print(TransportReservesRestaurantSection.to_json())

# convert the object into a dict
transport_reserves_restaurant_section_dict = transport_reserves_restaurant_section_instance.to_dict()
# create an instance of TransportReservesRestaurantSection from a dict
transport_reserves_restaurant_section_from_dict = TransportReservesRestaurantSection.from_dict(transport_reserves_restaurant_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


