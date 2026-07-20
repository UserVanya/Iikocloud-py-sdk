# iikocloud_client.AuthorizationApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthorizationApi.md#authenticate) | **POST** /api/1/access_token | Retrieve session key for API user.
[**authenticate_v2**](AuthorizationApi.md#authenticate_v2) | **POST** /api/v2/access_token | Retrieve session key for API access (v2)


# **authenticate**
> GetAccessTokenResponse authenticate(timeout=timeout, get_access_token_request=get_access_token_request)

Retrieve session key for API user.



> Deprecated: use `/api/v2/access_token` instead.

### Example


```python
import iikocloud_client
from iikocloud_client.models.get_access_token_request import GetAccessTokenRequest
from iikocloud_client.models.get_access_token_response import GetAccessTokenResponse
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
    get_access_token_request = iikocloud_client.GetAccessTokenRequest() # GetAccessTokenRequest |  (optional)

    try:
        # Retrieve session key for API user.
        api_response = await api_instance.authenticate(timeout=timeout, get_access_token_request=get_access_token_request)
        print("The response of AuthorizationApi->authenticate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->authenticate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_access_token_request** | [**GetAccessTokenRequest**](GetAccessTokenRequest.md)|  | [optional] 

### Return type

[**GetAccessTokenResponse**](GetAccessTokenResponse.md)

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
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_v2**
> GetAccessTokenV2Response authenticate_v2(timeout=timeout, get_access_token_v2_request=get_access_token_v2_request)

Retrieve session key for API access (v2)

Authenticates an application and returns a short-lived JWT token for subsequent API calls.
            
**Getting started:**
1. Register at https://public-api.iikoweb.ru/portal and fill in your company details.
2. Create an application — you will receive an `appId` and a one-time `clientSecret`.
3. In iikoWeb → "Integrations" → "API Keys", generate an API key.
4. Call this method with all three credentials.
5. Use the returned `token` as a Bearer token in the `Authorization` header of all
   subsequent API requests: `Authorization: Bearer {token}`.
**Token lifetime:** the token is valid for **1 hour**. The exact expiration is encoded
in the JWT `exp` claim. Request a new token before the current one expires — there is
no refresh token flow.

### Example


```python
import iikocloud_client
from iikocloud_client.models.get_access_token_v2_request import GetAccessTokenV2Request
from iikocloud_client.models.get_access_token_v2_response import GetAccessTokenV2Response
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
    get_access_token_v2_request = iikocloud_client.GetAccessTokenV2Request() # GetAccessTokenV2Request |  (optional)

    try:
        # Retrieve session key for API access (v2)
        api_response = await api_instance.authenticate_v2(timeout=timeout, get_access_token_v2_request=get_access_token_v2_request)
        print("The response of AuthorizationApi->authenticate_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->authenticate_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_access_token_v2_request** | [**GetAccessTokenV2Request**](GetAccessTokenV2Request.md)|  | [optional] 

### Return type

[**GetAccessTokenV2Response**](GetAccessTokenV2Response.md)

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
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

