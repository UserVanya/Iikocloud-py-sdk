# CustomerGuestCardInfo

Guest card info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Card id. | [optional] 
**track** | **str** | Card track. | [optional] 
**number** | **str** | Card number. | [optional] 
**valid_to_date** | **str** | Card valid to date. | [optional] 

## Example

```python
from iikocloud_client.models.customer_guest_card_info import CustomerGuestCardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGuestCardInfo from a JSON string
customer_guest_card_info_instance = CustomerGuestCardInfo.from_json(json)
# print the JSON string representation of the object
print(CustomerGuestCardInfo.to_json())

# convert the object into a dict
customer_guest_card_info_dict = customer_guest_card_info_instance.to_dict()
# create an instance of CustomerGuestCardInfo from a dict
customer_guest_card_info_from_dict = CustomerGuestCardInfo.from_dict(customer_guest_card_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


