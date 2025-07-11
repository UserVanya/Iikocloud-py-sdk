# TransportPaymentTypesPaymentTypesResponse

Response to request for payment types by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** |  | 
**payment_types** | [**List[TransportPaymentTypesPaymentType]**](TransportPaymentTypesPaymentType.md) | List of payment types and terminal groups where they are available. | 

## Example

```python
from iikocloud_client.models.transport_payment_types_payment_types_response import TransportPaymentTypesPaymentTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportPaymentTypesPaymentTypesResponse from a JSON string
transport_payment_types_payment_types_response_instance = TransportPaymentTypesPaymentTypesResponse.from_json(json)
# print the JSON string representation of the object
print(TransportPaymentTypesPaymentTypesResponse.to_json())

# convert the object into a dict
transport_payment_types_payment_types_response_dict = transport_payment_types_payment_types_response_instance.to_dict()
# create an instance of TransportPaymentTypesPaymentTypesResponse from a dict
transport_payment_types_payment_types_response_from_dict = TransportPaymentTypesPaymentTypesResponse.from_dict(transport_payment_types_payment_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


