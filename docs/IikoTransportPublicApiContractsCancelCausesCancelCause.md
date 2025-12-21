# IikoTransportPublicApiContractsCancelCausesCancelCause

Delivery cancel cause.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Identifier. | 
**name** | **str** | Name. | 
**is_deleted** | **bool** | Is deleted sign. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_cancel_causes_cancel_cause import IikoTransportPublicApiContractsCancelCausesCancelCause

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsCancelCausesCancelCause from a JSON string
iiko_transport_public_api_contracts_cancel_causes_cancel_cause_instance = IikoTransportPublicApiContractsCancelCausesCancelCause.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsCancelCausesCancelCause.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_cancel_causes_cancel_cause_dict = iiko_transport_public_api_contracts_cancel_causes_cancel_cause_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsCancelCausesCancelCause from a dict
iiko_transport_public_api_contracts_cancel_causes_cancel_cause_from_dict = IikoTransportPublicApiContractsCancelCausesCancelCause.from_dict(iiko_transport_public_api_contracts_cancel_causes_cancel_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


