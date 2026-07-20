# TableOrderCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthdate** | **str** | Date of birth. | [optional] 
**comment** | **str** | Comment. | [optional] 
**email** | **str** | Email. | [optional] 
**gender** | [**Gender**](Gender.md) | Gender. | [optional] 
**id** | **UUID** | Existing customer ID in RMS.   &gt; If null - the phone number and name is searched in database, otherwise the new customer is created in RMS. | [optional] 
**name** | **str** | Name of customer.  &gt; Required if \&quot;id\&quot; &#x3D;&#x3D; null.  &gt; Not required if \&quot;id\&quot; specified. | [optional] 
**phone** | **str** | Customer phone.  &gt; Required if \&quot;id\&quot; &#x3D;&#x3D; null.  &gt; Not required if \&quot;id\&quot; specified. | [optional] 
**should_receive_order_status_notifications** | **bool** | Whether customer receives order status notification messages. | [optional] 
**surname** | **str** | Last name. | [optional] 

## Example

```python
from iikocloud_client.models.table_order_customer import TableOrderCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrderCustomer from a JSON string
table_order_customer_instance = TableOrderCustomer.from_json(json)
# print the JSON string representation of the object
print(TableOrderCustomer.to_json())

# convert the object into a dict
table_order_customer_dict = table_order_customer_instance.to_dict()
# create an instance of TableOrderCustomer from a dict
table_order_customer_from_dict = TableOrderCustomer.from_dict(table_order_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


