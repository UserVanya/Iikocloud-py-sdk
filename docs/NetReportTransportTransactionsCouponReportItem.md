# NetReportTransportTransactionsCouponReportItem

Transactions report item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number. Can be null. | [optional] 
**series** | **str** | Series. Can be null. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_report_transport_transactions_coupon_report_item import NetReportTransportTransactionsCouponReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of NetReportTransportTransactionsCouponReportItem from a JSON string
net_report_transport_transactions_coupon_report_item_instance = NetReportTransportTransactionsCouponReportItem.from_json(json)
# print the JSON string representation of the object
print(NetReportTransportTransactionsCouponReportItem.to_json())

# convert the object into a dict
net_report_transport_transactions_coupon_report_item_dict = net_report_transport_transactions_coupon_report_item_instance.to_dict()
# create an instance of NetReportTransportTransactionsCouponReportItem from a dict
net_report_transport_transactions_coupon_report_item_from_dict = NetReportTransportTransactionsCouponReportItem.from_dict(net_report_transport_transactions_coupon_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


