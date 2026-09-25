# IncomingInventoryCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_shortage** | **str** | Shortage account identifier (GUID). Default 07926ff3-9319-b93e-80ff-1897825fdead | [optional] 
**account_surplus** | **str** | Surplus account identifier (GUID). Default 67af8bc9-628f-2124-2345-3750bb7db6fa | [optional] 
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing | [optional] 
**items** | [**List[IncomingInventoryCreateItem]**](IncomingInventoryCreateItem.md) | Main inventory items (second step / all products). Must contain at least one element | 
**items_first_step** | [**List[IncomingInventoryCreateFirstStepItem]**](IncomingInventoryCreateFirstStepItem.md) | First step items (dishes, preparations, modifiers). Can be an empty array | 
**number** | **str** | Document number | [optional] 
**organization_id** | **str** | Organization identifier (GUID) | 
**store** | **str** | Inventory store identifier (GUID) | 

## Example

```python
from iikocloud_client.models.incoming_inventory_create_request import IncomingInventoryCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingInventoryCreateRequest from a JSON string
incoming_inventory_create_request_instance = IncomingInventoryCreateRequest.from_json(json)
# print the JSON string representation of the object
print(IncomingInventoryCreateRequest.to_json())

# convert the object into a dict
incoming_inventory_create_request_dict = incoming_inventory_create_request_instance.to_dict()
# create an instance of IncomingInventoryCreateRequest from a dict
incoming_inventory_create_request_from_dict = IncomingInventoryCreateRequest.from_dict(incoming_inventory_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


