# DiscountsDiscountsRequest

Request of discounts/surcharges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organization IDs that require discounts return.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.discounts_discounts_request import DiscountsDiscountsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountsDiscountsRequest from a JSON string
discounts_discounts_request_instance = DiscountsDiscountsRequest.from_json(json)
# print the JSON string representation of the object
print(DiscountsDiscountsRequest.to_json())

# convert the object into a dict
discounts_discounts_request_dict = discounts_discounts_request_instance.to_dict()
# create an instance of DiscountsDiscountsRequest from a dict
discounts_discounts_request_from_dict = DiscountsDiscountsRequest.from_dict(discounts_discounts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


