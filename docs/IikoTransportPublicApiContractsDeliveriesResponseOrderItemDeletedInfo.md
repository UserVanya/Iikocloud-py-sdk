# IikoTransportPublicApiContractsDeliveriesResponseOrderItemDeletedInfo

Order cancellation details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletion_method** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderDeletionMethod**](IikoTransportPublicApiContractsDeliveriesResponseOrderDeletionMethod.md) | Deletion method. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_item_deleted_info import IikoTransportPublicApiContractsDeliveriesResponseOrderItemDeletedInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderItemDeletedInfo from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_item_deleted_info_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderItemDeletedInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderItemDeletedInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_item_deleted_info_dict = iiko_transport_public_api_contracts_deliveries_response_order_item_deleted_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderItemDeletedInfo from a dict
iiko_transport_public_api_contracts_deliveries_response_order_item_deleted_info_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderItemDeletedInfo.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_item_deleted_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


