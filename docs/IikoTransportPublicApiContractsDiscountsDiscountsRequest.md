# IikoTransportPublicApiContractsDiscountsDiscountsRequest

Request of discounts/surcharges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organization IDs that require discounts return.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_discounts_discounts_request import IikoTransportPublicApiContractsDiscountsDiscountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDiscountsDiscountsRequest from a JSON string
iiko_transport_public_api_contracts_discounts_discounts_request_instance = IikoTransportPublicApiContractsDiscountsDiscountsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDiscountsDiscountsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_discounts_discounts_request_dict = iiko_transport_public_api_contracts_discounts_discounts_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDiscountsDiscountsRequest from a dict
iiko_transport_public_api_contracts_discounts_discounts_request_from_dict = IikoTransportPublicApiContractsDiscountsDiscountsRequest.from_dict(iiko_transport_public_api_contracts_discounts_discounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


