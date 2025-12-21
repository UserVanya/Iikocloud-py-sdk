# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRegularCustomer


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
**gender** | [**IikoTransportPublicApiContractsDeliveriesCommonGender**](IikoTransportPublicApiContractsDeliveriesCommonGender.md) | Gender. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_regular_customer import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRegularCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRegularCustomer from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_regular_customer_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRegularCustomer.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRegularCustomer.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_regular_customer_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_regular_customer_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRegularCustomer from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_regular_customer_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRegularCustomer.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_regular_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


