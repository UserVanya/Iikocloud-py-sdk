# PaymentTypeGetByIDRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Entity identifier (UUID) | [optional] 

## Example

```python
from iikocloud_client.models.payment_type_get_by_id_request import PaymentTypeGetByIDRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypeGetByIDRequest from a JSON string
payment_type_get_by_id_request_instance = PaymentTypeGetByIDRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentTypeGetByIDRequest.to_json())

# convert the object into a dict
payment_type_get_by_id_request_dict = payment_type_get_by_id_request_instance.to_dict()
# create an instance of PaymentTypeGetByIDRequest from a dict
payment_type_get_by_id_request_from_dict = PaymentTypeGetByIDRequest.from_dict(payment_type_get_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


