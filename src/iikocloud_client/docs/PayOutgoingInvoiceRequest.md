# PayOutgoingInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Account identifier (GUID) | 
**amount** | **float** | Payment amount | 
**cfo_item_id** | **str** | Cash flow item identifier (GUID) | [optional] 
**document_id** | **str** | Outgoing invoice identifier (GUID) | 
**organization_id** | **str** | Organization identifier (GUID) | 
**payment_date** | **str** | Payment date (YYYY-MM-DD format) | 

## Example

```python
from iikocloud_client.models.pay_outgoing_invoice_request import PayOutgoingInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayOutgoingInvoiceRequest from a JSON string
pay_outgoing_invoice_request_instance = PayOutgoingInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(PayOutgoingInvoiceRequest.to_json())

# convert the object into a dict
pay_outgoing_invoice_request_dict = pay_outgoing_invoice_request_instance.to_dict()
# create an instance of PayOutgoingInvoiceRequest from a dict
pay_outgoing_invoice_request_from_dict = PayOutgoingInvoiceRequest.from_dict(pay_outgoing_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


