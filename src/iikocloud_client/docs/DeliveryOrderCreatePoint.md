# DeliveryOrderCreatePoint

Delivery location details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**DeliveryOrderCreateAddress**](DeliveryOrderCreateAddress.md) | Order delivery address.                &gt; The use of type **City** is allowed if the parameter **addressFormatType &#x3D;&#x3D; City**.                &gt; Can be obtained by &#x60;/api/1/organizations&#x60; or &#x60;/api/1/organizations/settings&#x60; operations (&#x60;addressFormatType&#x60; parameter). | [optional] 
**comment** | **str** | Additional information. | [optional] 
**coordinates** | [**DeliveryCoordinates**](DeliveryCoordinates.md) | Delivery address coordinates.  &gt; Allowed from version &#x60;7.7.3&#x60;. | [optional] 
**external_cartography_id** | **str** | Delivery location custom code in customer&#39;s API system. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_create_point import DeliveryOrderCreatePoint

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreatePoint from a JSON string
delivery_order_create_point_instance = DeliveryOrderCreatePoint.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreatePoint.to_json())

# convert the object into a dict
delivery_order_create_point_dict = delivery_order_create_point_instance.to_dict()
# create an instance of DeliveryOrderCreatePoint from a dict
delivery_order_create_point_from_dict = DeliveryOrderCreatePoint.from_dict(delivery_order_create_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


