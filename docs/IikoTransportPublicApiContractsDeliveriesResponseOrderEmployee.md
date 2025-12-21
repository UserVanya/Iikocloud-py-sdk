# IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee

Employee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 
**phone** | **str** | Phone. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_employee import IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee from a JSON string
iiko_transport_public_api_contracts_deliveries_response_order_employee_instance = IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_response_order_employee_dict = iiko_transport_public_api_contracts_deliveries_response_order_employee_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee from a dict
iiko_transport_public_api_contracts_deliveries_response_order_employee_from_dict = IikoTransportPublicApiContractsDeliveriesResponseOrderEmployee.from_dict(iiko_transport_public_api_contracts_deliveries_response_order_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


