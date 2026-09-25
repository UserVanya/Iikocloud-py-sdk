# IncomingInventoryGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_shortage** | **str** | Shortage account identifier (GUID). Default 07926ff3-9319-b93e-80ff-1897825fdead | [optional] 
**account_surplus** | **str** | Surplus account identifier (GUID). Default 67af8bc9-628f-2124-2345-3750bb7db6fa | [optional] 
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**current_step** | **int** | Current inventory step. Read-only | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_created** | **str** | Document creation date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_modified** | **str** | Document last modification date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing | [optional] 
**items** | [**List[IncomingInventoryGetItem]**](IncomingInventoryGetItem.md) | Main inventory items (second step / all products). Must contain at least one element | [optional] 
**items_first_step** | [**List[IncomingInventoryGetFirstItem]**](IncomingInventoryGetFirstItem.md) | First step items (dishes, preparations, modifiers). Can be an empty array | [optional] 
**number** | **str** | Document number | [optional] 
**register_turnover** | **bool** | Flag for tracking product movement over the period. Read-only | [optional] 
**status** | **str** | Document status (NEW — not processed, PROCESSED — processed, DELETED — deleted) | [optional] 
**store** | **str** | Inventory store identifier (GUID) | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.incoming_inventory_get_response import IncomingInventoryGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInventoryGetResponse from a JSON string
incoming_inventory_get_response_instance = IncomingInventoryGetResponse.from_json(json)
# print the JSON string representation of the object
print(IncomingInventoryGetResponse.to_json())

# convert the object into a dict
incoming_inventory_get_response_dict = incoming_inventory_get_response_instance.to_dict()
# create an instance of IncomingInventoryGetResponse from a dict
incoming_inventory_get_response_from_dict = IncomingInventoryGetResponse.from_dict(incoming_inventory_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


