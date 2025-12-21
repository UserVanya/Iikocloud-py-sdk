# DeliveriesCommonChequeAdditionalInfo

Cheque additional information according to russian federal law #54.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**need_receipt** | **bool** | Whether paper cheque should be printed. | 
**email** | **str** | Email to send cheque information or null if the cheque shouldn&#39;t be sent by email. | [optional] 
**settlement_place** | **str** | Settlement place. | [optional] 
**phone** | **str** | Phone to send cheque information (by sms) or null if the cheque shouldn&#39;t be sent by sms. | [optional] 
**retail_address** | **str** | Retail address.   &gt; Allowed from version &#x60;9.4.6&#x60;. | [optional] 
**is_internet_payment** | **bool** | Whether the settlement is an internet payment transaction.   &gt; Allowed from version &#x60;9.4.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_common_cheque_additional_info import DeliveriesCommonChequeAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesCommonChequeAdditionalInfo from a JSON string
deliveries_common_cheque_additional_info_instance = DeliveriesCommonChequeAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveriesCommonChequeAdditionalInfo.to_json())

# convert the object into a dict
deliveries_common_cheque_additional_info_dict = deliveries_common_cheque_additional_info_instance.to_dict()
# create an instance of DeliveriesCommonChequeAdditionalInfo from a dict
deliveries_common_cheque_additional_info_from_dict = DeliveriesCommonChequeAdditionalInfo.from_dict(deliveries_common_cheque_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


