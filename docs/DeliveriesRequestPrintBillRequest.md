# DeliveriesRequestPrintBillRequest

Request to print bill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID. | 
**order_id** | **UUID** | Order ID. | 

## Example

```python
from iikocloud_client.models.deliveries_request_print_bill_request import DeliveriesRequestPrintBillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestPrintBillRequest from a JSON string
deliveries_request_print_bill_request_instance = DeliveriesRequestPrintBillRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestPrintBillRequest.to_json())

# convert the object into a dict
deliveries_request_print_bill_request_dict = deliveries_request_print_bill_request_instance.to_dict()
# create an instance of DeliveriesRequestPrintBillRequest from a dict
deliveries_request_print_bill_request_from_dict = DeliveriesRequestPrintBillRequest.from_dict(deliveries_request_print_bill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


