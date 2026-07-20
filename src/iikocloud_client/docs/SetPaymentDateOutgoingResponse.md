# SetPaymentDateOutgoingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.set_payment_date_outgoing_response import SetPaymentDateOutgoingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetPaymentDateOutgoingResponse from a JSON string
set_payment_date_outgoing_response_instance = SetPaymentDateOutgoingResponse.from_json(json)
# print the JSON string representation of the object
print(SetPaymentDateOutgoingResponse.to_json())

# convert the object into a dict
set_payment_date_outgoing_response_dict = set_payment_date_outgoing_response_instance.to_dict()
# create an instance of SetPaymentDateOutgoingResponse from a dict
set_payment_date_outgoing_response_from_dict = SetPaymentDateOutgoingResponse.from_dict(set_payment_date_outgoing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


