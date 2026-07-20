# CreateOrUpdateCustomerRequest

Not empty `phone` or `magnetCardTrack` or `id` is required for successful import.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthday** | **str** | Customer birthday. | [optional] 
**card_number** | **str** | Card number. Required if cardTrack set. Can be null. | [optional] 
**card_track** | **str** | Card track. Required if cardNumber set. Can be null. | [optional] 
**comment** | **str** | Customer description and additional data. Can be null. | [optional] 
**consent_status** | [**PersonalDataConsentStatus**](PersonalDataConsentStatus.md) | Customer consent status.  &lt;br&gt;0 - unknown,&lt;br /&gt;1 - given,&lt;br /&gt;2 - revoked. | [optional] 
**email** | **str** | Customer email. Can be null. | [optional] 
**employee_id** | **str** | Employee number or id. Can be null. | [optional] 
**id** | **UUID** | Customer id. | [optional] 
**is_deleted** | **bool** | Customer logical deletion flag. | [optional] 
**middle_name** | **str** | Customer middle name. Can be null. | [optional] 
**name** | **str** | Customer name. Can be null. | [optional] 
**nullify_empty_fields** | **bool** | If set to true, then empty string values (not null) will overwrite origin guest fields with nulls, otherwise empty fields are ignored. | [optional] 
**organization_id** | **UUID** | Customer organization id. | 
**phone** | **str** | Customer phone. Can be null. | [optional] 
**referrer_id** | **str** | Id for referrer guest. Null for old integrations, Guid.Empty - for referrer deletion. Can be null. | [optional] 
**sex** | [**IikoNetUserSex**](IikoNetUserSex.md) | Customer sex.  &lt;br&gt;0 - not specified,&lt;br /&gt;1 - male,&lt;br /&gt;2 - female. | [optional] 
**should_receive_loyalty_info** | **bool** | Customer get loyalty messages (email, sms). If the parameter is not specified for new customers, the value &#39;true&#39; is used. | [optional] 
**should_receive_promo_actions_info** | **bool** | Customer get promo messages (email, sms). If the parameter is not specified for new customers, the value &#39;true&#39; is used. | [optional] 
**sur_name** | **str** | Customer surname. Can be null. | [optional] 
**user_data** | **str** | Customer user data. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.create_or_update_customer_request import CreateOrUpdateCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateCustomerRequest from a JSON string
create_or_update_customer_request_instance = CreateOrUpdateCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateCustomerRequest.to_json())

# convert the object into a dict
create_or_update_customer_request_dict = create_or_update_customer_request_instance.to_dict()
# create an instance of CreateOrUpdateCustomerRequest from a dict
create_or_update_customer_request_from_dict = CreateOrUpdateCustomerRequest.from_dict(create_or_update_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


