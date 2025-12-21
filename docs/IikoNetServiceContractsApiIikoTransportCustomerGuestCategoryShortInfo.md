# IikoNetServiceContractsApiIikoTransportCustomerGuestCategoryShortInfo

Guest category info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Category id. | [optional] 
**name** | **str** | Category name. | [optional] 
**is_active** | **bool** | Is category active or not. | [optional] 
**is_default_for_new_guests** | **bool** | Is category default for new guests or not. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_guest_category_short_info import IikoNetServiceContractsApiIikoTransportCustomerGuestCategoryShortInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGuestCategoryShortInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_guest_category_short_info_instance = IikoNetServiceContractsApiIikoTransportCustomerGuestCategoryShortInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerGuestCategoryShortInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_guest_category_short_info_dict = iiko_net_service_contracts_api_iiko_transport_customer_guest_category_short_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerGuestCategoryShortInfo from a dict
iiko_net_service_contracts_api_iiko_transport_customer_guest_category_short_info_from_dict = IikoNetServiceContractsApiIikoTransportCustomerGuestCategoryShortInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_guest_category_short_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


