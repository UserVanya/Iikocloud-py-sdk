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
> IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse employees_couriers_active_location_by_terminal_post(timeout=timeout, iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request=iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request)

Returns list of all active (courier session is opened) courier's locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.



 > Restriction group: `Drivers: location`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request import IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_active_courier_locations_response import IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest() # IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest |  (optional)

    try:
        # Returns list of all active (courier session is opened) courier's locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.
        api_response = await api_instance.employees_couriers_active_location_by_terminal_post(timeout=timeout, iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request=iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request)
        print("The response of EmployeesApi->employees_couriers_active_location_by_terminal_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_active_location_by_terminal_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_active_courier_locations_by_terminal_group_request** | [**IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest**](IikoTransportPublicApiContractsEmployeesActiveCourierLocationsByTerminalGroupRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse**](IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse.md)

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

# **employees_couriers_active_location_post**
> IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse employees_couriers_active_location_post(timeout=timeout, iiko_transport_public_api_contracts_employees_couriers_request=iiko_transport_public_api_contracts_employees_couriers_request)

Returns list of all active (courier session is opened) courier's locations which are delivery drivers   in specified restaurants.



 > Restriction group: `Drivers: location`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_active_courier_locations_response import IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_couriers_request import IikoTransportPublicApiContractsEmployeesCouriersRequest
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_couriers_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesCouriersRequest() # IikoTransportPublicApiContractsEmployeesCouriersRequest |  (optional)

    try:
        # Returns list of all active (courier session is opened) courier's locations which are delivery drivers   in specified restaurants.
        api_response = await api_instance.employees_couriers_active_location_post(timeout=timeout, iiko_transport_public_api_contracts_employees_couriers_request=iiko_transport_public_api_contracts_employees_couriers_request)
        print("The response of EmployeesApi->employees_couriers_active_location_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_active_location_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_couriers_request** | [**IikoTransportPublicApiContractsEmployeesCouriersRequest**](IikoTransportPublicApiContractsEmployeesCouriersRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse**](IikoTransportPublicApiContractsEmployeesActiveCourierLocationsResponse.md)

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

# **employees_couriers_by_role_post**
> IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse employees_couriers_by_role_post(timeout=timeout, iiko_transport_public_api_contracts_employees_couriers_and_check_role_request=iiko_transport_public_api_contracts_employees_couriers_and_check_role_request)

Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.



 > Restriction group: `Drivers: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_couriers_and_check_role_request import IikoTransportPublicApiContractsEmployeesCouriersAndCheckRoleRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employees_with_role_sign_response import IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_couriers_and_check_role_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesCouriersAndCheckRoleRequest() # IikoTransportPublicApiContractsEmployeesCouriersAndCheckRoleRequest |  (optional)

    try:
        # Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.
        api_response = await api_instance.employees_couriers_by_role_post(timeout=timeout, iiko_transport_public_api_contracts_employees_couriers_and_check_role_request=iiko_transport_public_api_contracts_employees_couriers_and_check_role_request)
        print("The response of EmployeesApi->employees_couriers_by_role_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_by_role_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_couriers_and_check_role_request** | [**IikoTransportPublicApiContractsEmployeesCouriersAndCheckRoleRequest**](IikoTransportPublicApiContractsEmployeesCouriersAndCheckRoleRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse**](IikoTransportPublicApiContractsEmployeesEmployeesWithRoleSignResponse.md)

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

# **employees_couriers_locations_by_time_offset_post**
> IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse employees_couriers_locations_by_time_offset_post(timeout=timeout, iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_request=iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_request)

Method of obtaining drivers' coordinates history.



 > Restriction group: `Drivers: location`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_request import IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_response import IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetRequest() # IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetRequest |  (optional)

    try:
        # Method of obtaining drivers' coordinates history.
        api_response = await api_instance.employees_couriers_locations_by_time_offset_post(timeout=timeout, iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_request=iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_request)
        print("The response of EmployeesApi->employees_couriers_locations_by_time_offset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_locations_by_time_offset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_courier_locations_by_time_offset_request** | [**IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetRequest**](IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse**](IikoTransportPublicApiContractsEmployeesCourierLocationsByTimeOffsetResponse.md)

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

# **employees_couriers_post**
> IikoTransportPublicApiContractsEmployeesEmployeesResponse employees_couriers_post(timeout=timeout, iiko_transport_public_api_contracts_employees_couriers_request=iiko_transport_public_api_contracts_employees_couriers_request)

Returns list of all employees which are delivery drivers in specified restaurants.



 > Restriction group: `Drivers: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_couriers_request import IikoTransportPublicApiContractsEmployeesCouriersRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employees_response import IikoTransportPublicApiContractsEmployeesEmployeesResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_couriers_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesCouriersRequest() # IikoTransportPublicApiContractsEmployeesCouriersRequest |  (optional)

    try:
        # Returns list of all employees which are delivery drivers in specified restaurants.
        api_response = await api_instance.employees_couriers_post(timeout=timeout, iiko_transport_public_api_contracts_employees_couriers_request=iiko_transport_public_api_contracts_employees_couriers_request)
        print("The response of EmployeesApi->employees_couriers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_couriers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_couriers_request** | [**IikoTransportPublicApiContractsEmployeesCouriersRequest**](IikoTransportPublicApiContractsEmployeesCouriersRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesEmployeesResponse**](IikoTransportPublicApiContractsEmployeesEmployeesResponse.md)

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

# **employees_info_post**
> IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse employees_info_post(timeout=timeout, iiko_transport_public_api_contracts_employees_employee_info_request=iiko_transport_public_api_contracts_employees_employee_info_request)

Returns employee info.



 > Restriction group: `Employees: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employee_info_request import IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employee_info_response import IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_employee_info_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest() # IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest |  (optional)

    try:
        # Returns employee info.
        api_response = await api_instance.employees_info_post(timeout=timeout, iiko_transport_public_api_contracts_employees_employee_info_request=iiko_transport_public_api_contracts_employees_employee_info_request)
        print("The response of EmployeesApi->employees_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_employee_info_request** | [**IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest**](IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse**](IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse.md)

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

# **employees_shift_clockin_post**
> IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse employees_shift_clockin_post(timeout=timeout, iiko_transport_public_api_contracts_employees_open_personal_session_request=iiko_transport_public_api_contracts_employees_open_personal_session_request)

Open personal session.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Employees: shifts`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_change_personal_session_response import IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_open_personal_session_request import IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_open_personal_session_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest() # IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest |  (optional)

    try:
        # Open personal session.
        api_response = await api_instance.employees_shift_clockin_post(timeout=timeout, iiko_transport_public_api_contracts_employees_open_personal_session_request=iiko_transport_public_api_contracts_employees_open_personal_session_request)
        print("The response of EmployeesApi->employees_shift_clockin_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shift_clockin_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_open_personal_session_request** | [**IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest**](IikoTransportPublicApiContractsEmployeesOpenPersonalSessionRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse**](IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse.md)

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

# **employees_shift_clockout_post**
> IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse employees_shift_clockout_post(timeout=timeout, iiko_transport_public_api_contracts_employees_close_personal_session_request=iiko_transport_public_api_contracts_employees_close_personal_session_request)

Close personal session.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Employees: shifts`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_change_personal_session_response import IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_close_personal_session_request import IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_close_personal_session_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest() # IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest |  (optional)

    try:
        # Close personal session.
        api_response = await api_instance.employees_shift_clockout_post(timeout=timeout, iiko_transport_public_api_contracts_employees_close_personal_session_request=iiko_transport_public_api_contracts_employees_close_personal_session_request)
        print("The response of EmployeesApi->employees_shift_clockout_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shift_clockout_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_close_personal_session_request** | [**IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest**](IikoTransportPublicApiContractsEmployeesClosePersonalSessionRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse**](IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse.md)

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

# **employees_shift_is_open_post**
> IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse employees_shift_is_open_post(timeout=timeout, iiko_transport_public_api_contracts_employees_get_personal_session_info_request=iiko_transport_public_api_contracts_employees_get_personal_session_info_request)

Check if personal session is open.



 > Restriction group: `Employees: shifts`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_get_personal_session_info_request import IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_get_personal_session_info_response import IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_get_personal_session_info_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoRequest() # IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoRequest |  (optional)

    try:
        # Check if personal session is open.
        api_response = await api_instance.employees_shift_is_open_post(timeout=timeout, iiko_transport_public_api_contracts_employees_get_personal_session_info_request=iiko_transport_public_api_contracts_employees_get_personal_session_info_request)
        print("The response of EmployeesApi->employees_shift_is_open_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shift_is_open_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_get_personal_session_info_request** | [**IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoRequest**](IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse**](IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse.md)

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

# **employees_shifts_by_courier_post**
> IikoTransportPublicApiContractsEmployeesGetTerminalGroupsOfEmployeeResponse employees_shifts_by_courier_post(timeout=timeout, iiko_transport_public_api_contracts_employees_get_terminal_groups_of_employee_request=iiko_transport_public_api_contracts_employees_get_terminal_groups_of_employee_request)

Get terminal groups where employee session is opened.



 > Restriction group: `Employees: shifts`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_get_terminal_groups_of_employee_request import IikoTransportPublicApiContractsEmployeesGetTerminalGroupsOfEmployeeRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_get_terminal_groups_of_employee_response import IikoTransportPublicApiContractsEmployeesGetTerminalGroupsOfEmployeeResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_employees_get_terminal_groups_of_employee_request = iikocloud_client.IikoTransportPublicApiContractsEmployeesGetTerminalGroupsOfEmployeeRequest() # IikoTransportPublicApiContractsEmployeesGetTerminalGroupsOfEmployeeRequest |  (optional)

    try:
        # Get terminal groups where employee session is opened.
        api_response = await api_instance.employees_shifts_by_courier_post(timeout=timeout, iiko_transport_public_api_contracts_employees_get_terminal_groups_of_employee_request=iiko_transport_public_api_contracts_employees_get_terminal_groups_of_employee_request)
        print("The response of EmployeesApi->employees_shifts_by_courier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->employees_shifts_by_courier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_employees_get_terminal_groups_of_employee_request** | [**IikoTransportPublicApiContractsEmployeesGetTerminalGroupsOfEmployeeRequest**](IikoTransportPublicApiContractsEmployeesGetTerminalGroupsOfEmployeeRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsEmployeesGetTerminalGroupsOfEmployeeResponse**](IikoTransportPublicApiContractsEmployeesGetTerminalGroupsOfEmployeeResponse.md)

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

