# PaymentTypeListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[PaymentType]**](PaymentType.md) | List of entities | [optional] 
**limit** | **int** | Limit value from the request | [optional] 
**offset** | **int** | Offset value from the request | [optional] 
**total_count** | **int** | Total number of records matching the filter | [optional] 

## Example

```python
from iikocloud_client.models.payment_type_list_response import PaymentTypeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTypeListResponse from a JSON string
payment_type_list_response_instance = PaymentTypeListResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentTypeListResponse.to_json())

# convert the object into a dict
payment_type_list_response_dict = payment_type_list_response_instance.to_dict()
# create an instance of PaymentTypeListResponse from a dict
payment_type_list_response_from_dict = PaymentTypeListResponse.from_dict(payment_type_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


