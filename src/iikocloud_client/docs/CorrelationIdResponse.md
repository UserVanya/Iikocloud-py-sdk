# CorrelationIdResponse

Wrapping object (external) for CorrelationId return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 

## Example

```python
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CorrelationIdResponse from a JSON string
correlation_id_response_instance = CorrelationIdResponse.from_json(json)
# print the JSON string representation of the object
print(CorrelationIdResponse.to_json())

# convert the object into a dict
correlation_id_response_dict = correlation_id_response_instance.to_dict()
# create an instance of CorrelationIdResponse from a dict
correlation_id_response_from_dict = CorrelationIdResponse.from_dict(correlation_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


