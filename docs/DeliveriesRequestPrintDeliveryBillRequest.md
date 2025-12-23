# DeliveriesRequestPrintDeliveryBillRequest

Request to print delivery bill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. | 
**order_id** | **str** | Order ID. | 

## Example

```python
from iikocloud_client.models.deliveries_request_print_delivery_bill_request import DeliveriesRequestPrintDeliveryBillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestPrintDeliveryBillRequest from a JSON string
deliveries_request_print_delivery_bill_request_instance = DeliveriesRequestPrintDeliveryBillRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestPrintDeliveryBillRequest.to_json())

# convert the object into a dict
deliveries_request_print_delivery_bill_request_dict = deliveries_request_print_delivery_bill_request_instance.to_dict()
# create an instance of DeliveriesRequestPrintDeliveryBillRequest from a dict
deliveries_request_print_delivery_bill_request_from_dict = DeliveriesRequestPrintDeliveryBillRequest.from_dict(deliveries_request_print_delivery_bill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


