# iikocloud_client.OrganizationsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_settings**](OrganizationsApi.md#get_organization_settings) | **POST** /api/1/organizations/settings | Returns available to api-login user organizations specified settings.
[**get_organizations**](OrganizationsApi.md#get_organizations) | **POST** /api/1/organizations | Returns organizations available to api-login user.


# **get_organization_settings**
> OrganizationsSettingsResponse get_organization_settings(timeout=timeout, organizations_settings_request=organizations_settings_request)

Returns available to api-login user organizations specified settings.



 > Restriction group: `Organizations: settings`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.organizations_settings_request import OrganizationsSettingsRequest
from iikocloud_client.models.organizations_settings_response import OrganizationsSettingsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.OrganizationsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    organizations_settings_request = iikocloud_client.OrganizationsSettingsRequest() # OrganizationsSettingsRequest |  (optional)

    try:
        # Returns available to api-login user organizations specified settings.
        api_response = await api_instance.get_organization_settings(timeout=timeout, organizations_settings_request=organizations_settings_request)
        print("The response of OrganizationsApi->get_organization_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **organizations_settings_request** | [**OrganizationsSettingsRequest**](OrganizationsSettingsRequest.md)|  | [optional] 

### Return type

[**OrganizationsSettingsResponse**](OrganizationsSettingsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

# **get_organizations**
> GetOrganizationsResponse get_organizations(timeout=timeout, get_organizations_request=get_organizations_request)

Returns organizations available to api-login user.



 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_organizations_request import GetOrganizationsRequest
from iikocloud_client.models.get_organizations_response import GetOrganizationsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.OrganizationsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_organizations_request = iikocloud_client.GetOrganizationsRequest() # GetOrganizationsRequest |  (optional)

    try:
        # Returns organizations available to api-login user.
        api_response = await api_instance.get_organizations(timeout=timeout, get_organizations_request=get_organizations_request)
        print("The response of OrganizationsApi->get_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_organizations_request** | [**GetOrganizationsRequest**](GetOrganizationsRequest.md)|  | [optional] 

### Return type

[**GetOrganizationsResponse**](GetOrganizationsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

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

