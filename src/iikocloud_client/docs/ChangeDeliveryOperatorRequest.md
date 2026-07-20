# ChangeDeliveryOperatorRequest

Request for assign/change the order operator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator_id** | **UUID** | Operator to assign the order to. | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.change_delivery_operator_request import ChangeDeliveryOperatorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeDeliveryOperatorRequest from a JSON string
change_delivery_operator_request_instance = ChangeDeliveryOperatorRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeDeliveryOperatorRequest.to_json())

# convert the object into a dict
change_delivery_operator_request_dict = change_delivery_operator_request_instance.to_dict()
# create an instance of ChangeDeliveryOperatorRequest from a dict
change_delivery_operator_request_from_dict = ChangeDeliveryOperatorRequest.from_dict(change_delivery_operator_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


