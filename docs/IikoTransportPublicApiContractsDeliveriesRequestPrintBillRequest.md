# IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest

Request to print bill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_print_bill_request import IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest from a JSON string
iiko_transport_public_api_contracts_deliveries_request_print_bill_request_instance = IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_print_bill_request_dict = iiko_transport_public_api_contracts_deliveries_request_print_bill_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest from a dict
iiko_transport_public_api_contracts_deliveries_request_print_bill_request_from_dict = IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest.from_dict(iiko_transport_public_api_contracts_deliveries_request_print_bill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


