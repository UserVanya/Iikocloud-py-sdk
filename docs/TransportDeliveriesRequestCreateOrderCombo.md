# TransportDeliveriesRequestCreateOrderCombo

Combo in order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Combo ID.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid(). | 
**name** | **str** | Name of combo. | 
**amount** | **int** | Quantity. | 
**price** | **float** | Price of one combo. | 
**source_id** | **str** | Combo validity ID. | 
**program_id** | **str** | Card program ID.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**size_id** | **str** | Size ID. Required if combo has a size scale.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_combo import TransportDeliveriesRequestCreateOrderCombo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderCombo from a JSON string
transport_deliveries_request_create_order_combo_instance = TransportDeliveriesRequestCreateOrderCombo.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderCombo.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_combo_dict = transport_deliveries_request_create_order_combo_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderCombo from a dict
transport_deliveries_request_create_order_combo_from_dict = TransportDeliveriesRequestCreateOrderCombo.from_dict(transport_deliveries_request_create_order_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


