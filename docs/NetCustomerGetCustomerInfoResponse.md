# NetCustomerGetCustomerInfoResponse

Get customer info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Guest id. | [optional] 
**referrer_id** | **str** | Guest referrer id. | [optional] 
**name** | **str** | Guest name. Can be null. | [optional] 
**surname** | **str** | Guest surname. Can be null. | [optional] 
**middle_name** | **str** | Guest middle name. Can be null. | [optional] 
**comment** | **str** | Guest comment. Can be null. | [optional] 
**phone** | **str** | Main customer&#39;s phone. Can be null. | [optional] 
**culture_name** | **str** | Guest culture name. Can be null. | [optional] 
**birthday** | **str** | Guest birthday. | [optional] 
**email** | **str** | Guest email. Can be null. | [optional] 
**sex** | [**NetCustomerIikoNetUserSex**](NetCustomerIikoNetUserSex.md) | Sex.  &lt;br&gt;0 - not specified,&lt;br /&gt;1 - male,&lt;br /&gt;2 - female. | [optional] 
**consent_status** | [**NetCustomerPersonalDataConsentStatus**](NetCustomerPersonalDataConsentStatus.md) | Guest consent status.  &lt;br&gt;0 - unknown,&lt;br /&gt;1 - given,&lt;br /&gt;2 - revoked. | [optional] 
**anonymized** | **bool** | Guest anonymized. | [optional] 
**cards** | [**List[NetCustomerGuestCardInfo]**](NetCustomerGuestCardInfo.md) | Customer&#39;s cards. | [optional] 
**categories** | [**List[NetCustomerGuestCategoryShortInfo]**](NetCustomerGuestCategoryShortInfo.md) | Customer categories. | [optional] 
**wallet_balances** | [**List[NetCustomerGuestBalanceInfo]**](NetCustomerGuestBalanceInfo.md) | Customer&#39;s user wallets. Contains bonus balances of different loyalty programs. | [optional] 
**user_data** | **str** | Technical user data, customizable by restaurateur. Can be null. | [optional] 
**should_receive_promo_actions_info** | **bool** | Customer get promo messages (email, sms). If null - unknown. | [optional] 
**should_receive_loyalty_info** | **bool** | Guest should receive loyalty info. | [optional] 
**should_receive_order_status_info** | **bool** | Guest should receive order status info. | [optional] 
**personal_data_consent_from** | **str** | Guest personal data consent from. | [optional] 
**personal_data_consent_to** | **str** | Guest personal data consent to. | [optional] 
**personal_data_processing_from** | **str** | Guest personal data processing from. | [optional] 
**personal_data_processing_to** | **str** | Guest personal data processing to. | [optional] 
**is_deleted** | **bool** | Customer marked as deleted. | [optional] 
**when_registered** | **str** | Registration date. | [optional] 
**last_processed_order_date** | **str** | Last order date. | [optional] 
**first_order_date** | **str** | First order date. | [optional] 
**last_visited_organization_id** | **str** | Guest last visited organization id. | [optional] 
**registration_organization_id** | **str** | Guest registration organization id. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_customer_get_customer_info_response import NetCustomerGetCustomerInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetCustomerGetCustomerInfoResponse from a JSON string
net_customer_get_customer_info_response_instance = NetCustomerGetCustomerInfoResponse.from_json(json)
# print the JSON string representation of the object
print(NetCustomerGetCustomerInfoResponse.to_json())

# convert the object into a dict
net_customer_get_customer_info_response_dict = net_customer_get_customer_info_response_instance.to_dict()
# create an instance of NetCustomerGetCustomerInfoResponse from a dict
net_customer_get_customer_info_response_from_dict = NetCustomerGetCustomerInfoResponse.from_dict(net_customer_get_customer_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


