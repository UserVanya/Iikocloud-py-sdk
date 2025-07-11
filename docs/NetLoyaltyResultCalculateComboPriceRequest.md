# NetLoyaltyResultCalculateComboPriceRequest

Calculate combo price request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TransportDeliveriesRequestCreateOrderOrderItem]**](TransportDeliveriesRequestCreateOrderOrderItem.md) | Items with modifiers included in combo. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_loyalty_result_calculate_combo_price_request import NetLoyaltyResultCalculateComboPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultCalculateComboPriceRequest from a JSON string
net_loyalty_result_calculate_combo_price_request_instance = NetLoyaltyResultCalculateComboPriceRequest.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultCalculateComboPriceRequest.to_json())

# convert the object into a dict
net_loyalty_result_calculate_combo_price_request_dict = net_loyalty_result_calculate_combo_price_request_instance.to_dict()
# create an instance of NetLoyaltyResultCalculateComboPriceRequest from a dict
net_loyalty_result_calculate_combo_price_request_from_dict = NetLoyaltyResultCalculateComboPriceRequest.from_dict(net_loyalty_result_calculate_combo_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


