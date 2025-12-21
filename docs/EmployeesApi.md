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
> EmployeesActiveCourierLocationsResponse employees_couriers_active_location_by_terminal_post(timeout=timeout, employees_active_courier_locations_by_terminal_group_request=employees_active_courier_locations_by_terminal_group_request)

Returns list of all active (courier session is opened) courier's locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.



 > Restriction group: `Drivers: location`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_active_courier_locations_by_terminal_group_request import EmployeesActiveCourierLocationsByTerminalGroupRequest
from iikocloud_client.models.employees_active_courier_locations_response import EmployeesActiveCourierLocationsResponse
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
    employees_active_courier_locations_by_terminal_group_request = iikocloud_client.EmployeesActiveCourierLocationsByTerminalGroupRequest() # EmployeesActiveCourierLocationsByTerminalGroupRequest |  (optional)

    try:
        # Returns list of all active (courier session is opened) courier's locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.
        api_response = await api_instance.employees_couriers_active_location_by_terminal_post(timeout=timeout, employees_active_courier_locations_by_terminal_group_request=employees_active_courier_locations_by_terminal_group_request)
        print("The response of EmployeesApi->employees_couriers_active_location_by_terminal_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_active_location_by_terminal_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_active_courier_locations_by_terminal_group_request** | [**EmployeesActiveCourierLocationsByTerminalGroupRequest**](EmployeesActiveCourierLocationsByTerminalGroupRequest.md)|  | [optional] 

### Return type

[**EmployeesActiveCourierLocationsResponse**](EmployeesActiveCourierLocationsResponse.md)

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
> EmployeesActiveCourierLocationsResponse employees_couriers_active_location_post(timeout=timeout, employees_couriers_request=employees_couriers_request)

Returns list of all active (courier session is opened) courier's locations which are delivery drivers   in specified restaurants.



 > Restriction group: `Drivers: location`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_active_courier_locations_response import EmployeesActiveCourierLocationsResponse
from iikocloud_client.models.employees_couriers_request import EmployeesCouriersRequest
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
    employees_couriers_request = iikocloud_client.EmployeesCouriersRequest() # EmployeesCouriersRequest |  (optional)

    try:
        # Returns list of all active (courier session is opened) courier's locations which are delivery drivers   in specified restaurants.
        api_response = await api_instance.employees_couriers_active_location_post(timeout=timeout, employees_couriers_request=employees_couriers_request)
        print("The response of EmployeesApi->employees_couriers_active_location_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_active_location_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_couriers_request** | [**EmployeesCouriersRequest**](EmployeesCouriersRequest.md)|  | [optional] 

### Return type

[**EmployeesActiveCourierLocationsResponse**](EmployeesActiveCourierLocationsResponse.md)

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
> EmployeesEmployeesWithRoleSignResponse employees_couriers_by_role_post(timeout=timeout, employees_couriers_and_check_role_request=employees_couriers_and_check_role_request)

Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.



 > Restriction group: `Drivers: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_couriers_and_check_role_request import EmployeesCouriersAndCheckRoleRequest
from iikocloud_client.models.employees_employees_with_role_sign_response import EmployeesEmployeesWithRoleSignResponse
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
    employees_couriers_and_check_role_request = iikocloud_client.EmployeesCouriersAndCheckRoleRequest() # EmployeesCouriersAndCheckRoleRequest |  (optional)

    try:
        # Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.
        api_response = await api_instance.employees_couriers_by_role_post(timeout=timeout, employees_couriers_and_check_role_request=employees_couriers_and_check_role_request)
        print("The response of EmployeesApi->employees_couriers_by_role_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_by_role_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_couriers_and_check_role_request** | [**EmployeesCouriersAndCheckRoleRequest**](EmployeesCouriersAndCheckRoleRequest.md)|  | [optional] 

### Return type

[**EmployeesEmployeesWithRoleSignResponse**](EmployeesEmployeesWithRoleSignResponse.md)

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
> EmployeesCourierLocationsByTimeOffsetResponse employees_couriers_locations_by_time_offset_post(timeout=timeout, employees_courier_locations_by_time_offset_request=employees_courier_locations_by_time_offset_request)

Method of obtaining drivers' coordinates history.



 > Restriction group: `Drivers: location`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_courier_locations_by_time_offset_request import EmployeesCourierLocationsByTimeOffsetRequest
from iikocloud_client.models.employees_courier_locations_by_time_offset_response import EmployeesCourierLocationsByTimeOffsetResponse
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
    employees_courier_locations_by_time_offset_request = iikocloud_client.EmployeesCourierLocationsByTimeOffsetRequest() # EmployeesCourierLocationsByTimeOffsetRequest |  (optional)

    try:
        # Method of obtaining drivers' coordinates history.
        api_response = await api_instance.employees_couriers_locations_by_time_offset_post(timeout=timeout, employees_courier_locations_by_time_offset_request=employees_courier_locations_by_time_offset_request)
        print("The response of EmployeesApi->employees_couriers_locations_by_time_offset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_locations_by_time_offset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_courier_locations_by_time_offset_request** | [**EmployeesCourierLocationsByTimeOffsetRequest**](EmployeesCourierLocationsByTimeOffsetRequest.md)|  | [optional] 

### Return type

[**EmployeesCourierLocationsByTimeOffsetResponse**](EmployeesCourierLocationsByTimeOffsetResponse.md)

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
> EmployeesEmployeesResponse employees_couriers_post(timeout=timeout, employees_couriers_request=employees_couriers_request)

Returns list of all employees which are delivery drivers in specified restaurants.



 > Restriction group: `Drivers: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_couriers_request import EmployeesCouriersRequest
from iikocloud_client.models.employees_employees_response import EmployeesEmployeesResponse
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
    employees_couriers_request = iikocloud_client.EmployeesCouriersRequest() # EmployeesCouriersRequest |  (optional)

    try:
        # Returns list of all employees which are delivery drivers in specified restaurants.
        api_response = await api_instance.employees_couriers_post(timeout=timeout, employees_couriers_request=employees_couriers_request)
        print("The response of EmployeesApi->employees_couriers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_couriers_request** | [**EmployeesCouriersRequest**](EmployeesCouriersRequest.md)|  | [optional] 

### Return type

[**EmployeesEmployeesResponse**](EmployeesEmployeesResponse.md)

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
> EmployeesEmployeeInfoResponse employees_info_post(timeout=timeout, employees_employee_info_request=employees_employee_info_request)

Returns employee info.



 > Restriction group: `Employees: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_employee_info_request import EmployeesEmployeeInfoRequest
from iikocloud_client.models.employees_employee_info_response import EmployeesEmployeeInfoResponse
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
    employees_employee_info_request = iikocloud_client.EmployeesEmployeeInfoRequest() # EmployeesEmployeeInfoRequest |  (optional)

    try:
        # Returns employee info.
        api_response = await api_instance.employees_info_post(timeout=timeout, employees_employee_info_request=employees_employee_info_request)
        print("The response of EmployeesApi->employees_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_employee_info_request** | [**EmployeesEmployeeInfoRequest**](EmployeesEmployeeInfoRequest.md)|  | [optional] 

### Return type

[**EmployeesEmployeeInfoResponse**](EmployeesEmployeeInfoResponse.md)

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
> EmployeesChangePersonalSessionResponse employees_shift_clockin_post(timeout=timeout, employees_open_personal_session_request=employees_open_personal_session_request)

Open personal session.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Employees: shifts`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_change_personal_session_response import EmployeesChangePersonalSessionResponse
from iikocloud_client.models.employees_open_personal_session_request import EmployeesOpenPersonalSessionRequest
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
    employees_open_personal_session_request = iikocloud_client.EmployeesOpenPersonalSessionRequest() # EmployeesOpenPersonalSessionRequest |  (optional)

    try:
        # Open personal session.
        api_response = await api_instance.employees_shift_clockin_post(timeout=timeout, employees_open_personal_session_request=employees_open_personal_session_request)
        print("The response of EmployeesApi->employees_shift_clockin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shift_clockin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_open_personal_session_request** | [**EmployeesOpenPersonalSessionRequest**](EmployeesOpenPersonalSessionRequest.md)|  | [optional] 

### Return type

[**EmployeesChangePersonalSessionResponse**](EmployeesChangePersonalSessionResponse.md)

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
> EmployeesChangePersonalSessionResponse employees_shift_clockout_post(timeout=timeout, employees_close_personal_session_request=employees_close_personal_session_request)

Close personal session.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Employees: shifts`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_change_personal_session_response import EmployeesChangePersonalSessionResponse
from iikocloud_client.models.employees_close_personal_session_request import EmployeesClosePersonalSessionRequest
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
    employees_close_personal_session_request = iikocloud_client.EmployeesClosePersonalSessionRequest() # EmployeesClosePersonalSessionRequest |  (optional)

    try:
        # Close personal session.
        api_response = await api_instance.employees_shift_clockout_post(timeout=timeout, employees_close_personal_session_request=employees_close_personal_session_request)
        print("The response of EmployeesApi->employees_shift_clockout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shift_clockout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_close_personal_session_request** | [**EmployeesClosePersonalSessionRequest**](EmployeesClosePersonalSessionRequest.md)|  | [optional] 

### Return type

[**EmployeesChangePersonalSessionResponse**](EmployeesChangePersonalSessionResponse.md)

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
> EmployeesGetPersonalSessionInfoResponse employees_shift_is_open_post(timeout=timeout, employees_get_personal_session_info_request=employees_get_personal_session_info_request)

Check if personal session is open.



 > Restriction group: `Employees: shifts`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_get_personal_session_info_request import EmployeesGetPersonalSessionInfoRequest
from iikocloud_client.models.employees_get_personal_session_info_response import EmployeesGetPersonalSessionInfoResponse
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
    employees_get_personal_session_info_request = iikocloud_client.EmployeesGetPersonalSessionInfoRequest() # EmployeesGetPersonalSessionInfoRequest |  (optional)

    try:
        # Check if personal session is open.
        api_response = await api_instance.employees_shift_is_open_post(timeout=timeout, employees_get_personal_session_info_request=employees_get_personal_session_info_request)
        print("The response of EmployeesApi->employees_shift_is_open_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shift_is_open_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_get_personal_session_info_request** | [**EmployeesGetPersonalSessionInfoRequest**](EmployeesGetPersonalSessionInfoRequest.md)|  | [optional] 

### Return type

[**EmployeesGetPersonalSessionInfoResponse**](EmployeesGetPersonalSessionInfoResponse.md)

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
> EmployeesGetTerminalGroupsOfEmployeeResponse employees_shifts_by_courier_post(timeout=timeout, employees_get_terminal_groups_of_employee_request=employees_get_terminal_groups_of_employee_request)

Get terminal groups where employee session is opened.



 > Restriction group: `Employees: shifts`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.employees_get_terminal_groups_of_employee_request import EmployeesGetTerminalGroupsOfEmployeeRequest
from iikocloud_client.models.employees_get_terminal_groups_of_employee_response import EmployeesGetTerminalGroupsOfEmployeeResponse
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
    employees_get_terminal_groups_of_employee_request = iikocloud_client.EmployeesGetTerminalGroupsOfEmployeeRequest() # EmployeesGetTerminalGroupsOfEmployeeRequest |  (optional)

    try:
        # Get terminal groups where employee session is opened.
        api_response = await api_instance.employees_shifts_by_courier_post(timeout=timeout, employees_get_terminal_groups_of_employee_request=employees_get_terminal_groups_of_employee_request)
        print("The response of EmployeesApi->employees_shifts_by_courier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shifts_by_courier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employees_get_terminal_groups_of_employee_request** | [**EmployeesGetTerminalGroupsOfEmployeeRequest**](EmployeesGetTerminalGroupsOfEmployeeRequest.md)|  | [optional] 

### Return type

[**EmployeesGetTerminalGroupsOfEmployeeResponse**](EmployeesGetTerminalGroupsOfEmployeeResponse.md)

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

