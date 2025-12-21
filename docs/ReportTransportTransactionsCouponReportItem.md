# ReportTransportTransactionsCouponReportItem

Transactions report item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number. Can be null. | [optional] 
**series** | **str** | Series. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.report_transport_transactions_coupon_report_item import ReportTransportTransactionsCouponReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTransportTransactionsCouponReportItem from a JSON string
report_transport_transactions_coupon_report_item_instance = ReportTransportTransactionsCouponReportItem.from_json(json)
# print the JSON string representation of the object
print(ReportTransportTransactionsCouponReportItem.to_json())

# convert the object into a dict
report_transport_transactions_coupon_report_item_dict = report_transport_transactions_coupon_report_item_instance.to_dict()
# create an instance of ReportTransportTransactionsCouponReportItem from a dict
report_transport_transactions_coupon_report_item_from_dict = ReportTransportTransactionsCouponReportItem.from_dict(report_transport_transactions_coupon_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


