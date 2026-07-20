# iikocloud_client.TerminalGroupsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**awake_terminal_groups**](TerminalGroupsApi.md#awake_terminal_groups) | **POST** /api/1/terminal_groups/awake | Awake terminal groups from sleep mode.
[**check_terminal_groups_availability**](TerminalGroupsApi.md#check_terminal_groups_availability) | **POST** /api/1/terminal_groups/is_alive | Returns information on availability of group of terminals.
[**get_terminal_groups**](TerminalGroupsApi.md#get_terminal_groups) | **POST** /api/1/terminal_groups | Method that returns information on groups of delivery terminals.


# **awake_terminal_groups**
> AwakeTerminalGroupsResponse awake_terminal_groups(timeout=timeout, awake_terminal_groups_request=awake_terminal_groups_request)

Awake terminal groups from sleep mode.



 > Restriction group: `Organizations: settings`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.awake_terminal_groups_request import AwakeTerminalGroupsRequest
from iikocloud_client.models.awake_terminal_groups_response import AwakeTerminalGroupsResponse
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
    api_instance = iikocloud_client.TerminalGroupsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    awake_terminal_groups_request = iikocloud_client.AwakeTerminalGroupsRequest() # AwakeTerminalGroupsRequest |  (optional)

    try:
        # Awake terminal groups from sleep mode.
        api_response = await api_instance.awake_terminal_groups(timeout=timeout, awake_terminal_groups_request=awake_terminal_groups_request)
        print("The response of TerminalGroupsApi->awake_terminal_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalGroupsApi->awake_terminal_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **awake_terminal_groups_request** | [**AwakeTerminalGroupsRequest**](AwakeTerminalGroupsRequest.md)|  | [optional] 

### Return type

[**AwakeTerminalGroupsResponse**](AwakeTerminalGroupsResponse.md)

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

# **check_terminal_groups_availability**
> TerminalGroupsIsAliveResponse check_terminal_groups_availability(timeout=timeout, terminal_groups_is_alive_request=terminal_groups_is_alive_request)

Returns information on availability of group of terminals.



 > Restriction group: `POS: availability`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.terminal_groups_is_alive_request import TerminalGroupsIsAliveRequest
from iikocloud_client.models.terminal_groups_is_alive_response import TerminalGroupsIsAliveResponse
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
    api_instance = iikocloud_client.TerminalGroupsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    terminal_groups_is_alive_request = iikocloud_client.TerminalGroupsIsAliveRequest() # TerminalGroupsIsAliveRequest |  (optional)

    try:
        # Returns information on availability of group of terminals.
        api_response = await api_instance.check_terminal_groups_availability(timeout=timeout, terminal_groups_is_alive_request=terminal_groups_is_alive_request)
        print("The response of TerminalGroupsApi->check_terminal_groups_availability:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalGroupsApi->check_terminal_groups_availability: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **terminal_groups_is_alive_request** | [**TerminalGroupsIsAliveRequest**](TerminalGroupsIsAliveRequest.md)|  | [optional] 

### Return type

[**TerminalGroupsIsAliveResponse**](TerminalGroupsIsAliveResponse.md)

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

# **get_terminal_groups**
> TerminalGroupsResponse get_terminal_groups(timeout=timeout, terminal_groups_request=terminal_groups_request)

Method that returns information on groups of delivery terminals.



 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.terminal_groups_request import TerminalGroupsRequest
from iikocloud_client.models.terminal_groups_response import TerminalGroupsResponse
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
    api_instance = iikocloud_client.TerminalGroupsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    terminal_groups_request = iikocloud_client.TerminalGroupsRequest() # TerminalGroupsRequest |  (optional)

    try:
        # Method that returns information on groups of delivery terminals.
        api_response = await api_instance.get_terminal_groups(timeout=timeout, terminal_groups_request=terminal_groups_request)
        print("The response of TerminalGroupsApi->get_terminal_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalGroupsApi->get_terminal_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **terminal_groups_request** | [**TerminalGroupsRequest**](TerminalGroupsRequest.md)|  | [optional] 

### Return type

[**TerminalGroupsResponse**](TerminalGroupsResponse.md)

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

