# GetCustomerInfoResponse

Get customer info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymized** | **bool** | Guest anonymized. | [optional] 
**birthday** | **str** | Guest birthday. | [optional] 
**cards** | [**List[GuestCardInfo]**](GuestCardInfo.md) | Customer&#39;s cards. | [optional] 
**categories** | [**List[GuestCategoryShortInfo]**](GuestCategoryShortInfo.md) | Customer categories. | [optional] 
**comment** | **str** | Guest comment. Can be null. | [optional] 
**consent_status** | [**PersonalDataConsentStatus**](PersonalDataConsentStatus.md) | Guest consent status.  &lt;br&gt;0 - unknown,&lt;br /&gt;1 - given,&lt;br /&gt;2 - revoked. | [optional] 
**culture_name** | **str** | Guest culture name. Can be null. | [optional] 
**email** | **str** | Guest email. Can be null. | [optional] 
**first_order_date** | **str** | First order date. | [optional] 
**id** | **UUID** | Guest id. | [optional] 
**is_deleted** | **bool** | Customer marked as deleted. | [optional] 
**last_processed_order_date** | **str** | Last order date. | [optional] 
**last_visited_organization_id** | **UUID** | Guest last visited organization id. | [optional] 
**middle_name** | **str** | Guest middle name. Can be null. | [optional] 
**name** | **str** | Guest name. Can be null. | [optional] 
**personal_data_consent_from** | **str** | Guest personal data consent from. | [optional] 
**personal_data_consent_to** | **str** | Guest personal data consent to. | [optional] 
**personal_data_processing_from** | **str** | Guest personal data processing from. | [optional] 
**personal_data_processing_to** | **str** | Guest personal data processing to. | [optional] 
**phone** | **str** | Main customer&#39;s phone. Can be null. | [optional] 
**referrer_id** | **UUID** | Guest referrer id. | [optional] 
**registration_organization_id** | **UUID** | Guest registration organization id. | [optional] 
**sex** | [**IikoNetUserSex**](IikoNetUserSex.md) | Sex.  &lt;br&gt;0 - not specified,&lt;br /&gt;1 - male,&lt;br /&gt;2 - female. | [optional] 
**should_receive_loyalty_info** | **bool** | Guest should receive loyalty info. | [optional] 
**should_receive_order_status_info** | **bool** | Guest should receive order status info. | [optional] 
**should_receive_promo_actions_info** | **bool** | Customer get promo messages (email, sms). If null - unknown. | [optional] 
**surname** | **str** | Guest surname. Can be null. | [optional] 
**user_data** | **str** | Technical user data, customizable by restaurateur. Can be null. | [optional] 
**wallet_balances** | [**List[GuestBalanceInfo]**](GuestBalanceInfo.md) | Customer&#39;s user wallets. Contains bonus balances of different loyalty programs. | [optional] 
**when_registered** | **str** | Registration date. | [optional] 

## Example

```python
from iikocloud_client.models.get_customer_info_response import GetCustomerInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomerInfoResponse from a JSON string
get_customer_info_response_instance = GetCustomerInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetCustomerInfoResponse.to_json())

# convert the object into a dict
get_customer_info_response_dict = get_customer_info_response_instance.to_dict()
# create an instance of GetCustomerInfoResponse from a dict
get_customer_info_response_from_dict = GetCustomerInfoResponse.from_dict(get_customer_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


