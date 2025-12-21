# IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse

Get categories response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_categories** | [**List[IikoNetServiceContractsApiIikoTransportCustomerGuestCategoryShortInfo]**](IikoNetServiceContractsApiIikoTransportCustomerGuestCategoryShortInfo.md) | Guest categories for organization. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_get_categories_response import IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_get_categories_response_instance = IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_get_categories_response_dict = iiko_net_service_contracts_api_iiko_transport_customer_get_categories_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse from a dict
iiko_net_service_contracts_api_iiko_transport_customer_get_categories_response_from_dict = IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_get_categories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


