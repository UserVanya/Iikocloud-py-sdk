# TransportTableOrdersRequestTableOrderCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Existing customer ID in RMS.   &gt; If null - the phone number and name is searched in database, otherwise the new customer is created in RMS. | [optional] 
**name** | **str** | Name of customer.  &gt; Required if \&quot;id\&quot; &#x3D;&#x3D; null.  &gt; Not required if \&quot;id\&quot; specified. | [optional] 
**surname** | **str** | Last name. | [optional] 
**comment** | **str** | Comment. | [optional] 
**birthdate** | **str** | Date of birth. | [optional] 
**email** | **str** | Email. | [optional] 
**should_receive_order_status_notifications** | **bool** | Whether customer receives order status notification messages. | [optional] 
**gender** | [**TransportDeliveriesCommonGender**](TransportDeliveriesCommonGender.md) | Gender. | [optional] 
**phone** | **str** | Customer phone.  &gt; Required if \&quot;id\&quot; &#x3D;&#x3D; null.  &gt; Not required if \&quot;id\&quot; specified. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_table_orders_request_table_order_customer import TransportTableOrdersRequestTableOrderCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersRequestTableOrderCustomer from a JSON string
transport_table_orders_request_table_order_customer_instance = TransportTableOrdersRequestTableOrderCustomer.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersRequestTableOrderCustomer.to_json())

# convert the object into a dict
transport_table_orders_request_table_order_customer_dict = transport_table_orders_request_table_order_customer_instance.to_dict()
# create an instance of TransportTableOrdersRequestTableOrderCustomer from a dict
transport_table_orders_request_table_order_customer_from_dict = TransportTableOrdersRequestTableOrderCustomer.from_dict(transport_table_orders_request_table_order_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


