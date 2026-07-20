# IncomingServiceUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**contract_date** | **str** | Contract date (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm) | [optional] 
**contract_number** | **str** | Contract number | [optional] 
**counteragent** | **str** | Counteragent identifier (GUID) | 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
**document_id** | **str** | Document identifier (GUID) | 
**due_date** | **str** | Payment due date | [optional] 
**employee_pass_to_account** | **str** | Charge to employee | [optional] 
**incoming_date** | **str** | Incoming document date (YYYY-MM-DD) | [optional] 
**incoming_document_number** | **str** | Incoming external document number | [optional] 
**invoice** | **str** | Invoice number | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[IncomingServiceCreateItem]**](IncomingServiceCreateItem.md) | List of document items | 
**number** | **str** | Document number | 
**organization_id** | **str** | Organization identifier (GUID) | 
**revenue_account** | **str** | Revenue account identifier (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.incoming_service_update_request import IncomingServiceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingServiceUpdateRequest from a JSON string
incoming_service_update_request_instance = IncomingServiceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(IncomingServiceUpdateRequest.to_json())

# convert the object into a dict
incoming_service_update_request_dict = incoming_service_update_request_instance.to_dict()
# create an instance of IncomingServiceUpdateRequest from a dict
incoming_service_update_request_from_dict = IncomingServiceUpdateRequest.from_dict(incoming_service_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


