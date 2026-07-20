# InternalTransferGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_created** | **str** | Document creation date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**date_modified** | **str** | Document last modification date (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | [optional] 
**document_id** | **str** | Document identifier (GUID) | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[InternalTransferGetItem]**](InternalTransferGetItem.md) | List of document items | [optional] 
**number** | **str** | Document number | [optional] 
**status** | **str** | Document status (NEW — not processed, PROCESSED — processed, DELETED — deleted) | [optional] 
**store_from** | **str** | Write-off store identifier (GUID) | [optional] 
**store_to** | **str** | Receipt store identifier (GUID) | [optional] 
**user_created** | **str** | User who created the document (GUID) | [optional] 
**user_modified** | **str** | User who last modified the document (GUID) | [optional] 

## Example

```python
from iikocloud_client.models.internal_transfer_get_response import InternalTransferGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransferGetResponse from a JSON string
internal_transfer_get_response_instance = InternalTransferGetResponse.from_json(json)
# print the JSON string representation of the object
print(InternalTransferGetResponse.to_json())

# convert the object into a dict
internal_transfer_get_response_dict = internal_transfer_get_response_instance.to_dict()
# create an instance of InternalTransferGetResponse from a dict
internal_transfer_get_response_from_dict = InternalTransferGetResponse.from_dict(internal_transfer_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


