# iikocloud_client.BanquetsReservesApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reserve_add_items_post**](BanquetsReservesApi.md#reserve_add_items_post) | **POST** /reserve/add_items | Add order items.
[**reserve_add_payments_post**](BanquetsReservesApi.md#reserve_add_payments_post) | **POST** /reserve/add_payments | Add order payments.
[**reserve_available_organizations_post**](BanquetsReservesApi.md#reserve_available_organizations_post) | **POST** /reserve/available_organizations | Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.
[**reserve_available_restaurant_sections_post**](BanquetsReservesApi.md#reserve_available_restaurant_sections_post) | **POST** /reserve/available_restaurant_sections | Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.
[**reserve_available_terminal_groups_post**](BanquetsReservesApi.md#reserve_available_terminal_groups_post) | **POST** /reserve/available_terminal_groups | Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.
[**reserve_cancel_post**](BanquetsReservesApi.md#reserve_cancel_post) | **POST** /reserve/cancel | Cancel reservation due to some reason.
[**reserve_change_estimated_start_time_post**](BanquetsReservesApi.md#reserve_change_estimated_start_time_post) | **POST** /reserve/change_estimated_start_time | Change reserve/banquet estimated start time.
[**reserve_change_items_post**](BanquetsReservesApi.md#reserve_change_items_post) | **POST** /reserve/change_items | Change order items.
[**reserve_change_tables_post**](BanquetsReservesApi.md#reserve_change_tables_post) | **POST** /reserve/change_tables | Change reserve/banquet tables.
[**reserve_create_post**](BanquetsReservesApi.md#reserve_create_post) | **POST** /reserve/create | Create banquet/reserve.
[**reserve_restaurant_sections_workload_post**](BanquetsReservesApi.md#reserve_restaurant_sections_workload_post) | **POST** /reserve/restaurant_sections_workload | Returns all banquets/reserves for passed restaurant sections.
[**reserve_status_by_id_post**](BanquetsReservesApi.md#reserve_status_by_id_post) | **POST** /reserve/status_by_id | Retrieve banquets/reserves statuses by IDs.


# **reserve_add_items_post**
> CommonCorrelationIdResponse reserve_add_items_post(timeout=timeout, reserves_add_order_items_to_banquet_request=reserves_add_order_items_to_banquet_request)

Add order items.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.reserves_add_order_items_to_banquet_request import ReservesAddOrderItemsToBanquetRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_add_order_items_to_banquet_request = iikocloud_client.ReservesAddOrderItemsToBanquetRequest() # ReservesAddOrderItemsToBanquetRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.reserve_add_items_post(timeout=timeout, reserves_add_order_items_to_banquet_request=reserves_add_order_items_to_banquet_request)
        print("The response of BanquetsReservesApi->reserve_add_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_add_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_add_order_items_to_banquet_request** | [**ReservesAddOrderItemsToBanquetRequest**](ReservesAddOrderItemsToBanquetRequest.md)|  | [optional] 

### Return type

[**CommonCorrelationIdResponse**](CommonCorrelationIdResponse.md)

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

# **reserve_add_payments_post**
> CommonCorrelationIdResponse reserve_add_payments_post(timeout=timeout, reserves_add_order_payments_to_banquet_request=reserves_add_order_payments_to_banquet_request)

Add order payments.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.reserves_add_order_payments_to_banquet_request import ReservesAddOrderPaymentsToBanquetRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_add_order_payments_to_banquet_request = iikocloud_client.ReservesAddOrderPaymentsToBanquetRequest() # ReservesAddOrderPaymentsToBanquetRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.reserve_add_payments_post(timeout=timeout, reserves_add_order_payments_to_banquet_request=reserves_add_order_payments_to_banquet_request)
        print("The response of BanquetsReservesApi->reserve_add_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_add_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_add_order_payments_to_banquet_request** | [**ReservesAddOrderPaymentsToBanquetRequest**](ReservesAddOrderPaymentsToBanquetRequest.md)|  | [optional] 

### Return type

[**CommonCorrelationIdResponse**](CommonCorrelationIdResponse.md)

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

# **reserve_available_organizations_post**
> OrganizationsGetOrganizationsResponse reserve_available_organizations_post(timeout=timeout, organizations_get_organizations_request=organizations_get_organizations_request)

Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.organizations_get_organizations_request import OrganizationsGetOrganizationsRequest
from iikocloud_client.models.organizations_get_organizations_response import OrganizationsGetOrganizationsResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    organizations_get_organizations_request = iikocloud_client.OrganizationsGetOrganizationsRequest() # OrganizationsGetOrganizationsRequest |  (optional)

    try:
        # Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.
        api_response = await api_instance.reserve_available_organizations_post(timeout=timeout, organizations_get_organizations_request=organizations_get_organizations_request)
        print("The response of BanquetsReservesApi->reserve_available_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_available_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **organizations_get_organizations_request** | [**OrganizationsGetOrganizationsRequest**](OrganizationsGetOrganizationsRequest.md)|  | [optional] 

### Return type

[**OrganizationsGetOrganizationsResponse**](OrganizationsGetOrganizationsResponse.md)

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

# **reserve_available_restaurant_sections_post**
> ReservesGetRestaurantSectionsResponse reserve_available_restaurant_sections_post(timeout=timeout, reserves_get_restaurant_sections_request=reserves_get_restaurant_sections_request)

Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.reserves_get_restaurant_sections_request import ReservesGetRestaurantSectionsRequest
from iikocloud_client.models.reserves_get_restaurant_sections_response import ReservesGetRestaurantSectionsResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_get_restaurant_sections_request = iikocloud_client.ReservesGetRestaurantSectionsRequest() # ReservesGetRestaurantSectionsRequest |  (optional)

    try:
        # Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.
        api_response = await api_instance.reserve_available_restaurant_sections_post(timeout=timeout, reserves_get_restaurant_sections_request=reserves_get_restaurant_sections_request)
        print("The response of BanquetsReservesApi->reserve_available_restaurant_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_available_restaurant_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_get_restaurant_sections_request** | [**ReservesGetRestaurantSectionsRequest**](ReservesGetRestaurantSectionsRequest.md)|  | [optional] 

### Return type

[**ReservesGetRestaurantSectionsResponse**](ReservesGetRestaurantSectionsResponse.md)

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

# **reserve_available_terminal_groups_post**
> TerminalsTerminalGroupsResponse reserve_available_terminal_groups_post(timeout=timeout, terminals_get_terminal_groups_by_organizations_request=terminals_get_terminal_groups_by_organizations_request)

Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.terminals_get_terminal_groups_by_organizations_request import TerminalsGetTerminalGroupsByOrganizationsRequest
from iikocloud_client.models.terminals_terminal_groups_response import TerminalsTerminalGroupsResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    terminals_get_terminal_groups_by_organizations_request = iikocloud_client.TerminalsGetTerminalGroupsByOrganizationsRequest() # TerminalsGetTerminalGroupsByOrganizationsRequest |  (optional)

    try:
        # Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.
        api_response = await api_instance.reserve_available_terminal_groups_post(timeout=timeout, terminals_get_terminal_groups_by_organizations_request=terminals_get_terminal_groups_by_organizations_request)
        print("The response of BanquetsReservesApi->reserve_available_terminal_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_available_terminal_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **terminals_get_terminal_groups_by_organizations_request** | [**TerminalsGetTerminalGroupsByOrganizationsRequest**](TerminalsGetTerminalGroupsByOrganizationsRequest.md)|  | [optional] 

### Return type

[**TerminalsTerminalGroupsResponse**](TerminalsTerminalGroupsResponse.md)

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

# **reserve_cancel_post**
> CommonCorrelationIdResponse reserve_cancel_post(timeout=timeout, reserves_cancel_reserve_request=reserves_cancel_reserve_request)

Cancel reservation due to some reason.

Available only for reserves with status 'New'.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.reserves_cancel_reserve_request import ReservesCancelReserveRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_cancel_reserve_request = iikocloud_client.ReservesCancelReserveRequest() # ReservesCancelReserveRequest |  (optional)

    try:
        # Cancel reservation due to some reason.
        api_response = await api_instance.reserve_cancel_post(timeout=timeout, reserves_cancel_reserve_request=reserves_cancel_reserve_request)
        print("The response of BanquetsReservesApi->reserve_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_cancel_reserve_request** | [**ReservesCancelReserveRequest**](ReservesCancelReserveRequest.md)|  | [optional] 

### Return type

[**CommonCorrelationIdResponse**](CommonCorrelationIdResponse.md)

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

# **reserve_change_estimated_start_time_post**
> CommonCorrelationIdResponse reserve_change_estimated_start_time_post(timeout=timeout, reserves_change_reserve_estimated_start_time_request=reserves_change_reserve_estimated_start_time_request)

Change reserve/banquet estimated start time.



 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.reserves_change_reserve_estimated_start_time_request import ReservesChangeReserveEstimatedStartTimeRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_change_reserve_estimated_start_time_request = iikocloud_client.ReservesChangeReserveEstimatedStartTimeRequest() # ReservesChangeReserveEstimatedStartTimeRequest |  (optional)

    try:
        # Change reserve/banquet estimated start time.
        api_response = await api_instance.reserve_change_estimated_start_time_post(timeout=timeout, reserves_change_reserve_estimated_start_time_request=reserves_change_reserve_estimated_start_time_request)
        print("The response of BanquetsReservesApi->reserve_change_estimated_start_time_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_change_estimated_start_time_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_change_reserve_estimated_start_time_request** | [**ReservesChangeReserveEstimatedStartTimeRequest**](ReservesChangeReserveEstimatedStartTimeRequest.md)|  | [optional] 

### Return type

[**CommonCorrelationIdResponse**](CommonCorrelationIdResponse.md)

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

# **reserve_change_items_post**
> CommonCorrelationIdResponse reserve_change_items_post(timeout=timeout, reserves_change_banquet_order_items_request=reserves_change_banquet_order_items_request)

Change order items.

Available only for banquets.

 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.reserves_change_banquet_order_items_request import ReservesChangeBanquetOrderItemsRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_change_banquet_order_items_request = iikocloud_client.ReservesChangeBanquetOrderItemsRequest() # ReservesChangeBanquetOrderItemsRequest |  (optional)

    try:
        # Change order items.
        api_response = await api_instance.reserve_change_items_post(timeout=timeout, reserves_change_banquet_order_items_request=reserves_change_banquet_order_items_request)
        print("The response of BanquetsReservesApi->reserve_change_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_change_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_change_banquet_order_items_request** | [**ReservesChangeBanquetOrderItemsRequest**](ReservesChangeBanquetOrderItemsRequest.md)|  | [optional] 

### Return type

[**CommonCorrelationIdResponse**](CommonCorrelationIdResponse.md)

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

# **reserve_change_tables_post**
> CommonCorrelationIdResponse reserve_change_tables_post(timeout=timeout, reserves_change_reserve_tables_request=reserves_change_reserve_tables_request)

Change reserve/banquet tables.



 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.reserves_change_reserve_tables_request import ReservesChangeReserveTablesRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_change_reserve_tables_request = iikocloud_client.ReservesChangeReserveTablesRequest() # ReservesChangeReserveTablesRequest |  (optional)

    try:
        # Change reserve/banquet tables.
        api_response = await api_instance.reserve_change_tables_post(timeout=timeout, reserves_change_reserve_tables_request=reserves_change_reserve_tables_request)
        print("The response of BanquetsReservesApi->reserve_change_tables_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_change_tables_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_change_reserve_tables_request** | [**ReservesChangeReserveTablesRequest**](ReservesChangeReserveTablesRequest.md)|  | [optional] 

### Return type

[**CommonCorrelationIdResponse**](CommonCorrelationIdResponse.md)

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

# **reserve_create_post**
> ReservesReserveResponse reserve_create_post(timeout=timeout, reserves_create_reserve_request=reserves_create_reserve_request)

Create banquet/reserve.



 > Allowed from version `7.1.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.reserves_create_reserve_request import ReservesCreateReserveRequest
from iikocloud_client.models.reserves_reserve_response import ReservesReserveResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_create_reserve_request = iikocloud_client.ReservesCreateReserveRequest() # ReservesCreateReserveRequest |  (optional)

    try:
        # Create banquet/reserve.
        api_response = await api_instance.reserve_create_post(timeout=timeout, reserves_create_reserve_request=reserves_create_reserve_request)
        print("The response of BanquetsReservesApi->reserve_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_create_reserve_request** | [**ReservesCreateReserveRequest**](ReservesCreateReserveRequest.md)|  | [optional] 

### Return type

[**ReservesReserveResponse**](ReservesReserveResponse.md)

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

# **reserve_restaurant_sections_workload_post**
> ReservesGetRestaurantSectionsWorkloadResponse reserve_restaurant_sections_workload_post(timeout=timeout, reserves_get_restaurant_sections_workload_request=reserves_get_restaurant_sections_workload_request)

Returns all banquets/reserves for passed restaurant sections.



 > Allowed from version `7.1.5`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.reserves_get_restaurant_sections_workload_request import ReservesGetRestaurantSectionsWorkloadRequest
from iikocloud_client.models.reserves_get_restaurant_sections_workload_response import ReservesGetRestaurantSectionsWorkloadResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_get_restaurant_sections_workload_request = iikocloud_client.ReservesGetRestaurantSectionsWorkloadRequest() # ReservesGetRestaurantSectionsWorkloadRequest |  (optional)

    try:
        # Returns all banquets/reserves for passed restaurant sections.
        api_response = await api_instance.reserve_restaurant_sections_workload_post(timeout=timeout, reserves_get_restaurant_sections_workload_request=reserves_get_restaurant_sections_workload_request)
        print("The response of BanquetsReservesApi->reserve_restaurant_sections_workload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_restaurant_sections_workload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_get_restaurant_sections_workload_request** | [**ReservesGetRestaurantSectionsWorkloadRequest**](ReservesGetRestaurantSectionsWorkloadRequest.md)|  | [optional] 

### Return type

[**ReservesGetRestaurantSectionsWorkloadResponse**](ReservesGetRestaurantSectionsWorkloadResponse.md)

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

# **reserve_status_by_id_post**
> ReservesReservesResponse reserve_status_by_id_post(timeout=timeout, reserves_reserves_by_id_request=reserves_reserves_by_id_request)

Retrieve banquets/reserves statuses by IDs.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.reserves_reserves_by_id_request import ReservesReservesByIdRequest
from iikocloud_client.models.reserves_reserves_response import ReservesReservesResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    reserves_reserves_by_id_request = iikocloud_client.ReservesReservesByIdRequest() # ReservesReservesByIdRequest |  (optional)

    try:
        # Retrieve banquets/reserves statuses by IDs.
        api_response = await api_instance.reserve_status_by_id_post(timeout=timeout, reserves_reserves_by_id_request=reserves_reserves_by_id_request)
        print("The response of BanquetsReservesApi->reserve_status_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_status_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **reserves_reserves_by_id_request** | [**ReservesReservesByIdRequest**](ReservesReservesByIdRequest.md)|  | [optional] 

### Return type

[**ReservesReservesResponse**](ReservesReservesResponse.md)

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

