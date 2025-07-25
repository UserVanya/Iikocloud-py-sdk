# iikocloud_client.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_organizations_post**](OrganizationsApi.md#api1_organizations_post) | **POST** /api/1/organizations | Returns organizations available to api-login user.
[**api1_organizations_settings_post**](OrganizationsApi.md#api1_organizations_settings_post) | **POST** /api/1/organizations/settings | Returns available to api-login user organizations specified settings.


# **api1_organizations_post**
> TransportOrganizationsGetOrganizationsResponse api1_organizations_post(authorization, timeout=timeout, transport_organizations_get_organizations_request=transport_organizations_get_organizations_request)

Returns organizations available to api-login user.



 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_organizations_get_organizations_request import TransportOrganizationsGetOrganizationsRequest
from iikocloud_client.models.transport_organizations_get_organizations_response import TransportOrganizationsGetOrganizationsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.OrganizationsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_organizations_get_organizations_request = iikocloud_client.TransportOrganizationsGetOrganizationsRequest() # TransportOrganizationsGetOrganizationsRequest |  (optional)

    try:
        # Returns organizations available to api-login user.
        api_response = await api_instance.api1_organizations_post(authorization, timeout=timeout, transport_organizations_get_organizations_request=transport_organizations_get_organizations_request)
        print("The response of OrganizationsApi->api1_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api1_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_organizations_get_organizations_request** | [**TransportOrganizationsGetOrganizationsRequest**](TransportOrganizationsGetOrganizationsRequest.md)|  | [optional] 

### Return type

[**TransportOrganizationsGetOrganizationsResponse**](TransportOrganizationsGetOrganizationsResponse.md)

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

# **api1_organizations_settings_post**
> TransportOrganizationsOrganizationsSettingsResponse api1_organizations_settings_post(authorization, timeout=timeout, transport_organizations_organizations_settings_request=transport_organizations_organizations_settings_request)

Returns available to api-login user organizations specified settings.



 > Restriction group: `Organizations: settings`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_organizations_organizations_settings_request import TransportOrganizationsOrganizationsSettingsRequest
from iikocloud_client.models.transport_organizations_organizations_settings_response import TransportOrganizationsOrganizationsSettingsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.OrganizationsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_organizations_organizations_settings_request = iikocloud_client.TransportOrganizationsOrganizationsSettingsRequest() # TransportOrganizationsOrganizationsSettingsRequest |  (optional)

    try:
        # Returns available to api-login user organizations specified settings.
        api_response = await api_instance.api1_organizations_settings_post(authorization, timeout=timeout, transport_organizations_organizations_settings_request=transport_organizations_organizations_settings_request)
        print("The response of OrganizationsApi->api1_organizations_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->api1_organizations_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_organizations_organizations_settings_request** | [**TransportOrganizationsOrganizationsSettingsRequest**](TransportOrganizationsOrganizationsSettingsRequest.md)|  | [optional] 

### Return type

[**TransportOrganizationsOrganizationsSettingsResponse**](TransportOrganizationsOrganizationsSettingsResponse.md)

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

