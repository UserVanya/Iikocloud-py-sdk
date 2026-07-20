# GetAccessTokenResponse

Response to authentication token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**token** | **str** | Authentication token. The standard token lifetime is 1 hour. | 

## Example

```python
from iikocloud_client.models.get_access_token_response import GetAccessTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccessTokenResponse from a JSON string
get_access_token_response_instance = GetAccessTokenResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccessTokenResponse.to_json())

# convert the object into a dict
get_access_token_response_dict = get_access_token_response_instance.to_dict()
# create an instance of GetAccessTokenResponse from a dict
get_access_token_response_from_dict = GetAccessTokenResponse.from_dict(get_access_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


