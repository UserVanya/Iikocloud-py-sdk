# NetReportTransportTransactionsCertificateReportItem

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
from iiko_cloud_client.models.net_report_transport_transactions_certificate_report_item import NetReportTransportTransactionsCertificateReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of NetReportTransportTransactionsCertificateReportItem from a JSON string
net_report_transport_transactions_certificate_report_item_instance = NetReportTransportTransactionsCertificateReportItem.from_json(json)
# print the JSON string representation of the object
print(NetReportTransportTransactionsCertificateReportItem.to_json())

# convert the object into a dict
net_report_transport_transactions_certificate_report_item_dict = net_report_transport_transactions_certificate_report_item_instance.to_dict()
# create an instance of NetReportTransportTransactionsCertificateReportItem from a dict
net_report_transport_transactions_certificate_report_item_from_dict = NetReportTransportTransactionsCertificateReportItem.from_dict(net_report_transport_transactions_certificate_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


