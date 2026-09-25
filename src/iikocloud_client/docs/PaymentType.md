# PaymentType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | User-defined payment type code | [optional] 
**id** | **str** | Payment type identifier (UUID) | [optional] 
**is_deleted** | **bool** | Flag indicating that the payment type is logically deleted | [optional] 
**name** | **str** | Display name of the payment type | [optional] 

## Example

```python
from iikocloud_client.models.payment_type import PaymentType

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentType from a JSON string
payment_type_instance = PaymentType.from_json(json)
# print the JSON string representation of the object
print(PaymentType.to_json())

# convert the object into a dict
payment_type_dict = payment_type_instance.to_dict()
# create an instance of PaymentType from a dict
payment_type_from_dict = PaymentType.from_dict(payment_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


