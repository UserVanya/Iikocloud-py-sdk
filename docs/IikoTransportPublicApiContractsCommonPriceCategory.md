# IikoTransportPublicApiContractsCommonPriceCategory

Price category of the order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id of price category. | 
**name** | **str** | Name of price category. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_common_price_category import IikoTransportPublicApiContractsCommonPriceCategory

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsCommonPriceCategory from a JSON string
iiko_transport_public_api_contracts_common_price_category_instance = IikoTransportPublicApiContractsCommonPriceCategory.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsCommonPriceCategory.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_common_price_category_dict = iiko_transport_public_api_contracts_common_price_category_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsCommonPriceCategory from a dict
iiko_transport_public_api_contracts_common_price_category_from_dict = IikoTransportPublicApiContractsCommonPriceCategory.from_dict(iiko_transport_public_api_contracts_common_price_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


