# TransportDeliveriesResponseOrderRegularCustomer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Customer ID. | 
**name** | **str** | Name. | 
**surname** | **str** | Last name. | [optional] 
**comment** | **str** | Comment. | [optional] 
**gender** | [**TransportDeliveriesCommonGender**](TransportDeliveriesCommonGender.md) | Sex. | [optional] 
**in_blacklist** | **bool** | Is client in blacklist. | [optional] 
**blacklist_reason** | **str** | Reason why client was added to blacklist. | [optional] 
**birthdate** | **str** | Date of birth.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_regular_customer import TransportDeliveriesResponseOrderRegularCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderRegularCustomer from a JSON string
transport_deliveries_response_order_regular_customer_instance = TransportDeliveriesResponseOrderRegularCustomer.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderRegularCustomer.to_json())

# convert the object into a dict
transport_deliveries_response_order_regular_customer_dict = transport_deliveries_response_order_regular_customer_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderRegularCustomer from a dict
transport_deliveries_response_order_regular_customer_from_dict = TransportDeliveriesResponseOrderRegularCustomer.from_dict(transport_deliveries_response_order_regular_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


