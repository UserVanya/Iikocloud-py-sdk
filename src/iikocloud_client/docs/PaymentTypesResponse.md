# PaymentTypesResponse

Response to request for payment types by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** |  | 
**payment_types** | [**List[PaymentTypeDefinition]**](PaymentTypeDefinition.md) | List of payment types and terminal groups where they are available. | 

## Example

```python
from iikocloud_client.models.payment_types_response import PaymentTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypesResponse from a JSON string
payment_types_response_instance = PaymentTypesResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentTypesResponse.to_json())

# convert the object into a dict
payment_types_response_dict = payment_types_response_instance.to_dict()
# create an instance of PaymentTypesResponse from a dict
payment_types_response_from_dict = PaymentTypesResponse.from_dict(payment_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


