# IncomingServiceGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**contract_date** | **str** | Contract date (ISO 8601 YYYY-MM-DDThh:mm:ss±hh:mm) | [optional] 
**contract_number** | **str** | Contract number | [optional] 
**counteragent** | **str** | Counteragent identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_created** | **str** | Document creation date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_modified** | **str** | Document last modification date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**due_date** | **str** | Payment due date | [optional] 
**employee_pass_to_account** | **str** | Charge to employee | [optional] 
**incoming_date** | **str** | Incoming document date (YYYY-MM-DD) | [optional] 
**incoming_document_number** | **str** | Incoming external document number | [optional] 
**invoice** | **str** | Invoice number | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[IncomingServiceGetItem]**](IncomingServiceGetItem.md) | List of document items | [optional] 
**number** | **str** | Document number | [optional] 
**revenue_account** | **str** | Revenue account identifier (GUID) | [optional] 
**status** | **str** | Document status (NEW — not processed, PROCESSED — processed, DELETED — deleted) | [optional] 
**sum** | **float** | Amount including VAT | [optional] 
**sum_without_vat** | **float** | Amount excluding VAT | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.incoming_service_get_response import IncomingServiceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncomingServiceGetResponse from a JSON string
incoming_service_get_response_instance = IncomingServiceGetResponse.from_json(json)
# print the JSON string representation of the object
print(IncomingServiceGetResponse.to_json())

# convert the object into a dict
incoming_service_get_response_dict = incoming_service_get_response_instance.to_dict()
# create an instance of IncomingServiceGetResponse from a dict
incoming_service_get_response_from_dict = IncomingServiceGetResponse.from_dict(incoming_service_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


