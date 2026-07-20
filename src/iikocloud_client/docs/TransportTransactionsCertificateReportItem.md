# TransportTransactionsCertificateReportItem

Transactions report item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number. Can be null. | [optional] 
**series** | **str** | Series. Can be null. | [optional] 
**status_name** | **str** | Status name. Can be null. | [optional] 
**type_name** | **str** | Type name. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.transport_transactions_certificate_report_item import TransportTransactionsCertificateReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTransactionsCertificateReportItem from a JSON string
transport_transactions_certificate_report_item_instance = TransportTransactionsCertificateReportItem.from_json(json)
# print the JSON string representation of the object
print(TransportTransactionsCertificateReportItem.to_json())

# convert the object into a dict
transport_transactions_certificate_report_item_dict = transport_transactions_certificate_report_item_instance.to_dict()
# create an instance of TransportTransactionsCertificateReportItem from a dict
transport_transactions_certificate_report_item_from_dict = TransportTransactionsCertificateReportItem.from_dict(transport_transactions_certificate_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


