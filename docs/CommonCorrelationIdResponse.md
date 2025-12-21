# CommonCorrelationIdResponse

Wrapping object (external) for CorrelationId return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 

## Example

```python
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommonCorrelationIdResponse from a JSON string
common_correlation_id_response_instance = CommonCorrelationIdResponse.from_json(json)
# print the JSON string representation of the object
print(CommonCorrelationIdResponse.to_json())

# convert the object into a dict
common_correlation_id_response_dict = common_correlation_id_response_instance.to_dict()
# create an instance of CommonCorrelationIdResponse from a dict
common_correlation_id_response_from_dict = CommonCorrelationIdResponse.from_dict(common_correlation_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


