# IncomingInventoryListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_shortage** | **str** | Shortage account identifier (GUID). Default 07926ff3-9319-b93e-80ff-1897825fdead | [optional] 
**account_surplus** | **str** | Surplus account identifier (GUID). Default 67af8bc9-628f-2124-2345-3750bb7db6fa | [optional] 
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_created** | **str** | Document creation date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_modified** | **str** | Document last modification date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**deleted** | **bool** | Flag indicating that the document is deleted | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing | [optional] 
**number** | **str** | Document number | [optional] 
**processed** | **bool** | Flag indicating that the document is processed | [optional] 
**shortage_sum** | **float** | Shortage sum | [optional] 
**store_from** | **str** | Write-off store identifier (GUID) | [optional] 
**sum** | **float** | Amount including VAT | [optional] 
**surplus_sum** | **float** | Surplus sum | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.incoming_inventory_list_item import IncomingInventoryListItem

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInventoryListItem from a JSON string
incoming_inventory_list_item_instance = IncomingInventoryListItem.from_json(json)
# print the JSON string representation of the object
print(IncomingInventoryListItem.to_json())

# convert the object into a dict
incoming_inventory_list_item_dict = incoming_inventory_list_item_instance.to_dict()
# create an instance of IncomingInventoryListItem from a dict
incoming_inventory_list_item_from_dict = IncomingInventoryListItem.from_dict(incoming_inventory_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


