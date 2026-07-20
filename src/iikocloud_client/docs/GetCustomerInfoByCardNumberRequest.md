# GetCustomerInfoByCardNumberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Customer card number. | [optional] 

## Example

```python
from iikocloud_client.models.get_customer_info_by_card_number_request import GetCustomerInfoByCardNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerInfoByCardNumberRequest from a JSON string
get_customer_info_by_card_number_request_instance = GetCustomerInfoByCardNumberRequest.from_json(json)
# print the JSON string representation of the object
print(GetCustomerInfoByCardNumberRequest.to_json())

# convert the object into a dict
get_customer_info_by_card_number_request_dict = get_customer_info_by_card_number_request_instance.to_dict()
# create an instance of GetCustomerInfoByCardNumberRequest from a dict
get_customer_info_by_card_number_request_from_dict = GetCustomerInfoByCardNumberRequest.from_dict(get_customer_info_by_card_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


