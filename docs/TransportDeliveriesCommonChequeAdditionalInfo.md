# TransportDeliveriesCommonChequeAdditionalInfo

Cheque additional information according to russian federal law #54.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**need_receipt** | **bool** | Whether paper cheque should be printed. | 
**email** | **str** | Email to send cheque information or null if the cheque shouldn&#39;t be sent by email. | [optional] 
**settlement_place** | **str** | Settlement place. | [optional] 
**phone** | **str** | Phone to send cheque information (by sms) or null if the cheque shouldn&#39;t be sent by sms. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_common_cheque_additional_info import TransportDeliveriesCommonChequeAdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesCommonChequeAdditionalInfo from a JSON string
transport_deliveries_common_cheque_additional_info_instance = TransportDeliveriesCommonChequeAdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesCommonChequeAdditionalInfo.to_json())

# convert the object into a dict
transport_deliveries_common_cheque_additional_info_dict = transport_deliveries_common_cheque_additional_info_instance.to_dict()
# create an instance of TransportDeliveriesCommonChequeAdditionalInfo from a dict
transport_deliveries_common_cheque_additional_info_from_dict = TransportDeliveriesCommonChequeAdditionalInfo.from_dict(transport_deliveries_common_cheque_additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


