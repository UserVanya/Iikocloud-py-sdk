# TableOrdersRequestTableOrderCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Existing customer ID in RMS.   &gt; If null - the phone number and name is searched in database, otherwise the new customer is created in RMS. | [optional] 
**name** | **str** | Name of customer.  &gt; Required if \&quot;id\&quot; &#x3D;&#x3D; null.  &gt; Not required if \&quot;id\&quot; specified. | [optional] 
**surname** | **str** | Last name. | [optional] 
**comment** | **str** | Comment. | [optional] 
**birthdate** | **str** | Date of birth. | [optional] 
**email** | **str** | Email. | [optional] 
**should_receive_order_status_notifications** | **bool** | Whether customer receives order status notification messages. | [optional] 
**gender** | [**DeliveriesCommonGender**](DeliveriesCommonGender.md) | Gender. | [optional] 
**phone** | **str** | Customer phone.  &gt; Required if \&quot;id\&quot; &#x3D;&#x3D; null.  &gt; Not required if \&quot;id\&quot; specified. | [optional] 

## Example

```python
from iikocloud_client.models.table_orders_request_table_order_customer import TableOrdersRequestTableOrderCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestTableOrderCustomer from a JSON string
table_orders_request_table_order_customer_instance = TableOrdersRequestTableOrderCustomer.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestTableOrderCustomer.to_json())

# convert the object into a dict
table_orders_request_table_order_customer_dict = table_orders_request_table_order_customer_instance.to_dict()
# create an instance of TableOrdersRequestTableOrderCustomer from a dict
table_orders_request_table_order_customer_from_dict = TableOrdersRequestTableOrderCustomer.from_dict(table_orders_request_table_order_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


