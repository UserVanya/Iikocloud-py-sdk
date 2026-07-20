# InternalTransferCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**conception** | **str** | Concept identifier (GUID) | [optional] 
**var_date** | **str** | Document date and time (ISO 8601 YYYY-MM-DDThh:mm:ss.sss±hh:mm) | 
**document_id** | **str** |  | [optional] 
**is_automatic** | **bool** | Automatic document creation flag | [optional] 
**is_editable** | **bool** | Editable flag. true — available for editing in RMS | [optional] 
**items** | [**List[InternalTransferCreateItem]**](InternalTransferCreateItem.md) | List of document items | 
**number** | **str** | Document number | [optional] 
**organization_id** | **str** | Organization identifier (GUID) | 
**store_from** | **str** | Write-off store identifier (GUID) | 
**store_to** | **str** | Receipt store identifier (GUID) | 

## Example

```python
from iikocloud_client.models.internal_transfer_create_request import InternalTransferCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalTransferCreateRequest from a JSON string
internal_transfer_create_request_instance = InternalTransferCreateRequest.from_json(json)
# print the JSON string representation of the object
print(InternalTransferCreateRequest.to_json())

# convert the object into a dict
internal_transfer_create_request_dict = internal_transfer_create_request_instance.to_dict()
# create an instance of InternalTransferCreateRequest from a dict
internal_transfer_create_request_from_dict = InternalTransferCreateRequest.from_dict(internal_transfer_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


