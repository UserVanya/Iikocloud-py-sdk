# DeliveryOrderResponseRegularCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthdate** | **str** | Date of birth.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**blacklist_reason** | **str** | Reason why client was added to blacklist. | [optional] 
**comment** | **str** | Comment. | [optional] 
**gender** | [**Gender**](Gender.md) | Sex. | [optional] 
**id** | **UUID** | Customer ID. | 
**in_blacklist** | **bool** | Is client in blacklist. | [optional] 
**name** | **str** | Name. | 
**surname** | **str** | Last name. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_regular_customer import DeliveryOrderResponseRegularCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseRegularCustomer from a JSON string
delivery_order_response_regular_customer_instance = DeliveryOrderResponseRegularCustomer.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseRegularCustomer.to_json())

# convert the object into a dict
delivery_order_response_regular_customer_dict = delivery_order_response_regular_customer_instance.to_dict()
# create an instance of DeliveryOrderResponseRegularCustomer from a dict
delivery_order_response_regular_customer_from_dict = DeliveryOrderResponseRegularCustomer.from_dict(delivery_order_response_regular_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


