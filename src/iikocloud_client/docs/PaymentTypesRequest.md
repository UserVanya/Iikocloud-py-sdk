# PaymentTypesRequest

Request for payment types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which payment types have to be returned.                 Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.payment_types_request import PaymentTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypesRequest from a JSON string
payment_types_request_instance = PaymentTypesRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentTypesRequest.to_json())

# convert the object into a dict
payment_types_request_dict = payment_types_request_instance.to_dict()
# create an instance of PaymentTypesRequest from a dict
payment_types_request_from_dict = PaymentTypesRequest.from_dict(payment_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


