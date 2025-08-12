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
[**reserve_create_post**](BanquetsReservesApi.md#reserve_create_post) | **POST** /reserve/create | Create banquet/reserve.
[**reserve_restaurant_sections_workload_post**](BanquetsReservesApi.md#reserve_restaurant_sections_workload_post) | **POST** /reserve/restaurant_sections_workload | Returns all banquets/reserves for passed restaurant sections.
[**reserve_status_by_id_post**](BanquetsReservesApi.md#reserve_status_by_id_post) | **POST** /reserve/status_by_id | Retrieve banquets/reserves statuses by IDs.


# **reserve_add_items_post**
> TransportCommonCorrelationIdResponse reserve_add_items_post(timeout=timeout, transport_reserves_add_order_items_to_banquet_request=transport_reserves_add_order_items_to_banquet_request)

Add order items.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_reserves_add_order_items_to_banquet_request import TransportReservesAddOrderItemsToBanquetRequest
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
    transport_reserves_add_order_items_to_banquet_request = iikocloud_client.TransportReservesAddOrderItemsToBanquetRequest() # TransportReservesAddOrderItemsToBanquetRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.reserve_add_items_post(timeout=timeout, transport_reserves_add_order_items_to_banquet_request=transport_reserves_add_order_items_to_banquet_request)
        print("The response of BanquetsReservesApi->reserve_add_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_add_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_add_order_items_to_banquet_request** | [**TransportReservesAddOrderItemsToBanquetRequest**](TransportReservesAddOrderItemsToBanquetRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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
> TransportCommonCorrelationIdResponse reserve_add_payments_post(timeout=timeout, transport_reserves_add_order_payments_to_banquet_request=transport_reserves_add_order_payments_to_banquet_request)

Add order payments.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_reserves_add_order_payments_to_banquet_request import TransportReservesAddOrderPaymentsToBanquetRequest
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
    transport_reserves_add_order_payments_to_banquet_request = iikocloud_client.TransportReservesAddOrderPaymentsToBanquetRequest() # TransportReservesAddOrderPaymentsToBanquetRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.reserve_add_payments_post(timeout=timeout, transport_reserves_add_order_payments_to_banquet_request=transport_reserves_add_order_payments_to_banquet_request)
        print("The response of BanquetsReservesApi->reserve_add_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_add_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_add_order_payments_to_banquet_request** | [**TransportReservesAddOrderPaymentsToBanquetRequest**](TransportReservesAddOrderPaymentsToBanquetRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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
> TransportOrganizationsGetOrganizationsResponse reserve_available_organizations_post(timeout=timeout, transport_organizations_get_organizations_request=transport_organizations_get_organizations_request)

Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_organizations_get_organizations_request import TransportOrganizationsGetOrganizationsRequest
from iikocloud_client.models.transport_organizations_get_organizations_response import TransportOrganizationsGetOrganizationsResponse
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
    transport_organizations_get_organizations_request = iikocloud_client.TransportOrganizationsGetOrganizationsRequest() # TransportOrganizationsGetOrganizationsRequest |  (optional)

    try:
        # Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.
        api_response = await api_instance.reserve_available_organizations_post(timeout=timeout, transport_organizations_get_organizations_request=transport_organizations_get_organizations_request)
        print("The response of BanquetsReservesApi->reserve_available_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_available_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_organizations_get_organizations_request** | [**TransportOrganizationsGetOrganizationsRequest**](TransportOrganizationsGetOrganizationsRequest.md)|  | [optional] 

### Return type

[**TransportOrganizationsGetOrganizationsResponse**](TransportOrganizationsGetOrganizationsResponse.md)

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
> TransportReservesGetRestaurantSectionsResponse reserve_available_restaurant_sections_post(timeout=timeout, transport_reserves_get_restaurant_sections_request=transport_reserves_get_restaurant_sections_request)

Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_reserves_get_restaurant_sections_request import TransportReservesGetRestaurantSectionsRequest
from iikocloud_client.models.transport_reserves_get_restaurant_sections_response import TransportReservesGetRestaurantSectionsResponse
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
    transport_reserves_get_restaurant_sections_request = iikocloud_client.TransportReservesGetRestaurantSectionsRequest() # TransportReservesGetRestaurantSectionsRequest |  (optional)

    try:
        # Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.
        api_response = await api_instance.reserve_available_restaurant_sections_post(timeout=timeout, transport_reserves_get_restaurant_sections_request=transport_reserves_get_restaurant_sections_request)
        print("The response of BanquetsReservesApi->reserve_available_restaurant_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_available_restaurant_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_get_restaurant_sections_request** | [**TransportReservesGetRestaurantSectionsRequest**](TransportReservesGetRestaurantSectionsRequest.md)|  | [optional] 

### Return type

[**TransportReservesGetRestaurantSectionsResponse**](TransportReservesGetRestaurantSectionsResponse.md)

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
> TransportTerminalsTerminalGroupsResponse reserve_available_terminal_groups_post(timeout=timeout, transport_terminals_get_terminal_groups_by_organizations_request=transport_terminals_get_terminal_groups_by_organizations_request)

Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_terminals_get_terminal_groups_by_organizations_request import TransportTerminalsGetTerminalGroupsByOrganizationsRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_terminals_get_terminal_groups_by_organizations_request = iikocloud_client.TransportTerminalsGetTerminalGroupsByOrganizationsRequest() # TransportTerminalsGetTerminalGroupsByOrganizationsRequest |  (optional)

    try:
        # Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.
        api_response = await api_instance.reserve_available_terminal_groups_post(timeout=timeout, transport_terminals_get_terminal_groups_by_organizations_request=transport_terminals_get_terminal_groups_by_organizations_request)
        print("The response of BanquetsReservesApi->reserve_available_terminal_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_available_terminal_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_terminals_get_terminal_groups_by_organizations_request** | [**TransportTerminalsGetTerminalGroupsByOrganizationsRequest**](TransportTerminalsGetTerminalGroupsByOrganizationsRequest.md)|  | [optional] 

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

# **reserve_cancel_post**
> TransportCommonCorrelationIdResponse reserve_cancel_post(timeout=timeout, transport_reserves_cancel_reserve_request=transport_reserves_cancel_reserve_request)

Cancel reservation due to some reason.

Available only for reserves with status 'New'.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_reserves_cancel_reserve_request import TransportReservesCancelReserveRequest
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
    transport_reserves_cancel_reserve_request = iikocloud_client.TransportReservesCancelReserveRequest() # TransportReservesCancelReserveRequest |  (optional)

    try:
        # Cancel reservation due to some reason.
        api_response = await api_instance.reserve_cancel_post(timeout=timeout, transport_reserves_cancel_reserve_request=transport_reserves_cancel_reserve_request)
        print("The response of BanquetsReservesApi->reserve_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_cancel_reserve_request** | [**TransportReservesCancelReserveRequest**](TransportReservesCancelReserveRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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
> TransportReservesReserveResponse reserve_create_post(timeout=timeout, transport_reserves_create_reserve_request=transport_reserves_create_reserve_request)

Create banquet/reserve.



 > Allowed from version `7.1.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_reserves_create_reserve_request import TransportReservesCreateReserveRequest
from iikocloud_client.models.transport_reserves_reserve_response import TransportReservesReserveResponse
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
    transport_reserves_create_reserve_request = iikocloud_client.TransportReservesCreateReserveRequest() # TransportReservesCreateReserveRequest |  (optional)

    try:
        # Create banquet/reserve.
        api_response = await api_instance.reserve_create_post(timeout=timeout, transport_reserves_create_reserve_request=transport_reserves_create_reserve_request)
        print("The response of BanquetsReservesApi->reserve_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_create_reserve_request** | [**TransportReservesCreateReserveRequest**](TransportReservesCreateReserveRequest.md)|  | [optional] 

### Return type

[**TransportReservesReserveResponse**](TransportReservesReserveResponse.md)

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
> TransportReservesGetRestaurantSectionsWorkloadResponse reserve_restaurant_sections_workload_post(timeout=timeout, transport_reserves_get_restaurant_sections_workload_request=transport_reserves_get_restaurant_sections_workload_request)

Returns all banquets/reserves for passed restaurant sections.



 > Allowed from version `7.1.5`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_reserves_get_restaurant_sections_workload_request import TransportReservesGetRestaurantSectionsWorkloadRequest
from iikocloud_client.models.transport_reserves_get_restaurant_sections_workload_response import TransportReservesGetRestaurantSectionsWorkloadResponse
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
    transport_reserves_get_restaurant_sections_workload_request = iikocloud_client.TransportReservesGetRestaurantSectionsWorkloadRequest() # TransportReservesGetRestaurantSectionsWorkloadRequest |  (optional)

    try:
        # Returns all banquets/reserves for passed restaurant sections.
        api_response = await api_instance.reserve_restaurant_sections_workload_post(timeout=timeout, transport_reserves_get_restaurant_sections_workload_request=transport_reserves_get_restaurant_sections_workload_request)
        print("The response of BanquetsReservesApi->reserve_restaurant_sections_workload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_restaurant_sections_workload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_get_restaurant_sections_workload_request** | [**TransportReservesGetRestaurantSectionsWorkloadRequest**](TransportReservesGetRestaurantSectionsWorkloadRequest.md)|  | [optional] 

### Return type

[**TransportReservesGetRestaurantSectionsWorkloadResponse**](TransportReservesGetRestaurantSectionsWorkloadResponse.md)

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
> TransportReservesReservesResponse reserve_status_by_id_post(timeout=timeout, transport_reserves_reserves_by_id_request=transport_reserves_reserves_by_id_request)

Retrieve banquets/reserves statuses by IDs.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_reserves_reserves_by_id_request import TransportReservesReservesByIdRequest
from iikocloud_client.models.transport_reserves_reserves_response import TransportReservesReservesResponse
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
    transport_reserves_reserves_by_id_request = iikocloud_client.TransportReservesReservesByIdRequest() # TransportReservesReservesByIdRequest |  (optional)

    try:
        # Retrieve banquets/reserves statuses by IDs.
        api_response = await api_instance.reserve_status_by_id_post(timeout=timeout, transport_reserves_reserves_by_id_request=transport_reserves_reserves_by_id_request)
        print("The response of BanquetsReservesApi->reserve_status_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_status_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_reserves_by_id_request** | [**TransportReservesReservesByIdRequest**](TransportReservesReservesByIdRequest.md)|  | [optional] 

### Return type

[**TransportReservesReservesResponse**](TransportReservesReservesResponse.md)

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

