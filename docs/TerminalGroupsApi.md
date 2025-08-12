# iikocloud_client.TerminalGroupsApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**terminal_groups_awake_post**](TerminalGroupsApi.md#terminal_groups_awake_post) | **POST** /terminal_groups/awake | Awake terminal groups from sleep mode.
[**terminal_groups_is_alive_post**](TerminalGroupsApi.md#terminal_groups_is_alive_post) | **POST** /terminal_groups/is_alive | Returns information on availability of group of terminals.
[**terminal_groups_post**](TerminalGroupsApi.md#terminal_groups_post) | **POST** /terminal_groups | Method that returns information on groups of delivery terminals.


# **terminal_groups_awake_post**
> TransportTerminalsAwakeTerminalGroupsResponse terminal_groups_awake_post(timeout=timeout, transport_terminals_awake_terminal_groups_request=transport_terminals_awake_terminal_groups_request)

Awake terminal groups from sleep mode.



 > Restriction group: `Organizations: settings`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_terminals_awake_terminal_groups_request import TransportTerminalsAwakeTerminalGroupsRequest
from iikocloud_client.models.transport_terminals_awake_terminal_groups_response import TransportTerminalsAwakeTerminalGroupsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.TerminalGroupsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_terminals_awake_terminal_groups_request = iikocloud_client.TransportTerminalsAwakeTerminalGroupsRequest() # TransportTerminalsAwakeTerminalGroupsRequest |  (optional)

    try:
        # Awake terminal groups from sleep mode.
        api_response = await api_instance.terminal_groups_awake_post(timeout=timeout, transport_terminals_awake_terminal_groups_request=transport_terminals_awake_terminal_groups_request)
        print("The response of TerminalGroupsApi->terminal_groups_awake_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalGroupsApi->terminal_groups_awake_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_terminals_awake_terminal_groups_request** | [**TransportTerminalsAwakeTerminalGroupsRequest**](TransportTerminalsAwakeTerminalGroupsRequest.md)|  | [optional] 

### Return type

[**TransportTerminalsAwakeTerminalGroupsResponse**](TransportTerminalsAwakeTerminalGroupsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **terminal_groups_is_alive_post**
> TransportTerminalsTerminalGroupsIsAliveResponse terminal_groups_is_alive_post(timeout=timeout, transport_terminals_terminal_groups_is_alive_request=transport_terminals_terminal_groups_is_alive_request)

Returns information on availability of group of terminals.



 > Restriction group: `POS: availability`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_terminals_terminal_groups_is_alive_request import TransportTerminalsTerminalGroupsIsAliveRequest
from iikocloud_client.models.transport_terminals_terminal_groups_is_alive_response import TransportTerminalsTerminalGroupsIsAliveResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.TerminalGroupsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_terminals_terminal_groups_is_alive_request = iikocloud_client.TransportTerminalsTerminalGroupsIsAliveRequest() # TransportTerminalsTerminalGroupsIsAliveRequest |  (optional)

    try:
        # Returns information on availability of group of terminals.
        api_response = await api_instance.terminal_groups_is_alive_post(timeout=timeout, transport_terminals_terminal_groups_is_alive_request=transport_terminals_terminal_groups_is_alive_request)
        print("The response of TerminalGroupsApi->terminal_groups_is_alive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalGroupsApi->terminal_groups_is_alive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_terminals_terminal_groups_is_alive_request** | [**TransportTerminalsTerminalGroupsIsAliveRequest**](TransportTerminalsTerminalGroupsIsAliveRequest.md)|  | [optional] 

### Return type

[**TransportTerminalsTerminalGroupsIsAliveResponse**](TransportTerminalsTerminalGroupsIsAliveResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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

# **terminal_groups_post**
> TransportTerminalsTerminalGroupsResponse terminal_groups_post(timeout=timeout, transport_terminals_terminal_groups_request=transport_terminals_terminal_groups_request)

Method that returns information on groups of delivery terminals.



 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_terminals_terminal_groups_request import TransportTerminalsTerminalGroupsRequest
from iikocloud_client.models.transport_terminals_terminal_groups_response import TransportTerminalsTerminalGroupsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.TerminalGroupsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_terminals_terminal_groups_request = iikocloud_client.TransportTerminalsTerminalGroupsRequest() # TransportTerminalsTerminalGroupsRequest |  (optional)

    try:
        # Method that returns information on groups of delivery terminals.
        api_response = await api_instance.terminal_groups_post(timeout=timeout, transport_terminals_terminal_groups_request=transport_terminals_terminal_groups_request)
        print("The response of TerminalGroupsApi->terminal_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TerminalGroupsApi->terminal_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_terminals_terminal_groups_request** | [**TransportTerminalsTerminalGroupsRequest**](TransportTerminalsTerminalGroupsRequest.md)|  | [optional] 

### Return type

[**TransportTerminalsTerminalGroupsResponse**](TransportTerminalsTerminalGroupsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

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

