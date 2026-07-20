# iikocloud_client.BanquetsReservesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_banquet_order_items**](BanquetsReservesApi.md#add_banquet_order_items) | **POST** /api/1/reserve/add_items | Add order items.
[**add_banquet_order_payments**](BanquetsReservesApi.md#add_banquet_order_payments) | **POST** /api/1/reserve/add_payments | Add order payments.
[**cancel_reserve**](BanquetsReservesApi.md#cancel_reserve) | **POST** /api/1/reserve/cancel | Cancel reservation due to some reason.
[**change_banquet_order_items**](BanquetsReservesApi.md#change_banquet_order_items) | **POST** /api/1/reserve/change_items | Change order items.
[**change_reserve_estimated_start_time**](BanquetsReservesApi.md#change_reserve_estimated_start_time) | **POST** /api/1/reserve/change_estimated_start_time | Change reserve/banquet estimated start time.
[**change_reserve_tables**](BanquetsReservesApi.md#change_reserve_tables) | **POST** /api/1/reserve/change_tables | Change reserve/banquet tables.
[**create_reserve**](BanquetsReservesApi.md#create_reserve) | **POST** /api/1/reserve/create | Create banquet/reserve.
[**get_reserve_available_organizations**](BanquetsReservesApi.md#get_reserve_available_organizations) | **POST** /api/1/reserve/available_organizations | Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.
[**get_reserve_restaurant_sections**](BanquetsReservesApi.md#get_reserve_restaurant_sections) | **POST** /api/1/reserve/available_restaurant_sections | Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.
[**get_reserve_statuses_by_id**](BanquetsReservesApi.md#get_reserve_statuses_by_id) | **POST** /api/1/reserve/status_by_id | Retrieve banquets/reserves statuses by IDs.
[**get_reserve_terminal_groups**](BanquetsReservesApi.md#get_reserve_terminal_groups) | **POST** /api/1/reserve/available_terminal_groups | Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.
[**get_restaurant_sections_workload**](BanquetsReservesApi.md#get_restaurant_sections_workload) | **POST** /api/1/reserve/restaurant_sections_workload | Returns all banquets/reserves for passed restaurant sections.


# **add_banquet_order_items**
> CorrelationIdResponse add_banquet_order_items(timeout=timeout, add_order_items_to_banquet_request=add_order_items_to_banquet_request)

Add order items.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_order_items_to_banquet_request import AddOrderItemsToBanquetRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_order_items_to_banquet_request = iikocloud_client.AddOrderItemsToBanquetRequest() # AddOrderItemsToBanquetRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.add_banquet_order_items(timeout=timeout, add_order_items_to_banquet_request=add_order_items_to_banquet_request)
        print("The response of BanquetsReservesApi->add_banquet_order_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->add_banquet_order_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_order_items_to_banquet_request** | [**AddOrderItemsToBanquetRequest**](AddOrderItemsToBanquetRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **add_banquet_order_payments**
> CorrelationIdResponse add_banquet_order_payments(timeout=timeout, add_order_payments_to_banquet_request=add_order_payments_to_banquet_request)

Add order payments.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_order_payments_to_banquet_request import AddOrderPaymentsToBanquetRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_order_payments_to_banquet_request = iikocloud_client.AddOrderPaymentsToBanquetRequest() # AddOrderPaymentsToBanquetRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.add_banquet_order_payments(timeout=timeout, add_order_payments_to_banquet_request=add_order_payments_to_banquet_request)
        print("The response of BanquetsReservesApi->add_banquet_order_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->add_banquet_order_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_order_payments_to_banquet_request** | [**AddOrderPaymentsToBanquetRequest**](AddOrderPaymentsToBanquetRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **cancel_reserve**
> CorrelationIdResponse cancel_reserve(timeout=timeout, cancel_reserve_request=cancel_reserve_request)

Cancel reservation due to some reason.

Available only for reserves with status 'New'.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cancel_reserve_request import CancelReserveRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    cancel_reserve_request = iikocloud_client.CancelReserveRequest() # CancelReserveRequest |  (optional)

    try:
        # Cancel reservation due to some reason.
        api_response = await api_instance.cancel_reserve(timeout=timeout, cancel_reserve_request=cancel_reserve_request)
        print("The response of BanquetsReservesApi->cancel_reserve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->cancel_reserve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **cancel_reserve_request** | [**CancelReserveRequest**](CancelReserveRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_banquet_order_items**
> CorrelationIdResponse change_banquet_order_items(timeout=timeout, change_banquet_order_items_request=change_banquet_order_items_request)

Change order items.

Available only for banquets.

 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_banquet_order_items_request import ChangeBanquetOrderItemsRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_banquet_order_items_request = iikocloud_client.ChangeBanquetOrderItemsRequest() # ChangeBanquetOrderItemsRequest |  (optional)

    try:
        # Change order items.
        api_response = await api_instance.change_banquet_order_items(timeout=timeout, change_banquet_order_items_request=change_banquet_order_items_request)
        print("The response of BanquetsReservesApi->change_banquet_order_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->change_banquet_order_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_banquet_order_items_request** | [**ChangeBanquetOrderItemsRequest**](ChangeBanquetOrderItemsRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_reserve_estimated_start_time**
> CorrelationIdResponse change_reserve_estimated_start_time(timeout=timeout, change_reserve_estimated_start_time_request=change_reserve_estimated_start_time_request)

Change reserve/banquet estimated start time.



 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_reserve_estimated_start_time_request import ChangeReserveEstimatedStartTimeRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_reserve_estimated_start_time_request = iikocloud_client.ChangeReserveEstimatedStartTimeRequest() # ChangeReserveEstimatedStartTimeRequest |  (optional)

    try:
        # Change reserve/banquet estimated start time.
        api_response = await api_instance.change_reserve_estimated_start_time(timeout=timeout, change_reserve_estimated_start_time_request=change_reserve_estimated_start_time_request)
        print("The response of BanquetsReservesApi->change_reserve_estimated_start_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->change_reserve_estimated_start_time: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_reserve_estimated_start_time_request** | [**ChangeReserveEstimatedStartTimeRequest**](ChangeReserveEstimatedStartTimeRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **change_reserve_tables**
> CorrelationIdResponse change_reserve_tables(timeout=timeout, change_reserve_tables_request=change_reserve_tables_request)

Change reserve/banquet tables.



 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_reserve_tables_request import ChangeReserveTablesRequest
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_reserve_tables_request = iikocloud_client.ChangeReserveTablesRequest() # ChangeReserveTablesRequest |  (optional)

    try:
        # Change reserve/banquet tables.
        api_response = await api_instance.change_reserve_tables(timeout=timeout, change_reserve_tables_request=change_reserve_tables_request)
        print("The response of BanquetsReservesApi->change_reserve_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->change_reserve_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_reserve_tables_request** | [**ChangeReserveTablesRequest**](ChangeReserveTablesRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

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

# **create_reserve**
> ReserveResponse create_reserve(timeout=timeout, create_reserve_request=create_reserve_request)

Create banquet/reserve.



 > Allowed from version `7.1.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.create_reserve_request import CreateReserveRequest
from iikocloud_client.models.reserve_response import ReserveResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    create_reserve_request = iikocloud_client.CreateReserveRequest() # CreateReserveRequest |  (optional)

    try:
        # Create banquet/reserve.
        api_response = await api_instance.create_reserve(timeout=timeout, create_reserve_request=create_reserve_request)
        print("The response of BanquetsReservesApi->create_reserve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->create_reserve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **create_reserve_request** | [**CreateReserveRequest**](CreateReserveRequest.md)|  | [optional] 

### Return type

[**ReserveResponse**](ReserveResponse.md)

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

# **get_reserve_available_organizations**
> GetOrganizationsResponse get_reserve_available_organizations(timeout=timeout, get_organizations_request=get_organizations_request)

Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_organizations_request = iikocloud_client.GetOrganizationsRequest() # GetOrganizationsRequest |  (optional)

    try:
        # Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.
        api_response = await api_instance.get_reserve_available_organizations(timeout=timeout, get_organizations_request=get_organizations_request)
        print("The response of BanquetsReservesApi->get_reserve_available_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->get_reserve_available_organizations: %s\n" % e)
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

# **get_reserve_restaurant_sections**
> GetRestaurantSectionsResponse get_reserve_restaurant_sections(timeout=timeout, get_restaurant_sections_request=get_restaurant_sections_request)

Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_restaurant_sections_request import GetRestaurantSectionsRequest
from iikocloud_client.models.get_restaurant_sections_response import GetRestaurantSectionsResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_restaurant_sections_request = iikocloud_client.GetRestaurantSectionsRequest() # GetRestaurantSectionsRequest |  (optional)

    try:
        # Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.
        api_response = await api_instance.get_reserve_restaurant_sections(timeout=timeout, get_restaurant_sections_request=get_restaurant_sections_request)
        print("The response of BanquetsReservesApi->get_reserve_restaurant_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->get_reserve_restaurant_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_restaurant_sections_request** | [**GetRestaurantSectionsRequest**](GetRestaurantSectionsRequest.md)|  | [optional] 

### Return type

[**GetRestaurantSectionsResponse**](GetRestaurantSectionsResponse.md)

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

# **get_reserve_statuses_by_id**
> ReservesResponse get_reserve_statuses_by_id(timeout=timeout, reserves_by_id_request=reserves_by_id_request)

Retrieve banquets/reserves statuses by IDs.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.reserves_by_id_request import ReservesByIdRequest
from iikocloud_client.models.reserves_response import ReservesResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_by_id_request = iikocloud_client.ReservesByIdRequest() # ReservesByIdRequest |  (optional)

    try:
        # Retrieve banquets/reserves statuses by IDs.
        api_response = await api_instance.get_reserve_statuses_by_id(timeout=timeout, reserves_by_id_request=reserves_by_id_request)
        print("The response of BanquetsReservesApi->get_reserve_statuses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->get_reserve_statuses_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_by_id_request** | [**ReservesByIdRequest**](ReservesByIdRequest.md)|  | [optional] 

### Return type

[**ReservesResponse**](ReservesResponse.md)

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

# **get_reserve_terminal_groups**
> TerminalGroupsResponse get_reserve_terminal_groups(timeout=timeout, get_terminal_groups_by_organizations_request=get_terminal_groups_by_organizations_request)

Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_terminal_groups_by_organizations_request import GetTerminalGroupsByOrganizationsRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_terminal_groups_by_organizations_request = iikocloud_client.GetTerminalGroupsByOrganizationsRequest() # GetTerminalGroupsByOrganizationsRequest |  (optional)

    try:
        # Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.
        api_response = await api_instance.get_reserve_terminal_groups(timeout=timeout, get_terminal_groups_by_organizations_request=get_terminal_groups_by_organizations_request)
        print("The response of BanquetsReservesApi->get_reserve_terminal_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->get_reserve_terminal_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_terminal_groups_by_organizations_request** | [**GetTerminalGroupsByOrganizationsRequest**](GetTerminalGroupsByOrganizationsRequest.md)|  | [optional] 

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

# **get_restaurant_sections_workload**
> GetRestaurantSectionsWorkloadResponse get_restaurant_sections_workload(timeout=timeout, get_restaurant_sections_workload_request=get_restaurant_sections_workload_request)

Returns all banquets/reserves for passed restaurant sections.



 > Allowed from version `7.1.5`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_restaurant_sections_workload_request import GetRestaurantSectionsWorkloadRequest
from iikocloud_client.models.get_restaurant_sections_workload_response import GetRestaurantSectionsWorkloadResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_restaurant_sections_workload_request = iikocloud_client.GetRestaurantSectionsWorkloadRequest() # GetRestaurantSectionsWorkloadRequest |  (optional)

    try:
        # Returns all banquets/reserves for passed restaurant sections.
        api_response = await api_instance.get_restaurant_sections_workload(timeout=timeout, get_restaurant_sections_workload_request=get_restaurant_sections_workload_request)
        print("The response of BanquetsReservesApi->get_restaurant_sections_workload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->get_restaurant_sections_workload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_restaurant_sections_workload_request** | [**GetRestaurantSectionsWorkloadRequest**](GetRestaurantSectionsWorkloadRequest.md)|  | [optional] 

### Return type

[**GetRestaurantSectionsWorkloadResponse**](GetRestaurantSectionsWorkloadResponse.md)

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

