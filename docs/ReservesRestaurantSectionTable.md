# ReservesRestaurantSectionTable

Restaurant section table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **UUID** | Table ID. | 
**x** | **int** | X coordinate of left point of item. | 
**y** | **int** | Y coordinate of top point of item. | 
**z** | **int** | Z-index of item. | 
**angle** | **float** | Item&#39;s angle of slope. | 
**width** | **int** | Item&#39;s width in px. | 
**height** | **int** | Item&#39;s height in px. | 

## Example

```python
from iikocloud_client.models.reserves_restaurant_section_table import ReservesRestaurantSectionTable

# TODO update the JSON string below
json = "{}"
# create an instance of ReservesRestaurantSectionTable from a JSON string
reserves_restaurant_section_table_instance = ReservesRestaurantSectionTable.from_json(json)
# print the JSON string representation of the object
print(ReservesRestaurantSectionTable.to_json())

# convert the object into a dict
reserves_restaurant_section_table_dict = reserves_restaurant_section_table_instance.to_dict()
# create an instance of ReservesRestaurantSectionTable from a dict
reserves_restaurant_section_table_from_dict = ReservesRestaurantSectionTable.from_dict(reserves_restaurant_section_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


