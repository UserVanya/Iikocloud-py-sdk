# DeliveryOrderCreateRegularCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthdate** | **str** | Date of birth. | [optional] 
**comment** | **str** | Comment. | [optional] 
**email** | **str** | Email. | [optional] 
**gender** | [**Gender**](Gender.md) | Gender. | [optional] 
**id** | **UUID** | Existing customer ID in RMS.   &gt; If null - the phone number is searched in database, otherwise the new customer is created in RMS. | [optional] 
**name** | **str** | Name of customer.  &gt; Required for new customers (i.e. if \&quot;id\&quot; &#x3D;&#x3D; null)  &gt; Not required if \&quot;id\&quot; specified. | [optional] 
**should_receive_order_status_notifications** | **bool** | Whether customer receives order status notification messages. | [optional] 
**should_receive_promo_actions_info** | **bool** | Deprecated, use \&quot;shouldReceiveOrderStatusNotifications\&quot; instead. | [optional] 
**surname** | **str** | Last name. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_create_regular_customer import DeliveryOrderCreateRegularCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateRegularCustomer from a JSON string
delivery_order_create_regular_customer_instance = DeliveryOrderCreateRegularCustomer.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateRegularCustomer.to_json())

# convert the object into a dict
delivery_order_create_regular_customer_dict = delivery_order_create_regular_customer_instance.to_dict()
# create an instance of DeliveryOrderCreateRegularCustomer from a dict
delivery_order_create_regular_customer_from_dict = DeliveryOrderCreateRegularCustomer.from_dict(delivery_order_create_regular_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


