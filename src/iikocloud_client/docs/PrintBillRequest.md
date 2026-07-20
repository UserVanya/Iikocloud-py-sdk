# PrintBillRequest

Request to print bill.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID. | 

## Example

```python
from iikocloud_client.models.print_bill_request import PrintBillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrintBillRequest from a JSON string
print_bill_request_instance = PrintBillRequest.from_json(json)
# print the JSON string representation of the object
print(PrintBillRequest.to_json())

# convert the object into a dict
print_bill_request_dict = print_bill_request_instance.to_dict()
# create an instance of PrintBillRequest from a dict
print_bill_request_from_dict = PrintBillRequest.from_dict(print_bill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


