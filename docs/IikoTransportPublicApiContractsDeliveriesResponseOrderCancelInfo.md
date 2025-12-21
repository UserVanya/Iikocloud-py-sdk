# IikoTransportPublicApiContractsDeliveriesResponseOrderCancelInfo

Order cancellation details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when_cancelled** | **str** | Cancellation time (Local for delivery terminal). | 
**cause** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderCancelCause**](IikoTransportPublicApiContractsDeliveriesResponseOrderCancelCause.md) | Delivery cancellation reason. | 
**comment** | **str** | Delivery cancellation comment. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_cancel_info import IikoTransportPublicApiContractsDeliveriesResponseOrderCancelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCancelInfo from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_cancel_info_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderCancelInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderCancelInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_cancel_info_dict = iiko_transport_public_api_contracts_deliveries_response_order_cancel_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCancelInfo from a dict
iiko_transport_public_api_contracts_deliveries_response_order_cancel_info_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderCancelInfo.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_cancel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


