# ReportTransportTransactionsCertificateReportItem

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
from iikocloud_client.models.report_transport_transactions_certificate_report_item import ReportTransportTransactionsCertificateReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTransportTransactionsCertificateReportItem from a JSON string
report_transport_transactions_certificate_report_item_instance = ReportTransportTransactionsCertificateReportItem.from_json(json)
# print the JSON string representation of the object
print(ReportTransportTransactionsCertificateReportItem.to_json())

# convert the object into a dict
report_transport_transactions_certificate_report_item_dict = report_transport_transactions_certificate_report_item_instance.to_dict()
# create an instance of ReportTransportTransactionsCertificateReportItem from a dict
report_transport_transactions_certificate_report_item_from_dict = ReportTransportTransactionsCertificateReportItem.from_dict(report_transport_transactions_certificate_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


