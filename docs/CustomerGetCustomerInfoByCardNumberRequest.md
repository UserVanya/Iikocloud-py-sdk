# CustomerGetCustomerInfoByCardNumberRequest

Request to get customer by card number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Customer card number. | [optional] 

## Example

```python
from iikocloud_client.models.customer_get_customer_info_by_card_number_request import CustomerGetCustomerInfoByCardNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCustomerInfoByCardNumberRequest from a JSON string
customer_get_customer_info_by_card_number_request_instance = CustomerGetCustomerInfoByCardNumberRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCustomerInfoByCardNumberRequest.to_json())

# convert the object into a dict
customer_get_customer_info_by_card_number_request_dict = customer_get_customer_info_by_card_number_request_instance.to_dict()
# create an instance of CustomerGetCustomerInfoByCardNumberRequest from a dict
customer_get_customer_info_by_card_number_request_from_dict = CustomerGetCustomerInfoByCardNumberRequest.from_dict(customer_get_customer_info_by_card_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


