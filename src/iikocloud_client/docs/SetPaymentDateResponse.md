# SetPaymentDateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Operation result message | [optional] 

## Example

```python
from iikocloud_client.models.set_payment_date_response import SetPaymentDateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetPaymentDateResponse from a JSON string
set_payment_date_response_instance = SetPaymentDateResponse.from_json(json)
# print the JSON string representation of the object
print(SetPaymentDateResponse.to_json())

# convert the object into a dict
set_payment_date_response_dict = set_payment_date_response_instance.to_dict()
# create an instance of SetPaymentDateResponse from a dict
set_payment_date_response_from_dict = SetPaymentDateResponse.from_dict(set_payment_date_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


