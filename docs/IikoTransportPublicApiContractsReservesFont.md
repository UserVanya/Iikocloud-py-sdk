# IikoTransportPublicApiContractsReservesFont

Font.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_family** | **str** | Font family. | 
**size** | **float** | Font size. | 
**font_style** | [**IikoTransportPublicApiContractsReservesFontStyle**](IikoTransportPublicApiContractsReservesFontStyle.md) | Font style. May be multiple values. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_font import IikoTransportPublicApiContractsReservesFont

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsReservesFont from a JSON string
iiko_transport_public_api_contracts_reserves_font_instance = IikoTransportPublicApiContractsReservesFont.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsReservesFont.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_reserves_font_dict = iiko_transport_public_api_contracts_reserves_font_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsReservesFont from a dict
iiko_transport_public_api_contracts_reserves_font_from_dict = IikoTransportPublicApiContractsReservesFont.from_dict(iiko_transport_public_api_contracts_reserves_font_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


