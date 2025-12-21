# iikocloud_client.OrganizationsApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_post**](OrganizationsApi.md#organizations_post) | **POST** /organizations | Returns organizations available to api-login user.
[**organizations_settings_post**](OrganizationsApi.md#organizations_settings_post) | **POST** /organizations/settings | Returns available to api-login user organizations specified settings.


# **organizations_post**
> IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse organizations_post(timeout=timeout, iiko_transport_public_api_contracts_organizations_get_organizations_request=iiko_transport_public_api_contracts_organizations_get_organizations_request)

Returns organizations available to api-login user.



 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_get_organizations_request import IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_get_organizations_response import IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.OrganizationsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_organizations_get_organizations_request = iikocloud_client.IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest() # IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest |  (optional)

    try:
        # Returns organizations available to api-login user.
        api_response = await api_instance.organizations_post(timeout=timeout, iiko_transport_public_api_contracts_organizations_get_organizations_request=iiko_transport_public_api_contracts_organizations_get_organizations_request)
        print("The response of OrganizationsApi->organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_organizations_get_organizations_request** | [**IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest**](IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse**](IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse.md)

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

# **organizations_settings_post**
> IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse organizations_settings_post(timeout=timeout, iiko_transport_public_api_contracts_organizations_organizations_settings_request=iiko_transport_public_api_contracts_organizations_organizations_settings_request)

Returns available to api-login user organizations specified settings.



 > Restriction group: `Organizations: settings`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_organizations_settings_request import IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_organizations_settings_response import IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.OrganizationsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_organizations_organizations_settings_request = iikocloud_client.IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest() # IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest |  (optional)

    try:
        # Returns available to api-login user organizations specified settings.
        api_response = await api_instance.organizations_settings_post(timeout=timeout, iiko_transport_public_api_contracts_organizations_organizations_settings_request=iiko_transport_public_api_contracts_organizations_organizations_settings_request)
        print("The response of OrganizationsApi->organizations_settings_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->organizations_settings_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_organizations_organizations_settings_request** | [**IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest**](IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse**](IikoTransportPublicApiContractsOrganizationsOrganizationsSettingsResponse.md)

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

