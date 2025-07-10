# TransportReservesRestaurantSectionTable

Restaurant section table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_id** | **str** | Table ID. | 
**x** | **int** | X coordinate of left point of item. | 
**y** | **int** | Y coordinate of top point of item. | 
**z** | **int** | Z-index of item. | 
**angle** | **float** | Item&#39;s angle of slope. | 
**width** | **int** | Item&#39;s width in px. | 
**height** | **int** | Item&#39;s height in px. | 

## Example

```python
from iiko_cloud_client.models.transport_reserves_restaurant_section_table import TransportReservesRestaurantSectionTable

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesRestaurantSectionTable from a JSON string
transport_reserves_restaurant_section_table_instance = TransportReservesRestaurantSectionTable.from_json(json)
# print the JSON string representation of the object
print(TransportReservesRestaurantSectionTable.to_json())

# convert the object into a dict
transport_reserves_restaurant_section_table_dict = transport_reserves_restaurant_section_table_instance.to_dict()
# create an instance of TransportReservesRestaurantSectionTable from a dict
transport_reserves_restaurant_section_table_from_dict = TransportReservesRestaurantSectionTable.from_dict(transport_reserves_restaurant_section_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


