# NetReportTransportTransactionsReportItem

Transactions report item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_client_login** | **str** | Api client login. Can be null. | [optional] 
**balance_after** | **float** | Balance after. | [optional] 
**balance_before** | **float** | Balance before. | [optional] 
**block_reason** | **str** | Block reason. Can be null. | [optional] 
**certificate** | [**NetReportTransportTransactionsCertificateReportItem**](NetReportTransportTransactionsCertificateReportItem.md) | Certificate. | [optional] 
**comment** | **str** | Comment. Can be null. | [optional] 
**counteragent** | **str** | Counteragent. Can be null. | [optional] 
**counteragent_type** | [**NetReportCertificateCounteragentType**](NetReportCertificateCounteragentType.md) | Counteragent type. | [optional] 
**counteragent_type_name** | **str** | Counteragent type name. Can be null. | [optional] 
**coupon** | [**NetReportTransportTransactionsCouponReportItem**](NetReportTransportTransactionsCouponReportItem.md) | Coupon. | [optional] 
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
**type** | [**NetReportTransactionType**](NetReportTransactionType.md) | Type. | [optional] 
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
from iiko_cloud_client.models.net_report_transport_transactions_report_item import NetReportTransportTransactionsReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of NetReportTransportTransactionsReportItem from a JSON string
net_report_transport_transactions_report_item_instance = NetReportTransportTransactionsReportItem.from_json(json)
# print the JSON string representation of the object
print(NetReportTransportTransactionsReportItem.to_json())

# convert the object into a dict
net_report_transport_transactions_report_item_dict = net_report_transport_transactions_report_item_instance.to_dict()
# create an instance of NetReportTransportTransactionsReportItem from a dict
net_report_transport_transactions_report_item_from_dict = NetReportTransportTransactionsReportItem.from_dict(net_report_transport_transactions_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


