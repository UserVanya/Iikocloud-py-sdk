# TransportPaymentTypesPaymentTypesRequest

Request for payment types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations IDs which payment types have to be returned.                 Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_payment_types_payment_types_request import TransportPaymentTypesPaymentTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportPaymentTypesPaymentTypesRequest from a JSON string
transport_payment_types_payment_types_request_instance = TransportPaymentTypesPaymentTypesRequest.from_json(json)
# print the JSON string representation of the object
print(TransportPaymentTypesPaymentTypesRequest.to_json())

# convert the object into a dict
transport_payment_types_payment_types_request_dict = transport_payment_types_payment_types_request_instance.to_dict()
# create an instance of TransportPaymentTypesPaymentTypesRequest from a dict
transport_payment_types_payment_types_request_from_dict = TransportPaymentTypesPaymentTypesRequest.from_dict(transport_payment_types_payment_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


