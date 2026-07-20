# SetPaymentDateOutgoingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Incoming invoice identifier (GUID) | 
**organization_id** | **str** | Organization identifier (GUID) | 
**payment_date** | **str** | Payment date (YYYY-MM-DD format) | 

## Example

```python
from iikocloud_client.models.set_payment_date_outgoing_request import SetPaymentDateOutgoingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetPaymentDateOutgoingRequest from a JSON string
set_payment_date_outgoing_request_instance = SetPaymentDateOutgoingRequest.from_json(json)
# print the JSON string representation of the object
print(SetPaymentDateOutgoingRequest.to_json())

# convert the object into a dict
set_payment_date_outgoing_request_dict = set_payment_date_outgoing_request_instance.to_dict()
# create an instance of SetPaymentDateOutgoingRequest from a dict
set_payment_date_outgoing_request_from_dict = SetPaymentDateOutgoingRequest.from_dict(set_payment_date_outgoing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


