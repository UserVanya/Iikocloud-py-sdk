# Store


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Store address; null if the address is not filled in | [optional] 
**code** | **str** | User-defined store code | [optional] 
**custom_transactions_allowed** | **bool** | Flag indicating whether custom transactions can be created on the associated store account | [optional] 
**deleted** | **bool** | Flag indicating that the store is logically deleted | [optional] 
**description** | **str** | Text description of the store; null if the description is not filled in | [optional] 
**external_store_guid** | **str** | GUID of the supplier store from which internal API server automatically creates an internal transfer when posting a sales act; null if the supplier store is not configured | [optional] 
**gln** | **str** | Global Location Number (GLN) of the store; null if the number is not set | [optional] 
**id** | **str** | Store identifier | [optional] 
**modified_at** | **str** | Date and time of the last modification in ISO 8601 format with time zone; null if unknown | [optional] 
**name** | **str** | Display name of the store | [optional] 
**organization_id** | **str** | Identifier of the parent store entity in the NPE hierarchy; null if no link is set | [optional] 
**parent** | **str** | Identifier of the parent store entity; null if no parent is set | [optional] 
**representative_supplier** | **str** | Store&#39;s representative supplier: outgoing invoices in its name automatically create incoming invoices for this store; null if not configured | [optional] 
**revision** | **int** | Store revision number | [optional] 
**system_account** | **bool** | Flag indicating that the account associated with the store is a system account | [optional] 
**type** | **str** | Store entity type | [optional] 

## Example

```python
from iikocloud_client.models.store import Store

# TODO update the JSON string below
json = "{}"
# create an instance of Store from a JSON string
store_instance = Store.from_json(json)
# print the JSON string representation of the object
print(Store.to_json())

# convert the object into a dict
store_dict = store_instance.to_dict()
# create an instance of Store from a dict
store_from_dict = Store.from_dict(store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


