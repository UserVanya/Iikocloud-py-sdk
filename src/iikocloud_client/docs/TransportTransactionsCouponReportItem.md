# TransportTransactionsCouponReportItem

Transactions report item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number. Can be null. | [optional] 
**series** | **str** | Series. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.transport_transactions_coupon_report_item import TransportTransactionsCouponReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTransactionsCouponReportItem from a JSON string
transport_transactions_coupon_report_item_instance = TransportTransactionsCouponReportItem.from_json(json)
# print the JSON string representation of the object
print(TransportTransactionsCouponReportItem.to_json())

# convert the object into a dict
transport_transactions_coupon_report_item_dict = transport_transactions_coupon_report_item_instance.to_dict()
# create an instance of TransportTransactionsCouponReportItem from a dict
transport_transactions_coupon_report_item_from_dict = TransportTransactionsCouponReportItem.from_dict(transport_transactions_coupon_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


