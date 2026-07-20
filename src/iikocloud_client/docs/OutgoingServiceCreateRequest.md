# OutgoingServiceCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**contract_date** | **str** | Contract date (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm) | [optional] 
**contract_number** | **str** | Contract number | [optional] 
**counteragent** | **str** | Counteragent identifier (GUID) | 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
**document_id** | **str** |  | [optional] 
**due_date** | **str** | Payment due date | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[OutgoingServiceCreateItem]**](OutgoingServiceCreateItem.md) | List of document items | 
**number** | **str** | Document number | [optional] 
**organization_id** | **str** | Organization identifier (GUID) | 
**revenue_account** | **str** | Revenue account identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.outgoing_service_create_request import OutgoingServiceCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingServiceCreateRequest from a JSON string
outgoing_service_create_request_instance = OutgoingServiceCreateRequest.from_json(json)
# print the JSON string representation of the object
print(OutgoingServiceCreateRequest.to_json())

# convert the object into a dict
outgoing_service_create_request_dict = outgoing_service_create_request_instance.to_dict()
# create an instance of OutgoingServiceCreateRequest from a dict
outgoing_service_create_request_from_dict = OutgoingServiceCreateRequest.from_dict(outgoing_service_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


