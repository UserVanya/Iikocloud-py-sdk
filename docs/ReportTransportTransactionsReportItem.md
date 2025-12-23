# ReportTransportTransactionsReportItem

Transactions report item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_client_login** | **str** | Api client login. Can be null. | [optional] 
**balance_after** | **float** | Balance after. | [optional] 
**balance_before** | **float** | Balance before. | [optional] 
**block_reason** | **str** | Block reason. Can be null. | [optional] 
**certificate** | [**ReportTransportTransactionsCertificateReportItem**](ReportTransportTransactionsCertificateReportItem.md) | Certificate. | [optional] 
**comment** | **str** | Comment. Can be null. | [optional] 
**counteragent** | **str** | Counteragent. Can be null. | [optional] 
**counteragent_type** | [**ReportCertificateCounteragentType**](ReportCertificateCounteragentType.md) | Counteragent type. | [optional] 
**counteragent_type_name** | **str** | Counteragent type name. Can be null. | [optional] 
**coupon** | [**ReportTransportTransactionsCouponReportItem**](ReportTransportTransactionsCouponReportItem.md) | Coupon. | [optional] 
**emitent_name** | **str** | Emitent name. Can be null. | [optional] 
**loyalty_user** | **str** | Loyalty user. Can be null. | [optional] 
**marketing_campaign_id** | **str** | Marketing campaign id. | [optional] 
**nominal** | **float** | Nominal. | [optional] 
**order_number** | **int** | Order number. | [optional] 
**order_sum** | **float** | Order sum. | [optional] 
**organization_id** | **str** | Organization id. | 
**pos_balance_before** | **float** | Pos balance before. | [optional] 
**program_id** | **str** | Program id. | [optional] 
**sum** | **float** | Sum. | [optional] 
**type** | [**ReportTransactionType**](ReportTransactionType.md) | Type. | [optional] 
**type_name** | **str** | Type name. Can be null. | [optional] 
**wallet_id** | **str** | Wallet id. | [optional] 
**when_created** | **datetime** | When created. | [optional] 
**when_created_order** | **datetime** | When created order. | [optional] 
**id** | **str** | Id. | 
**is_delivery** | **bool** | Is delivery. | [optional] 
**is_ignored** | **bool** | Is ignored. | [optional] 
**pos_order_id** | **str** | Pos order id. | [optional] 
**revision** | **int** | Revision. | 
**terminal_group_id** | **str** | Terminal group id. | [optional] 

## Example

```python
from iikocloud_client.models.report_transport_transactions_report_item import ReportTransportTransactionsReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReportTransportTransactionsReportItem from a JSON string
report_transport_transactions_report_item_instance = ReportTransportTransactionsReportItem.from_json(json)
# print the JSON string representation of the object
print(ReportTransportTransactionsReportItem.to_json())

# convert the object into a dict
report_transport_transactions_report_item_dict = report_transport_transactions_report_item_instance.to_dict()
# create an instance of ReportTransportTransactionsReportItem from a dict
report_transport_transactions_report_item_from_dict = ReportTransportTransactionsReportItem.from_dict(report_transport_transactions_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


