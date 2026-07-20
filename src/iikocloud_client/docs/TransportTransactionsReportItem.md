# TransportTransactionsReportItem

Transactions report item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_client_login** | **str** | Api client login. Can be null. | [optional] 
**balance_after** | **float** | Balance after. | [optional] 
**balance_before** | **float** | Balance before. | [optional] 
**block_reason** | **str** | Block reason. Can be null. | [optional] 
**certificate** | [**TransportTransactionsCertificateReportItem**](TransportTransactionsCertificateReportItem.md) | Certificate. | [optional] 
**comment** | **str** | Comment. Can be null. | [optional] 
**counteragent** | **str** | Counteragent. Can be null. | [optional] 
**counteragent_type** | [**CertificateCounteragentType**](CertificateCounteragentType.md) | Counteragent type. | [optional] 
**counteragent_type_name** | **str** | Counteragent type name. Can be null. | [optional] 
**coupon** | [**TransportTransactionsCouponReportItem**](TransportTransactionsCouponReportItem.md) | Coupon. | [optional] 
**emitent_name** | **str** | Emitent name. Can be null. | [optional] 
**id** | **UUID** | Id. | 
**is_delivery** | **bool** | Is delivery. | [optional] 
**is_ignored** | **bool** | Is ignored. | [optional] 
**loyalty_user** | **str** | Loyalty user. Can be null. | [optional] 
**marketing_campaign_id** | **UUID** | Marketing campaign id. | [optional] 
**nominal** | **float** | Nominal. | [optional] 
**order_number** | **int** | Order number. | [optional] 
**order_sum** | **float** | Order sum. | [optional] 
**organization_id** | **UUID** | Organization id. | 
**pos_balance_before** | **float** | Pos balance before. | [optional] 
**pos_order_id** | **UUID** | Pos order id. | [optional] 
**program_id** | **UUID** | Program id. | [optional] 
**revision** | **int** | Revision. | 
**sum** | **float** | Sum. | [optional] 
**terminal_group_id** | **UUID** | Terminal group id. | [optional] 
**type** | [**TransactionType**](TransactionType.md) | Type. | [optional] 
**type_name** | **str** | Type name. Can be null. | [optional] 
**wallet_id** | **UUID** | Wallet id. | [optional] 
**when_created** | **str** | When created. In UTC. | [optional] 
**when_created_order** | **str** | When created order. In UTC. | [optional] 

## Example

```python
from iikocloud_client.models.transport_transactions_report_item import TransportTransactionsReportItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTransactionsReportItem from a JSON string
transport_transactions_report_item_instance = TransportTransactionsReportItem.from_json(json)
# print the JSON string representation of the object
print(TransportTransactionsReportItem.to_json())

# convert the object into a dict
transport_transactions_report_item_dict = transport_transactions_report_item_instance.to_dict()
# create an instance of TransportTransactionsReportItem from a dict
transport_transactions_report_item_from_dict = TransportTransactionsReportItem.from_dict(transport_transactions_report_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


