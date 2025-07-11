# TransportDeliveriesCommonCoordinates

Coordinate details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_common_coordinates import TransportDeliveriesCommonCoordinates

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesCommonCoordinates from a JSON string
transport_deliveries_common_coordinates_instance = TransportDeliveriesCommonCoordinates.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesCommonCoordinates.to_json())

# convert the object into a dict
transport_deliveries_common_coordinates_dict = transport_deliveries_common_coordinates_instance.to_dict()
# create an instance of TransportDeliveriesCommonCoordinates from a dict
transport_deliveries_common_coordinates_from_dict = TransportDeliveriesCommonCoordinates.from_dict(transport_deliveries_common_coordinates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


