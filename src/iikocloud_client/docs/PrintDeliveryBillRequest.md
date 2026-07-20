# PrintDeliveryBillRequest

Request to print delivery bill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID. | 

## Example

```python
from iikocloud_client.models.print_delivery_bill_request import PrintDeliveryBillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintDeliveryBillRequest from a JSON string
print_delivery_bill_request_instance = PrintDeliveryBillRequest.from_json(json)
# print the JSON string representation of the object
print(PrintDeliveryBillRequest.to_json())

# convert the object into a dict
print_delivery_bill_request_dict = print_delivery_bill_request_instance.to_dict()
# create an instance of PrintDeliveryBillRequest from a dict
print_delivery_bill_request_from_dict = PrintDeliveryBillRequest.from_dict(print_delivery_bill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


