# TransportDeliveriesRequestCreateOrderRegularCustomer

'Regular' customer:  - can be used only if a customer agrees to take part in the store's loyalty programs  - customer details will be added (updated) to the store's customer database  - benefits (accumulation of rewards, etc.) of active loyalty programs will be made available to the customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Existing customer ID in RMS.   &gt; If null - the phone number is searched in database, otherwise the new customer is created in RMS. | [optional] 
**name** | **str** | Name of customer.  &gt; Required for new customers (i.e. if \&quot;id\&quot; &#x3D;&#x3D; null)  &gt; Not required if \&quot;id\&quot; specified. | [optional] 
**surname** | **str** | Last name. | [optional] 
**comment** | **str** | Comment. | [optional] 
**birthdate** | **str** | Date of birth. | [optional] 
**email** | **str** | Email. | [optional] 
**should_receive_promo_actions_info** | **bool** | Deprecated, use \&quot;shouldReceiveOrderStatusNotifications\&quot; instead. | [optional] 
**should_receive_order_status_notifications** | **bool** | Whether customer receives order status notification messages. | [optional] 
**gender** | [**TransportDeliveriesCommonGender**](TransportDeliveriesCommonGender.md) | Gender. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_regular_customer import TransportDeliveriesRequestCreateOrderRegularCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderRegularCustomer from a JSON string
transport_deliveries_request_create_order_regular_customer_instance = TransportDeliveriesRequestCreateOrderRegularCustomer.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderRegularCustomer.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_regular_customer_dict = transport_deliveries_request_create_order_regular_customer_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderRegularCustomer from a dict
transport_deliveries_request_create_order_regular_customer_from_dict = TransportDeliveriesRequestCreateOrderRegularCustomer.from_dict(transport_deliveries_request_create_order_regular_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


