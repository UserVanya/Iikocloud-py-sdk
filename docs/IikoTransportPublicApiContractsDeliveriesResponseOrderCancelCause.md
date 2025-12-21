# IikoTransportPublicApiContractsDeliveriesResponseOrderCancelCause

Delivery cancellation reason.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Description. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_cancel_cause import IikoTransportPublicApiContractsDeliveriesResponseOrderCancelCause

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCancelCause from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_cancel_cause_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderCancelCause.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderCancelCause.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_cancel_cause_dict = iiko_transport_public_api_contracts_deliveries_response_order_cancel_cause_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderCancelCause from a dict
iiko_transport_public_api_contracts_deliveries_response_order_cancel_cause_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderCancelCause.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_cancel_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


