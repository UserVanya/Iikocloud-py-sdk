# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRmsDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type_id** | **UUID** | Discount type.                 Can be obtained by &#x60;/discounts&#x60; operation. | 
**sum** | **float** | Discount/surcharge sum. | [optional] 
**selective_positions** | **List[UUID]** | Order item positions. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_rms_discount import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRmsDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRmsDiscount from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_rms_discount_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRmsDiscount.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRmsDiscount.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_rms_discount_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_rms_discount_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRmsDiscount from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_rms_discount_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRmsDiscount.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_rms_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


