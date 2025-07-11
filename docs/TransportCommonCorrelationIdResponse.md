# TransportCommonCorrelationIdResponse

Wrapping object (external) for CorrelationId return.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 

## Example

```python
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommonCorrelationIdResponse from a JSON string
transport_common_correlation_id_response_instance = TransportCommonCorrelationIdResponse.from_json(json)
# print the JSON string representation of the object
print(TransportCommonCorrelationIdResponse.to_json())

# convert the object into a dict
transport_common_correlation_id_response_dict = transport_common_correlation_id_response_instance.to_dict()
# create an instance of TransportCommonCorrelationIdResponse from a dict
transport_common_correlation_id_response_from_dict = TransportCommonCorrelationIdResponse.from_dict(transport_common_correlation_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


