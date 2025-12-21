# ReservesRestaurantSection

Restaurant section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Restaurant section ID. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**name** | **str** | Name. | 
**tables** | [**List[ReservesTable]**](ReservesTable.md) | Tables. | 
**var_schema** | [**ReservesSectionSchema**](ReservesSectionSchema.md) | Table layout. | [optional] 

## Example

```python
from iikocloud_client.models.reserves_restaurant_section import ReservesRestaurantSection

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesRestaurantSection from a JSON string
reserves_restaurant_section_instance = ReservesRestaurantSection.from_json(json)
# print the JSON string representation of the object
print(ReservesRestaurantSection.to_json())

# convert the object into a dict
reserves_restaurant_section_dict = reserves_restaurant_section_instance.to_dict()
# create an instance of ReservesRestaurantSection from a dict
reserves_restaurant_section_from_dict = ReservesRestaurantSection.from_dict(reserves_restaurant_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


