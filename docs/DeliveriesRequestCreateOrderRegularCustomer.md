# DeliveriesRequestCreateOrderRegularCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Existing customer ID in RMS.   &gt; If null - the phone number is searched in database, otherwise the new customer is created in RMS. | [optional] 
**name** | **str** | Name of customer.  &gt; Required for new customers (i.e. if \&quot;id\&quot; &#x3D;&#x3D; null)  &gt; Not required if \&quot;id\&quot; specified. | [optional] 
**surname** | **str** | Last name. | [optional] 
**comment** | **str** | Comment. | [optional] 
**birthdate** | **str** | Date of birth. | [optional] 
**email** | **str** | Email. | [optional] 
**should_receive_promo_actions_info** | **bool** | Deprecated, use \&quot;shouldReceiveOrderStatusNotifications\&quot; instead. | [optional] 
**should_receive_order_status_notifications** | **bool** | Whether customer receives order status notification messages. | [optional] 
**gender** | [**DeliveriesCommonGender**](DeliveriesCommonGender.md) | Gender. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_regular_customer import DeliveriesRequestCreateOrderRegularCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderRegularCustomer from a JSON string
deliveries_request_create_order_regular_customer_instance = DeliveriesRequestCreateOrderRegularCustomer.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderRegularCustomer.to_json())

# convert the object into a dict
deliveries_request_create_order_regular_customer_dict = deliveries_request_create_order_regular_customer_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderRegularCustomer from a dict
deliveries_request_create_order_regular_customer_from_dict = DeliveriesRequestCreateOrderRegularCustomer.from_dict(deliveries_request_create_order_regular_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


