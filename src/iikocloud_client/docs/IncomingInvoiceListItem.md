# IncomingInvoiceListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_stores** | **List[str]** |  | [optional] 
**comment** | **str** |  | [optional] 
**conception** | **str** |  | [optional] 
**counteragent** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**date_modified** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**document_id** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**is_editable** | **bool** |  | [optional] 
**items** | [**List[IncomingInvoiceItem]**](IncomingInvoiceItem.md) | List of document items | [optional] 
**number** | **str** |  | [optional] 
**processed** | **bool** |  | [optional] 
**revision** | **int** | Document revision — a monotonically increasing version number that grows on every change. In the list response it appears only when changed documents (revision) or full details (returnFullDetails) are requested | [optional] 
**sum** | **float** |  | [optional] 
**sum_without_vat** | **float** |  | [optional] 
**user_created** | **str** |  | [optional] 
**user_modified** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.incoming_invoice_list_item import IncomingInvoiceListItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInvoiceListItem from a JSON string
incoming_invoice_list_item_instance = IncomingInvoiceListItem.from_json(json)
# print the JSON string representation of the object
print(IncomingInvoiceListItem.to_json())

# convert the object into a dict
incoming_invoice_list_item_dict = incoming_invoice_list_item_instance.to_dict()
# create an instance of IncomingInvoiceListItem from a dict
incoming_invoice_list_item_from_dict = IncomingInvoiceListItem.from_dict(incoming_invoice_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


