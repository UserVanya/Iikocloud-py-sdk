# TransportDiscountsDiscountsRequest

Request of discounts/surcharges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organization IDs that require discounts return.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_discounts_discounts_request import TransportDiscountsDiscountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDiscountsDiscountsRequest from a JSON string
transport_discounts_discounts_request_instance = TransportDiscountsDiscountsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportDiscountsDiscountsRequest.to_json())

# convert the object into a dict
transport_discounts_discounts_request_dict = transport_discounts_discounts_request_instance.to_dict()
# create an instance of TransportDiscountsDiscountsRequest from a dict
transport_discounts_discounts_request_from_dict = TransportDiscountsDiscountsRequest.from_dict(transport_discounts_discounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


