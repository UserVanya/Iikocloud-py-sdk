# IikoTransportPublicApiContractsDeliveriesResponseOrderDeletionMethod

Deletion method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**comment** | **str** | Comment. | [optional] 
**removal_type** | [**IikoTransportPublicApiContractsDeliveriesResponseOrderRemovalType**](IikoTransportPublicApiContractsDeliveriesResponseOrderRemovalType.md) | Write-off type. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_deletion_method import IikoTransportPublicApiContractsDeliveriesResponseOrderDeletionMethod

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderDeletionMethod from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_deletion_method_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderDeletionMethod.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderDeletionMethod.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_deletion_method_dict = iiko_transport_public_api_contracts_deliveries_response_order_deletion_method_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderDeletionMethod from a dict
iiko_transport_public_api_contracts_deliveries_response_order_deletion_method_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderDeletionMethod.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_deletion_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


