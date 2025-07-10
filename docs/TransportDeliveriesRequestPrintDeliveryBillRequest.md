# TransportDeliveriesRequestPrintDeliveryBillRequest

Request to print delivery bill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. | 
**order_id** | **str** | Order ID. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_print_delivery_bill_request import TransportDeliveriesRequestPrintDeliveryBillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestPrintDeliveryBillRequest from a JSON string
transport_deliveries_request_print_delivery_bill_request_instance = TransportDeliveriesRequestPrintDeliveryBillRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestPrintDeliveryBillRequest.to_json())

# convert the object into a dict
transport_deliveries_request_print_delivery_bill_request_dict = transport_deliveries_request_print_delivery_bill_request_instance.to_dict()
# create an instance of TransportDeliveriesRequestPrintDeliveryBillRequest from a dict
transport_deliveries_request_print_delivery_bill_request_from_dict = TransportDeliveriesRequestPrintDeliveryBillRequest.from_dict(transport_deliveries_request_print_delivery_bill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


