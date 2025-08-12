# iikocloud_client.EmployeesApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employees_couriers_active_location_by_terminal_post**](EmployeesApi.md#employees_couriers_active_location_by_terminal_post) | **POST** /employees/couriers/active_location/by_terminal | Returns list of all active (courier session is opened) courier&#39;s locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.
[**employees_couriers_active_location_post**](EmployeesApi.md#employees_couriers_active_location_post) | **POST** /employees/couriers/active_location | Returns list of all active (courier session is opened) courier&#39;s locations which are delivery drivers   in specified restaurants.
[**employees_couriers_by_role_post**](EmployeesApi.md#employees_couriers_by_role_post) | **POST** /employees/couriers/by_role | Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.
[**employees_couriers_locations_by_time_offset_post**](EmployeesApi.md#employees_couriers_locations_by_time_offset_post) | **POST** /employees/couriers/locations/by_time_offset | Method of obtaining drivers&#39; coordinates history.
[**employees_couriers_post**](EmployeesApi.md#employees_couriers_post) | **POST** /employees/couriers | Returns list of all employees which are delivery drivers in specified restaurants.
[**employees_info_post**](EmployeesApi.md#employees_info_post) | **POST** /employees/info | Returns employee info.
[**employees_shift_clockin_post**](EmployeesApi.md#employees_shift_clockin_post) | **POST** /employees/shift/clockin | Open personal session.
[**employees_shift_clockout_post**](EmployeesApi.md#employees_shift_clockout_post) | **POST** /employees/shift/clockout | Close personal session.
[**employees_shift_is_open_post**](EmployeesApi.md#employees_shift_is_open_post) | **POST** /employees/shift/is_open | Check if personal session is open.
[**employees_shifts_by_courier_post**](EmployeesApi.md#employees_shifts_by_courier_post) | **POST** /employees/shifts/by_courier | Get terminal groups where employee session is opened.


# **employees_couriers_active_location_by_terminal_post**
> TransportEmployeesActiveCourierLocationsResponse employees_couriers_active_location_by_terminal_post(timeout=timeout, transport_employees_active_courier_locations_by_terminal_group_request=transport_employees_active_courier_locations_by_terminal_group_request)

Returns list of all active (courier session is opened) courier's locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.



 > Restriction group: `Drivers: location`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_active_courier_locations_by_terminal_group_request import TransportEmployeesActiveCourierLocationsByTerminalGroupRequest
from iikocloud_client.models.transport_employees_active_courier_locations_response import TransportEmployeesActiveCourierLocationsResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_active_courier_locations_by_terminal_group_request = iikocloud_client.TransportEmployeesActiveCourierLocationsByTerminalGroupRequest() # TransportEmployeesActiveCourierLocationsByTerminalGroupRequest |  (optional)

    try:
        # Returns list of all active (courier session is opened) courier's locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.
        api_response = await api_instance.employees_couriers_active_location_by_terminal_post(timeout=timeout, transport_employees_active_courier_locations_by_terminal_group_request=transport_employees_active_courier_locations_by_terminal_group_request)
        print("The response of EmployeesApi->employees_couriers_active_location_by_terminal_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_active_location_by_terminal_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_active_courier_locations_by_terminal_group_request** | [**TransportEmployeesActiveCourierLocationsByTerminalGroupRequest**](TransportEmployeesActiveCourierLocationsByTerminalGroupRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesActiveCourierLocationsResponse**](TransportEmployeesActiveCourierLocationsResponse.md)

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

# **employees_couriers_active_location_post**
> TransportEmployeesActiveCourierLocationsResponse employees_couriers_active_location_post(timeout=timeout, transport_employees_couriers_request=transport_employees_couriers_request)

Returns list of all active (courier session is opened) courier's locations which are delivery drivers   in specified restaurants.



 > Restriction group: `Drivers: location`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_active_courier_locations_response import TransportEmployeesActiveCourierLocationsResponse
from iikocloud_client.models.transport_employees_couriers_request import TransportEmployeesCouriersRequest
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_couriers_request = iikocloud_client.TransportEmployeesCouriersRequest() # TransportEmployeesCouriersRequest |  (optional)

    try:
        # Returns list of all active (courier session is opened) courier's locations which are delivery drivers   in specified restaurants.
        api_response = await api_instance.employees_couriers_active_location_post(timeout=timeout, transport_employees_couriers_request=transport_employees_couriers_request)
        print("The response of EmployeesApi->employees_couriers_active_location_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_active_location_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_couriers_request** | [**TransportEmployeesCouriersRequest**](TransportEmployeesCouriersRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesActiveCourierLocationsResponse**](TransportEmployeesActiveCourierLocationsResponse.md)

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

# **employees_couriers_by_role_post**
> TransportEmployeesEmployeesWithRoleSignResponse employees_couriers_by_role_post(timeout=timeout, transport_employees_couriers_and_check_role_request=transport_employees_couriers_and_check_role_request)

Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.



 > Restriction group: `Drivers: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_couriers_and_check_role_request import TransportEmployeesCouriersAndCheckRoleRequest
from iikocloud_client.models.transport_employees_employees_with_role_sign_response import TransportEmployeesEmployeesWithRoleSignResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_couriers_and_check_role_request = iikocloud_client.TransportEmployeesCouriersAndCheckRoleRequest() # TransportEmployeesCouriersAndCheckRoleRequest |  (optional)

    try:
        # Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.
        api_response = await api_instance.employees_couriers_by_role_post(timeout=timeout, transport_employees_couriers_and_check_role_request=transport_employees_couriers_and_check_role_request)
        print("The response of EmployeesApi->employees_couriers_by_role_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_by_role_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_couriers_and_check_role_request** | [**TransportEmployeesCouriersAndCheckRoleRequest**](TransportEmployeesCouriersAndCheckRoleRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesEmployeesWithRoleSignResponse**](TransportEmployeesEmployeesWithRoleSignResponse.md)

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

# **employees_couriers_locations_by_time_offset_post**
> TransportEmployeesCourierLocationsByTimeOffsetResponse employees_couriers_locations_by_time_offset_post(timeout=timeout, transport_employees_courier_locations_by_time_offset_request=transport_employees_courier_locations_by_time_offset_request)

Method of obtaining drivers' coordinates history.



 > Restriction group: `Drivers: location`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_courier_locations_by_time_offset_request import TransportEmployeesCourierLocationsByTimeOffsetRequest
from iikocloud_client.models.transport_employees_courier_locations_by_time_offset_response import TransportEmployeesCourierLocationsByTimeOffsetResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_courier_locations_by_time_offset_request = iikocloud_client.TransportEmployeesCourierLocationsByTimeOffsetRequest() # TransportEmployeesCourierLocationsByTimeOffsetRequest |  (optional)

    try:
        # Method of obtaining drivers' coordinates history.
        api_response = await api_instance.employees_couriers_locations_by_time_offset_post(timeout=timeout, transport_employees_courier_locations_by_time_offset_request=transport_employees_courier_locations_by_time_offset_request)
        print("The response of EmployeesApi->employees_couriers_locations_by_time_offset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_locations_by_time_offset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_courier_locations_by_time_offset_request** | [**TransportEmployeesCourierLocationsByTimeOffsetRequest**](TransportEmployeesCourierLocationsByTimeOffsetRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesCourierLocationsByTimeOffsetResponse**](TransportEmployeesCourierLocationsByTimeOffsetResponse.md)

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

# **employees_couriers_post**
> TransportEmployeesEmployeesResponse employees_couriers_post(timeout=timeout, transport_employees_couriers_request=transport_employees_couriers_request)

Returns list of all employees which are delivery drivers in specified restaurants.



 > Restriction group: `Drivers: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_couriers_request import TransportEmployeesCouriersRequest
from iikocloud_client.models.transport_employees_employees_response import TransportEmployeesEmployeesResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_couriers_request = iikocloud_client.TransportEmployeesCouriersRequest() # TransportEmployeesCouriersRequest |  (optional)

    try:
        # Returns list of all employees which are delivery drivers in specified restaurants.
        api_response = await api_instance.employees_couriers_post(timeout=timeout, transport_employees_couriers_request=transport_employees_couriers_request)
        print("The response of EmployeesApi->employees_couriers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_couriers_request** | [**TransportEmployeesCouriersRequest**](TransportEmployeesCouriersRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesEmployeesResponse**](TransportEmployeesEmployeesResponse.md)

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

# **employees_info_post**
> TransportEmployeesEmployeeInfoResponse employees_info_post(timeout=timeout, transport_employees_employee_info_request=transport_employees_employee_info_request)

Returns employee info.



 > Restriction group: `Employees: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_employee_info_request import TransportEmployeesEmployeeInfoRequest
from iikocloud_client.models.transport_employees_employee_info_response import TransportEmployeesEmployeeInfoResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_employee_info_request = iikocloud_client.TransportEmployeesEmployeeInfoRequest() # TransportEmployeesEmployeeInfoRequest |  (optional)

    try:
        # Returns employee info.
        api_response = await api_instance.employees_info_post(timeout=timeout, transport_employees_employee_info_request=transport_employees_employee_info_request)
        print("The response of EmployeesApi->employees_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_employee_info_request** | [**TransportEmployeesEmployeeInfoRequest**](TransportEmployeesEmployeeInfoRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesEmployeeInfoResponse**](TransportEmployeesEmployeeInfoResponse.md)

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

# **employees_shift_clockin_post**
> TransportEmployeesChangePersonalSessionResponse employees_shift_clockin_post(timeout=timeout, transport_employees_open_personal_session_request=transport_employees_open_personal_session_request)

Open personal session.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Employees: shifts`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_change_personal_session_response import TransportEmployeesChangePersonalSessionResponse
from iikocloud_client.models.transport_employees_open_personal_session_request import TransportEmployeesOpenPersonalSessionRequest
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_open_personal_session_request = iikocloud_client.TransportEmployeesOpenPersonalSessionRequest() # TransportEmployeesOpenPersonalSessionRequest |  (optional)

    try:
        # Open personal session.
        api_response = await api_instance.employees_shift_clockin_post(timeout=timeout, transport_employees_open_personal_session_request=transport_employees_open_personal_session_request)
        print("The response of EmployeesApi->employees_shift_clockin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shift_clockin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_open_personal_session_request** | [**TransportEmployeesOpenPersonalSessionRequest**](TransportEmployeesOpenPersonalSessionRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesChangePersonalSessionResponse**](TransportEmployeesChangePersonalSessionResponse.md)

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

# **employees_shift_clockout_post**
> TransportEmployeesChangePersonalSessionResponse employees_shift_clockout_post(timeout=timeout, transport_employees_close_personal_session_request=transport_employees_close_personal_session_request)

Close personal session.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Employees: shifts`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_change_personal_session_response import TransportEmployeesChangePersonalSessionResponse
from iikocloud_client.models.transport_employees_close_personal_session_request import TransportEmployeesClosePersonalSessionRequest
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_close_personal_session_request = iikocloud_client.TransportEmployeesClosePersonalSessionRequest() # TransportEmployeesClosePersonalSessionRequest |  (optional)

    try:
        # Close personal session.
        api_response = await api_instance.employees_shift_clockout_post(timeout=timeout, transport_employees_close_personal_session_request=transport_employees_close_personal_session_request)
        print("The response of EmployeesApi->employees_shift_clockout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shift_clockout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_close_personal_session_request** | [**TransportEmployeesClosePersonalSessionRequest**](TransportEmployeesClosePersonalSessionRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesChangePersonalSessionResponse**](TransportEmployeesChangePersonalSessionResponse.md)

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

# **employees_shift_is_open_post**
> TransportEmployeesGetPersonalSessionInfoResponse employees_shift_is_open_post(timeout=timeout, transport_employees_get_personal_session_info_request=transport_employees_get_personal_session_info_request)

Check if personal session is open.



 > Restriction group: `Employees: shifts`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_get_personal_session_info_request import TransportEmployeesGetPersonalSessionInfoRequest
from iikocloud_client.models.transport_employees_get_personal_session_info_response import TransportEmployeesGetPersonalSessionInfoResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_get_personal_session_info_request = iikocloud_client.TransportEmployeesGetPersonalSessionInfoRequest() # TransportEmployeesGetPersonalSessionInfoRequest |  (optional)

    try:
        # Check if personal session is open.
        api_response = await api_instance.employees_shift_is_open_post(timeout=timeout, transport_employees_get_personal_session_info_request=transport_employees_get_personal_session_info_request)
        print("The response of EmployeesApi->employees_shift_is_open_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shift_is_open_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_get_personal_session_info_request** | [**TransportEmployeesGetPersonalSessionInfoRequest**](TransportEmployeesGetPersonalSessionInfoRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesGetPersonalSessionInfoResponse**](TransportEmployeesGetPersonalSessionInfoResponse.md)

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

# **employees_shifts_by_courier_post**
> TransportEmployeesGetTerminalGroupsOfEmployeeResponse employees_shifts_by_courier_post(timeout=timeout, transport_employees_get_terminal_groups_of_employee_request=transport_employees_get_terminal_groups_of_employee_request)

Get terminal groups where employee session is opened.



 > Restriction group: `Employees: shifts`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_employees_get_terminal_groups_of_employee_request import TransportEmployeesGetTerminalGroupsOfEmployeeRequest
from iikocloud_client.models.transport_employees_get_terminal_groups_of_employee_response import TransportEmployeesGetTerminalGroupsOfEmployeeResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_employees_get_terminal_groups_of_employee_request = iikocloud_client.TransportEmployeesGetTerminalGroupsOfEmployeeRequest() # TransportEmployeesGetTerminalGroupsOfEmployeeRequest |  (optional)

    try:
        # Get terminal groups where employee session is opened.
        api_response = await api_instance.employees_shifts_by_courier_post(timeout=timeout, transport_employees_get_terminal_groups_of_employee_request=transport_employees_get_terminal_groups_of_employee_request)
        print("The response of EmployeesApi->employees_shifts_by_courier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shifts_by_courier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_employees_get_terminal_groups_of_employee_request** | [**TransportEmployeesGetTerminalGroupsOfEmployeeRequest**](TransportEmployeesGetTerminalGroupsOfEmployeeRequest.md)|  | [optional] 

### Return type

[**TransportEmployeesGetTerminalGroupsOfEmployeeResponse**](TransportEmployeesGetTerminalGroupsOfEmployeeResponse.md)

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

