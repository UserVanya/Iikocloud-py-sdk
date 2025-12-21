# IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest

Change category for customer request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **UUID** | Customer id. | 
**category_id** | **UUID** | Guest category id. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request import IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request_instance = IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request_dict = iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest from a dict
iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request_from_dict = IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


