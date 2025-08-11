# iikocloud_client.AuthorizationApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_access_token_post**](AuthorizationApi.md#api1_access_token_post) | **POST** /api/1/access_token | Retrieve session key for API user.


# **api1_access_token_post**
> TransportAuthGetAccessTokenResponse api1_access_token_post(timeout=timeout, transport_auth_get_access_token_request=transport_auth_get_access_token_request)

Retrieve session key for API user.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_auth_get_access_token_request import TransportAuthGetAccessTokenRequest
from iikocloud_client.models.transport_auth_get_access_token_response import TransportAuthGetAccessTokenResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.AuthorizationApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_auth_get_access_token_request = iikocloud_client.TransportAuthGetAccessTokenRequest() # TransportAuthGetAccessTokenRequest |  (optional)

    try:
        # Retrieve session key for API user.
        api_response = await api_instance.api1_access_token_post(timeout=timeout, transport_auth_get_access_token_request=transport_auth_get_access_token_request)
        print("The response of AuthorizationApi->api1_access_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->api1_access_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_auth_get_access_token_request** | [**TransportAuthGetAccessTokenRequest**](TransportAuthGetAccessTokenRequest.md)|  | [optional] 

### Return type

[**TransportAuthGetAccessTokenResponse**](TransportAuthGetAccessTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

