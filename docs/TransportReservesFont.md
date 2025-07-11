# TransportReservesFont

Font.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_family** | **str** | Font family. | 
**size** | **float** | Font size. | 
**font_style** | [**TransportReservesFontStyle**](TransportReservesFontStyle.md) | Font style. May be multiple values. | 

## Example

```python
from iikocloud_client.models.transport_reserves_font import TransportReservesFont

# TODO update the JSON string below
json = "{}"
# create an instance of TransportReservesFont from a JSON string
transport_reserves_font_instance = TransportReservesFont.from_json(json)
# print the JSON string representation of the object
print(TransportReservesFont.to_json())

# convert the object into a dict
transport_reserves_font_dict = transport_reserves_font_instance.to_dict()
# create an instance of TransportReservesFont from a dict
transport_reserves_font_from_dict = TransportReservesFont.from_dict(transport_reserves_font_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


