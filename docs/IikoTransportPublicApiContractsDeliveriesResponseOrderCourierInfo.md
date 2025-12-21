# IikoTransportPublicApiContractsDeliveriesResponseOrderCourierInfo

Driver information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee**](IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee.md) | Order driver. | 
**is_courier_selected_manually** | **bool** | Whether driver is selected manually. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_courier_info import IikoTransportPublicApiContractsDeliveriesResponseOrderCourierInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCourierInfo from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_courier_info_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderCourierInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderCourierInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_courier_info_dict = iiko_transport_public_api_contracts_deliveries_response_order_courier_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCourierInfo from a dict
iiko_transport_public_api_contracts_deliveries_response_order_courier_info_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderCourierInfo.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_courier_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


