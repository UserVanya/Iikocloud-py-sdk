# IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest

Not empty `phone` or `magnetCardTrack` or `id` is required for successful import.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Customer id. | [optional] 
**phone** | **str** | Customer phone. Can be null. | [optional] 
**card_track** | **str** | Card track. Required if cardNumber set. Can be null. | [optional] 
**card_number** | **str** | Card number. Required if cardTrack set. Can be null. | [optional] 
**name** | **str** | Customer name. Can be null. | [optional] 
**middle_name** | **str** | Customer middle name. Can be null. | [optional] 
**sur_name** | **str** | Customer surname. Can be null. | [optional] 
**birthday** | **str** | Customer birthday. | [optional] 
**email** | **str** | Customer email. Can be null. | [optional] 
**sex** | [**IikoNetServiceContractsApiIikoTransportCustomerIikoNetUserSex**](IikoNetServiceContractsApiIikoTransportCustomerIikoNetUserSex.md) | Customer sex.  &lt;br&gt;0 - not specified,&lt;br /&gt;1 - male,&lt;br /&gt;2 - female. | [optional] 
**consent_status** | [**IikoNetServiceContractsApiIikoTransportCustomerPersonalDataConsentStatus**](IikoNetServiceContractsApiIikoTransportCustomerPersonalDataConsentStatus.md) | Customer consent status.  &lt;br&gt;0 - unknown,&lt;br /&gt;1 - given,&lt;br /&gt;2 - revoked. | [optional] 
**should_receive_loyalty_info** | **bool** | Customer get loyalty messages (email, sms). If the parameter is not specified for new customers, the value &#39;true&#39; is used. | [optional] 
**should_receive_promo_actions_info** | **bool** | Customer get promo messages (email, sms). If the parameter is not specified for new customers, the value &#39;true&#39; is used. | [optional] 
**referrer_id** | **str** | Id for referrer guest. Null for old integrations, Guid.Empty - for referrer deletion. Can be null. | [optional] 
**user_data** | **str** | Customer user data. Can be null. | [optional] 
**is_deleted** | **bool** | Customer logical deletion flag. | [optional] 
**organization_id** | **UUID** | Customer organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request import IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request_instance = IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request_dict = iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest from a dict
iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request_from_dict = IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


