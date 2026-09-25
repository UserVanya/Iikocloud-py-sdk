# iikocloud_client.EmployeesAttendanceApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee_attendance**](EmployeesAttendanceApi.md#create_employee_attendance) | **POST** /api/employees/v1/attendance/create | Create employee attendance
[**delete_employee_attendance**](EmployeesAttendanceApi.md#delete_employee_attendance) | **POST** /api/employees/v1/attendance/delete | Delete employee attendance
[**list_employee_attendance_types**](EmployeesAttendanceApi.md#list_employee_attendance_types) | **POST** /api/employees/v1/attendance-type/list | List attendance types
[**list_employee_attendances**](EmployeesAttendanceApi.md#list_employee_attendances) | **POST** /api/employees/v1/attendance/list | List employee attendances
[**update_employee_attendance**](EmployeesAttendanceApi.md#update_employee_attendance) | **POST** /api/employees/v1/attendance/update | Update employee attendance


# **create_employee_attendance**
> AttendanceCreateResponse create_employee_attendance(attendance_create_request, timeout=timeout)

Create employee attendance

Creates a closed employee attendance and returns the creation result

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.attendance_create_request import AttendanceCreateRequest
from iikocloud_client.models.attendance_create_response import AttendanceCreateResponse
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
    api_instance = iikocloud_client.EmployeesAttendanceApi(api_client)
    attendance_create_request = iikocloud_client.AttendanceCreateRequest() # AttendanceCreateRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create employee attendance
        api_response = await api_instance.create_employee_attendance(attendance_create_request, timeout=timeout)
        print("The response of EmployeesAttendanceApi->create_employee_attendance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesAttendanceApi->create_employee_attendance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attendance_create_request** | [**AttendanceCreateRequest**](AttendanceCreateRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AttendanceCreateResponse**](AttendanceCreateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable entity |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_employee_attendance**
> AttendanceDeleteResponse delete_employee_attendance(attendance_delete_request, timeout=timeout)

Delete employee attendance

Irreversibly deletes a single attendance

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.attendance_delete_request import AttendanceDeleteRequest
from iikocloud_client.models.attendance_delete_response import AttendanceDeleteResponse
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
    api_instance = iikocloud_client.EmployeesAttendanceApi(api_client)
    attendance_delete_request = iikocloud_client.AttendanceDeleteRequest() # AttendanceDeleteRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete employee attendance
        api_response = await api_instance.delete_employee_attendance(attendance_delete_request, timeout=timeout)
        print("The response of EmployeesAttendanceApi->delete_employee_attendance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesAttendanceApi->delete_employee_attendance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attendance_delete_request** | [**AttendanceDeleteRequest**](AttendanceDeleteRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AttendanceDeleteResponse**](AttendanceDeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable entity |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_attendance_types**
> AttendanceTypeListResponse list_employee_attendance_types(attendance_type_list_request, timeout=timeout)

List attendance types

Returns the attendance type catalog

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.attendance_type_list_request import AttendanceTypeListRequest
from iikocloud_client.models.attendance_type_list_response import AttendanceTypeListResponse
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
    api_instance = iikocloud_client.EmployeesAttendanceApi(api_client)
    attendance_type_list_request = iikocloud_client.AttendanceTypeListRequest() # AttendanceTypeListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # List attendance types
        api_response = await api_instance.list_employee_attendance_types(attendance_type_list_request, timeout=timeout)
        print("The response of EmployeesAttendanceApi->list_employee_attendance_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesAttendanceApi->list_employee_attendance_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attendance_type_list_request** | [**AttendanceTypeListRequest**](AttendanceTypeListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AttendanceTypeListResponse**](AttendanceTypeListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_employee_attendances**
> AttendanceListResponse list_employee_attendances(attendance_list_request, timeout=timeout)

List employee attendances

Returns attendances within one organization for a period

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.attendance_list_request import AttendanceListRequest
from iikocloud_client.models.attendance_list_response import AttendanceListResponse
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
    api_instance = iikocloud_client.EmployeesAttendanceApi(api_client)
    attendance_list_request = iikocloud_client.AttendanceListRequest() # AttendanceListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # List employee attendances
        api_response = await api_instance.list_employee_attendances(attendance_list_request, timeout=timeout)
        print("The response of EmployeesAttendanceApi->list_employee_attendances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesAttendanceApi->list_employee_attendances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attendance_list_request** | [**AttendanceListRequest**](AttendanceListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AttendanceListResponse**](AttendanceListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_attendance**
> AttendanceUpdateResponse update_employee_attendance(attendance_update_request, timeout=timeout)

Update employee attendance

Updates an attendance; when the organization is changed, a new attendance with a new id is created

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.attendance_update_request import AttendanceUpdateRequest
from iikocloud_client.models.attendance_update_response import AttendanceUpdateResponse
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
    api_instance = iikocloud_client.EmployeesAttendanceApi(api_client)
    attendance_update_request = iikocloud_client.AttendanceUpdateRequest() # AttendanceUpdateRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update employee attendance
        api_response = await api_instance.update_employee_attendance(attendance_update_request, timeout=timeout)
        print("The response of EmployeesAttendanceApi->update_employee_attendance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmployeesAttendanceApi->update_employee_attendance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attendance_update_request** | [**AttendanceUpdateRequest**](AttendanceUpdateRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AttendanceUpdateResponse**](AttendanceUpdateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable entity |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

