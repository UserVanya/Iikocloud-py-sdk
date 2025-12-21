# IikoTransportPublicApiContractsDiscountsDiscountsResponse

Response with list of discounts/surcharges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**discounts** | [**List[RmsItemsResponseWrapperDiscountsDiscountCardTypeInfo]**](RmsItemsResponseWrapperDiscountsDiscountCardTypeInfo.md) | List of discounts/surcharges. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_discounts_discounts_response import IikoTransportPublicApiContractsDiscountsDiscountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDiscountsDiscountsResponse from a JSON string
iiko_transport_public_api_contracts_discounts_discounts_response_instance = IikoTransportPublicApiContractsDiscountsDiscountsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDiscountsDiscountsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_discounts_discounts_response_dict = iiko_transport_public_api_contracts_discounts_discounts_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDiscountsDiscountsResponse from a dict
iiko_transport_public_api_contracts_discounts_discounts_response_from_dict = IikoTransportPublicApiContractsDiscountsDiscountsResponse.from_dict(iiko_transport_public_api_contracts_discounts_discounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


