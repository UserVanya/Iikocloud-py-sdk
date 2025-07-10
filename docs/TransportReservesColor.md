# TransportReservesColor

Color.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a** | **int** | Alpha-component. | 
**r** | **int** | Red-component. | 
**g** | **int** | Green-component. | 
**b** | **int** | Blue-component. | 

## Example

```python
from iiko_cloud_client.models.transport_reserves_color import TransportReservesColor

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesColor from a JSON string
transport_reserves_color_instance = TransportReservesColor.from_json(json)
# print the JSON string representation of the object
print(TransportReservesColor.to_json())

# convert the object into a dict
transport_reserves_color_dict = transport_reserves_color_instance.to_dict()
# create an instance of TransportReservesColor from a dict
transport_reserves_color_from_dict = TransportReservesColor.from_dict(transport_reserves_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


