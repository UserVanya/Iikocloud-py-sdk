# ChequeAdditionalInfo

Cheque additional information according to russian federal law #54.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email to send cheque information or null if the cheque shouldn&#39;t be sent by email. | [optional] 
**is_internet_payment** | **bool** | Whether the settlement is an internet payment transaction.   &gt; Allowed from version &#x60;9.4.6&#x60;. | [optional] 
**need_receipt** | **bool** | Whether paper cheque should be printed. | 
**phone** | **str** | Phone to send cheque information (by sms) or null if the cheque shouldn&#39;t be sent by sms. | [optional] 
**retail_address** | **str** | Retail address.   &gt; Allowed from version &#x60;9.4.6&#x60;. | [optional] 
**settlement_place** | **str** | Settlement place. | [optional] 

## Example

```python
from iikocloud_client.models.cheque_additional_info import ChequeAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ChequeAdditionalInfo from a JSON string
cheque_additional_info_instance = ChequeAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(ChequeAdditionalInfo.to_json())

# convert the object into a dict
cheque_additional_info_dict = cheque_additional_info_instance.to_dict()
# create an instance of ChequeAdditionalInfo from a dict
cheque_additional_info_from_dict = ChequeAdditionalInfo.from_dict(cheque_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


