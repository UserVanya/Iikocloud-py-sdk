# iiko_cloud_client.WebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_webhooks_settings_post**](WebhooksApi.md#api1_webhooks_settings_post) | **POST** /api/1/webhooks/settings | Get webhooks settings for specified organization and authorized API login.
[**api1_webhooks_update_settings_post**](WebhooksApi.md#api1_webhooks_update_settings_post) | **POST** /api/1/webhooks/update_settings | Update webhooks settings for specified organization and authorized API login.


# **api1_webhooks_settings_post**
> TransportWebHooksGetWebHookSettingsResponse api1_webhooks_settings_post(authorization, timeout=timeout, transport_web_hooks_get_web_hook_settings_request=transport_web_hooks_get_web_hook_settings_request)

Get webhooks settings for specified organization and authorized API login.



 > Restriction group: `Organizations: settings`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_web_hooks_get_web_hook_settings_request import TransportWebHooksGetWebHookSettingsRequest
from iiko_cloud_client.models.transport_web_hooks_get_web_hook_settings_response import TransportWebHooksGetWebHookSettingsResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.WebhooksApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_web_hooks_get_web_hook_settings_request = iiko_cloud_client.TransportWebHooksGetWebHookSettingsRequest() # TransportWebHooksGetWebHookSettingsRequest |  (optional)

    try:
        # Get webhooks settings for specified organization and authorized API login.
        api_response = await api_instance.api1_webhooks_settings_post(authorization, timeout=timeout, transport_web_hooks_get_web_hook_settings_request=transport_web_hooks_get_web_hook_settings_request)
        print("The response of WebhooksApi->api1_webhooks_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api1_webhooks_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_web_hooks_get_web_hook_settings_request** | [**TransportWebHooksGetWebHookSettingsRequest**](TransportWebHooksGetWebHookSettingsRequest.md)|  | [optional] 

### Return type

[**TransportWebHooksGetWebHookSettingsResponse**](TransportWebHooksGetWebHookSettingsResponse.md)

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

# **api1_webhooks_update_settings_post**
> TransportCommonCorrelationIdResponse api1_webhooks_update_settings_post(authorization, timeout=timeout, transport_web_hooks_update_web_hook_settings_request=transport_web_hooks_update_web_hook_settings_request)

Update webhooks settings for specified organization and authorized API login.



 > Restriction group: `Organizations: settings`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_web_hooks_update_web_hook_settings_request import TransportWebHooksUpdateWebHookSettingsRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.WebhooksApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_web_hooks_update_web_hook_settings_request = iiko_cloud_client.TransportWebHooksUpdateWebHookSettingsRequest() # TransportWebHooksUpdateWebHookSettingsRequest |  (optional)

    try:
        # Update webhooks settings for specified organization and authorized API login.
        api_response = await api_instance.api1_webhooks_update_settings_post(authorization, timeout=timeout, transport_web_hooks_update_web_hook_settings_request=transport_web_hooks_update_web_hook_settings_request)
        print("The response of WebhooksApi->api1_webhooks_update_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api1_webhooks_update_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_web_hooks_update_web_hook_settings_request** | [**TransportWebHooksUpdateWebHookSettingsRequest**](TransportWebHooksUpdateWebHookSettingsRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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

