# iikocloud_client.EmployeesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_personal_session**](EmployeesApi.md#close_personal_session) | **POST** /api/1/employees/shift/clockout | Close personal session.
[**get_active_courier_locations**](EmployeesApi.md#get_active_courier_locations) | **POST** /api/1/employees/couriers/active_location | Returns list of all active (courier session is opened) courier&#39;s locations which are delivery drivers   in specified restaurants.
[**get_active_courier_locations_by_terminal**](EmployeesApi.md#get_active_courier_locations_by_terminal) | **POST** /api/1/employees/couriers/active_location/by_terminal | Returns list of all active (courier session is opened) courier&#39;s locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.
[**get_courier_location_history**](EmployeesApi.md#get_courier_location_history) | **POST** /api/1/employees/couriers/locations/by_time_offset | Method of obtaining drivers&#39; coordinates history.
[**get_couriers**](EmployeesApi.md#get_couriers) | **POST** /api/1/employees/couriers | Returns list of all employees which are delivery drivers in specified restaurants.
[**get_couriers_by_role**](EmployeesApi.md#get_couriers_by_role) | **POST** /api/1/employees/couriers/by_role | Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.
[**get_employee_info**](EmployeesApi.md#get_employee_info) | **POST** /api/1/employees/info | Returns employee info.
[**get_personal_session_info**](EmployeesApi.md#get_personal_session_info) | **POST** /api/1/employees/shift/is_open | Check if personal session is open.
[**get_terminal_groups_of_employee**](EmployeesApi.md#get_terminal_groups_of_employee) | **POST** /api/1/employees/shifts/by_courier | Get terminal groups where employee session is opened.
[**open_personal_session**](EmployeesApi.md#open_personal_session) | **POST** /api/1/employees/shift/clockin | Open personal session.


# **close_personal_session**
> ChangePersonalSessionResponse close_personal_session(timeout=timeout, close_personal_session_request=close_personal_session_request)

Close personal session.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Employees: shifts`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_personal_session_response import ChangePersonalSessionResponse
from iikocloud_client.models.close_personal_session_request import ClosePersonalSessionRequest
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    close_personal_session_request = iikocloud_client.ClosePersonalSessionRequest() # ClosePersonalSessionRequest |  (optional)

    try:
        # Close personal session.
        api_response = await api_instance.close_personal_session(timeout=timeout, close_personal_session_request=close_personal_session_request)
        print("The response of EmployeesApi->close_personal_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->close_personal_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **close_personal_session_request** | [**ClosePersonalSessionRequest**](ClosePersonalSessionRequest.md)|  | [optional] 

### Return type

[**ChangePersonalSessionResponse**](ChangePersonalSessionResponse.md)

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

# **get_active_courier_locations**
> ActiveCourierLocationsResponse get_active_courier_locations(timeout=timeout, couriers_request=couriers_request)

Returns list of all active (courier session is opened) courier's locations which are delivery drivers   in specified restaurants.



 > Restriction group: `Drivers: location`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.active_courier_locations_response import ActiveCourierLocationsResponse
from iikocloud_client.models.couriers_request import CouriersRequest
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    couriers_request = iikocloud_client.CouriersRequest() # CouriersRequest |  (optional)

    try:
        # Returns list of all active (courier session is opened) courier's locations which are delivery drivers   in specified restaurants.
        api_response = await api_instance.get_active_courier_locations(timeout=timeout, couriers_request=couriers_request)
        print("The response of EmployeesApi->get_active_courier_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_active_courier_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **couriers_request** | [**CouriersRequest**](CouriersRequest.md)|  | [optional] 

### Return type

[**ActiveCourierLocationsResponse**](ActiveCourierLocationsResponse.md)

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

# **get_active_courier_locations_by_terminal**
> ActiveCourierLocationsResponse get_active_courier_locations_by_terminal(timeout=timeout, active_courier_locations_by_terminal_group_request=active_courier_locations_by_terminal_group_request)

Returns list of all active (courier session is opened) courier's locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.



 > Restriction group: `Drivers: location`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.active_courier_locations_by_terminal_group_request import ActiveCourierLocationsByTerminalGroupRequest
from iikocloud_client.models.active_courier_locations_response import ActiveCourierLocationsResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    active_courier_locations_by_terminal_group_request = iikocloud_client.ActiveCourierLocationsByTerminalGroupRequest() # ActiveCourierLocationsByTerminalGroupRequest |  (optional)

    try:
        # Returns list of all active (courier session is opened) courier's locations which are delivery drivers in specified   restaurant and are clocked in on specified delivery terminal.
        api_response = await api_instance.get_active_courier_locations_by_terminal(timeout=timeout, active_courier_locations_by_terminal_group_request=active_courier_locations_by_terminal_group_request)
        print("The response of EmployeesApi->get_active_courier_locations_by_terminal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_active_courier_locations_by_terminal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **active_courier_locations_by_terminal_group_request** | [**ActiveCourierLocationsByTerminalGroupRequest**](ActiveCourierLocationsByTerminalGroupRequest.md)|  | [optional] 

### Return type

[**ActiveCourierLocationsResponse**](ActiveCourierLocationsResponse.md)

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

# **get_courier_location_history**
> CourierLocationsByTimeOffsetResponse get_courier_location_history(timeout=timeout, courier_locations_by_time_offset_request=courier_locations_by_time_offset_request)

Method of obtaining drivers' coordinates history.



 > Restriction group: `Drivers: location`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.courier_locations_by_time_offset_request import CourierLocationsByTimeOffsetRequest
from iikocloud_client.models.courier_locations_by_time_offset_response import CourierLocationsByTimeOffsetResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    courier_locations_by_time_offset_request = iikocloud_client.CourierLocationsByTimeOffsetRequest() # CourierLocationsByTimeOffsetRequest |  (optional)

    try:
        # Method of obtaining drivers' coordinates history.
        api_response = await api_instance.get_courier_location_history(timeout=timeout, courier_locations_by_time_offset_request=courier_locations_by_time_offset_request)
        print("The response of EmployeesApi->get_courier_location_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_courier_location_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **courier_locations_by_time_offset_request** | [**CourierLocationsByTimeOffsetRequest**](CourierLocationsByTimeOffsetRequest.md)|  | [optional] 

### Return type

[**CourierLocationsByTimeOffsetResponse**](CourierLocationsByTimeOffsetResponse.md)

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

# **get_couriers**
> EmployeesResponse get_couriers(timeout=timeout, couriers_request=couriers_request)

Returns list of all employees which are delivery drivers in specified restaurants.



 > Restriction group: `Drivers: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.couriers_request import CouriersRequest
from iikocloud_client.models.employees_response import EmployeesResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    couriers_request = iikocloud_client.CouriersRequest() # CouriersRequest |  (optional)

    try:
        # Returns list of all employees which are delivery drivers in specified restaurants.
        api_response = await api_instance.get_couriers(timeout=timeout, couriers_request=couriers_request)
        print("The response of EmployeesApi->get_couriers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_couriers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **couriers_request** | [**CouriersRequest**](CouriersRequest.md)|  | [optional] 

### Return type

[**EmployeesResponse**](EmployeesResponse.md)

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

# **get_couriers_by_role**
> EmployeesWithRoleSignResponse get_couriers_by_role(timeout=timeout, couriers_and_check_role_request=couriers_and_check_role_request)

Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.



 > Restriction group: `Drivers: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.couriers_and_check_role_request import CouriersAndCheckRoleRequest
from iikocloud_client.models.employees_with_role_sign_response import EmployeesWithRoleSignResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    couriers_and_check_role_request = iikocloud_client.CouriersAndCheckRoleRequest() # CouriersAndCheckRoleRequest |  (optional)

    try:
        # Returns list of all employees which are delivery drivers in specified restaurants,   and checks whether each employee has passed role.
        api_response = await api_instance.get_couriers_by_role(timeout=timeout, couriers_and_check_role_request=couriers_and_check_role_request)
        print("The response of EmployeesApi->get_couriers_by_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_couriers_by_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **couriers_and_check_role_request** | [**CouriersAndCheckRoleRequest**](CouriersAndCheckRoleRequest.md)|  | [optional] 

### Return type

[**EmployeesWithRoleSignResponse**](EmployeesWithRoleSignResponse.md)

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

# **get_employee_info**
> EmployeeInfoResponse get_employee_info(timeout=timeout, employee_info_request=employee_info_request)

Returns employee info.



 > Restriction group: `Employees: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.employee_info_request import EmployeeInfoRequest
from iikocloud_client.models.employee_info_response import EmployeeInfoResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    employee_info_request = iikocloud_client.EmployeeInfoRequest() # EmployeeInfoRequest |  (optional)

    try:
        # Returns employee info.
        api_response = await api_instance.get_employee_info(timeout=timeout, employee_info_request=employee_info_request)
        print("The response of EmployeesApi->get_employee_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_employee_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **employee_info_request** | [**EmployeeInfoRequest**](EmployeeInfoRequest.md)|  | [optional] 

### Return type

[**EmployeeInfoResponse**](EmployeeInfoResponse.md)

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

# **get_personal_session_info**
> GetPersonalSessionInfoResponse get_personal_session_info(timeout=timeout, get_personal_session_info_request=get_personal_session_info_request)

Check if personal session is open.



 > Restriction group: `Employees: shifts`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_personal_session_info_request import GetPersonalSessionInfoRequest
from iikocloud_client.models.get_personal_session_info_response import GetPersonalSessionInfoResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_personal_session_info_request = iikocloud_client.GetPersonalSessionInfoRequest() # GetPersonalSessionInfoRequest |  (optional)

    try:
        # Check if personal session is open.
        api_response = await api_instance.get_personal_session_info(timeout=timeout, get_personal_session_info_request=get_personal_session_info_request)
        print("The response of EmployeesApi->get_personal_session_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_personal_session_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_personal_session_info_request** | [**GetPersonalSessionInfoRequest**](GetPersonalSessionInfoRequest.md)|  | [optional] 

### Return type

[**GetPersonalSessionInfoResponse**](GetPersonalSessionInfoResponse.md)

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

# **get_terminal_groups_of_employee**
> GetTerminalGroupsOfEmployeeResponse get_terminal_groups_of_employee(timeout=timeout, get_terminal_groups_of_employee_request=get_terminal_groups_of_employee_request)

Get terminal groups where employee session is opened.



 > Restriction group: `Employees: shifts`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_terminal_groups_of_employee_request import GetTerminalGroupsOfEmployeeRequest
from iikocloud_client.models.get_terminal_groups_of_employee_response import GetTerminalGroupsOfEmployeeResponse
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_terminal_groups_of_employee_request = iikocloud_client.GetTerminalGroupsOfEmployeeRequest() # GetTerminalGroupsOfEmployeeRequest |  (optional)

    try:
        # Get terminal groups where employee session is opened.
        api_response = await api_instance.get_terminal_groups_of_employee(timeout=timeout, get_terminal_groups_of_employee_request=get_terminal_groups_of_employee_request)
        print("The response of EmployeesApi->get_terminal_groups_of_employee:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->get_terminal_groups_of_employee: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_terminal_groups_of_employee_request** | [**GetTerminalGroupsOfEmployeeRequest**](GetTerminalGroupsOfEmployeeRequest.md)|  | [optional] 

### Return type

[**GetTerminalGroupsOfEmployeeResponse**](GetTerminalGroupsOfEmployeeResponse.md)

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

# **open_personal_session**
> ChangePersonalSessionResponse open_personal_session(timeout=timeout, open_personal_session_request=open_personal_session_request)

Open personal session.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Employees: shifts`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_personal_session_response import ChangePersonalSessionResponse
from iikocloud_client.models.open_personal_session_request import OpenPersonalSessionRequest
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
    api_instance = iikocloud_client.EmployeesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    open_personal_session_request = iikocloud_client.OpenPersonalSessionRequest() # OpenPersonalSessionRequest |  (optional)

    try:
        # Open personal session.
        api_response = await api_instance.open_personal_session(timeout=timeout, open_personal_session_request=open_personal_session_request)
        print("The response of EmployeesApi->open_personal_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesApi->open_personal_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **open_personal_session_request** | [**OpenPersonalSessionRequest**](OpenPersonalSessionRequest.md)|  | [optional] 

### Return type

[**ChangePersonalSessionResponse**](ChangePersonalSessionResponse.md)

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

