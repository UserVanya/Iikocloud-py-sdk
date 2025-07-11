# iikocloud_client.BanquetsReservesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_reserve_add_items_post**](BanquetsReservesApi.md#api1_reserve_add_items_post) | **POST** /api/1/reserve/add_items | Add order items.
[**api1_reserve_add_payments_post**](BanquetsReservesApi.md#api1_reserve_add_payments_post) | **POST** /api/1/reserve/add_payments | Add order payments.
[**api1_reserve_available_organizations_post**](BanquetsReservesApi.md#api1_reserve_available_organizations_post) | **POST** /api/1/reserve/available_organizations | Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.
[**api1_reserve_available_restaurant_sections_post**](BanquetsReservesApi.md#api1_reserve_available_restaurant_sections_post) | **POST** /api/1/reserve/available_restaurant_sections | Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.
[**api1_reserve_available_terminal_groups_post**](BanquetsReservesApi.md#api1_reserve_available_terminal_groups_post) | **POST** /api/1/reserve/available_terminal_groups | Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.
[**api1_reserve_cancel_post**](BanquetsReservesApi.md#api1_reserve_cancel_post) | **POST** /api/1/reserve/cancel | Cancel reservation due to some reason.
[**api1_reserve_create_post**](BanquetsReservesApi.md#api1_reserve_create_post) | **POST** /api/1/reserve/create | Create banquet/reserve.
[**api1_reserve_restaurant_sections_workload_post**](BanquetsReservesApi.md#api1_reserve_restaurant_sections_workload_post) | **POST** /api/1/reserve/restaurant_sections_workload | Returns all banquets/reserves for passed restaurant sections.
[**api1_reserve_status_by_id_post**](BanquetsReservesApi.md#api1_reserve_status_by_id_post) | **POST** /api/1/reserve/status_by_id | Retrieve banquets/reserves statuses by IDs.


# **api1_reserve_add_items_post**
> TransportCommonCorrelationIdResponse api1_reserve_add_items_post(authorization, timeout=timeout, transport_reserves_add_order_items_to_banquet_request=transport_reserves_add_order_items_to_banquet_request)

Add order items.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_reserves_add_order_items_to_banquet_request import TransportReservesAddOrderItemsToBanquetRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_reserves_add_order_items_to_banquet_request = iikocloud_client.TransportReservesAddOrderItemsToBanquetRequest() # TransportReservesAddOrderItemsToBanquetRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.api1_reserve_add_items_post(authorization, timeout=timeout, transport_reserves_add_order_items_to_banquet_request=transport_reserves_add_order_items_to_banquet_request)
        print("The response of BanquetsReservesApi->api1_reserve_add_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->api1_reserve_add_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_add_order_items_to_banquet_request** | [**TransportReservesAddOrderItemsToBanquetRequest**](TransportReservesAddOrderItemsToBanquetRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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

# **api1_reserve_add_payments_post**
> TransportCommonCorrelationIdResponse api1_reserve_add_payments_post(authorization, timeout=timeout, transport_reserves_add_order_payments_to_banquet_request=transport_reserves_add_order_payments_to_banquet_request)

Add order payments.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_reserves_add_order_payments_to_banquet_request import TransportReservesAddOrderPaymentsToBanquetRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_reserves_add_order_payments_to_banquet_request = iikocloud_client.TransportReservesAddOrderPaymentsToBanquetRequest() # TransportReservesAddOrderPaymentsToBanquetRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.api1_reserve_add_payments_post(authorization, timeout=timeout, transport_reserves_add_order_payments_to_banquet_request=transport_reserves_add_order_payments_to_banquet_request)
        print("The response of BanquetsReservesApi->api1_reserve_add_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->api1_reserve_add_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_add_order_payments_to_banquet_request** | [**TransportReservesAddOrderPaymentsToBanquetRequest**](TransportReservesAddOrderPaymentsToBanquetRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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

# **api1_reserve_available_organizations_post**
> TransportOrganizationsGetOrganizationsResponse api1_reserve_available_organizations_post(authorization, timeout=timeout, transport_organizations_get_organizations_request=transport_organizations_get_organizations_request)

Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_organizations_get_organizations_request import TransportOrganizationsGetOrganizationsRequest
from iikocloud_client.models.transport_organizations_get_organizations_response import TransportOrganizationsGetOrganizationsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_organizations_get_organizations_request = iikocloud_client.TransportOrganizationsGetOrganizationsRequest() # TransportOrganizationsGetOrganizationsRequest |  (optional)

    try:
        # Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.
        api_response = await api_instance.api1_reserve_available_organizations_post(authorization, timeout=timeout, transport_organizations_get_organizations_request=transport_organizations_get_organizations_request)
        print("The response of BanquetsReservesApi->api1_reserve_available_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->api1_reserve_available_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_organizations_get_organizations_request** | [**TransportOrganizationsGetOrganizationsRequest**](TransportOrganizationsGetOrganizationsRequest.md)|  | [optional] 

### Return type

[**TransportOrganizationsGetOrganizationsResponse**](TransportOrganizationsGetOrganizationsResponse.md)

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

# **api1_reserve_available_restaurant_sections_post**
> TransportReservesGetRestaurantSectionsResponse api1_reserve_available_restaurant_sections_post(authorization, timeout=timeout, transport_reserves_get_restaurant_sections_request=transport_reserves_get_restaurant_sections_request)

Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_reserves_get_restaurant_sections_request import TransportReservesGetRestaurantSectionsRequest
from iikocloud_client.models.transport_reserves_get_restaurant_sections_response import TransportReservesGetRestaurantSectionsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_reserves_get_restaurant_sections_request = iikocloud_client.TransportReservesGetRestaurantSectionsRequest() # TransportReservesGetRestaurantSectionsRequest |  (optional)

    try:
        # Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.
        api_response = await api_instance.api1_reserve_available_restaurant_sections_post(authorization, timeout=timeout, transport_reserves_get_restaurant_sections_request=transport_reserves_get_restaurant_sections_request)
        print("The response of BanquetsReservesApi->api1_reserve_available_restaurant_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->api1_reserve_available_restaurant_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_get_restaurant_sections_request** | [**TransportReservesGetRestaurantSectionsRequest**](TransportReservesGetRestaurantSectionsRequest.md)|  | [optional] 

### Return type

[**TransportReservesGetRestaurantSectionsResponse**](TransportReservesGetRestaurantSectionsResponse.md)

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

# **api1_reserve_available_terminal_groups_post**
> TransportTerminalsTerminalGroupsResponse api1_reserve_available_terminal_groups_post(authorization, timeout=timeout, transport_terminals_get_terminal_groups_by_organizations_request=transport_terminals_get_terminal_groups_by_organizations_request)

Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_terminals_get_terminal_groups_by_organizations_request import TransportTerminalsGetTerminalGroupsByOrganizationsRequest
from iikocloud_client.models.transport_terminals_terminal_groups_response import TransportTerminalsTerminalGroupsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_terminals_get_terminal_groups_by_organizations_request = iikocloud_client.TransportTerminalsGetTerminalGroupsByOrganizationsRequest() # TransportTerminalsGetTerminalGroupsByOrganizationsRequest |  (optional)

    try:
        # Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.
        api_response = await api_instance.api1_reserve_available_terminal_groups_post(authorization, timeout=timeout, transport_terminals_get_terminal_groups_by_organizations_request=transport_terminals_get_terminal_groups_by_organizations_request)
        print("The response of BanquetsReservesApi->api1_reserve_available_terminal_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->api1_reserve_available_terminal_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_terminals_get_terminal_groups_by_organizations_request** | [**TransportTerminalsGetTerminalGroupsByOrganizationsRequest**](TransportTerminalsGetTerminalGroupsByOrganizationsRequest.md)|  | [optional] 

### Return type

[**TransportTerminalsTerminalGroupsResponse**](TransportTerminalsTerminalGroupsResponse.md)

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

# **api1_reserve_cancel_post**
> TransportCommonCorrelationIdResponse api1_reserve_cancel_post(authorization, timeout=timeout, transport_reserves_cancel_reserve_request=transport_reserves_cancel_reserve_request)

Cancel reservation due to some reason.

Available only for reserves with status 'New'.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_reserves_cancel_reserve_request import TransportReservesCancelReserveRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_reserves_cancel_reserve_request = iikocloud_client.TransportReservesCancelReserveRequest() # TransportReservesCancelReserveRequest |  (optional)

    try:
        # Cancel reservation due to some reason.
        api_response = await api_instance.api1_reserve_cancel_post(authorization, timeout=timeout, transport_reserves_cancel_reserve_request=transport_reserves_cancel_reserve_request)
        print("The response of BanquetsReservesApi->api1_reserve_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->api1_reserve_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_cancel_reserve_request** | [**TransportReservesCancelReserveRequest**](TransportReservesCancelReserveRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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

# **api1_reserve_create_post**
> TransportReservesReserveResponse api1_reserve_create_post(authorization, timeout=timeout, transport_reserves_create_reserve_request=transport_reserves_create_reserve_request)

Create banquet/reserve.



 > Allowed from version `7.1.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_reserves_create_reserve_request import TransportReservesCreateReserveRequest
from iikocloud_client.models.transport_reserves_reserve_response import TransportReservesReserveResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_reserves_create_reserve_request = iikocloud_client.TransportReservesCreateReserveRequest() # TransportReservesCreateReserveRequest |  (optional)

    try:
        # Create banquet/reserve.
        api_response = await api_instance.api1_reserve_create_post(authorization, timeout=timeout, transport_reserves_create_reserve_request=transport_reserves_create_reserve_request)
        print("The response of BanquetsReservesApi->api1_reserve_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->api1_reserve_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_create_reserve_request** | [**TransportReservesCreateReserveRequest**](TransportReservesCreateReserveRequest.md)|  | [optional] 

### Return type

[**TransportReservesReserveResponse**](TransportReservesReserveResponse.md)

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

# **api1_reserve_restaurant_sections_workload_post**
> TransportReservesGetRestaurantSectionsWorkloadResponse api1_reserve_restaurant_sections_workload_post(authorization, timeout=timeout, transport_reserves_get_restaurant_sections_workload_request=transport_reserves_get_restaurant_sections_workload_request)

Returns all banquets/reserves for passed restaurant sections.



 > Allowed from version `7.1.5`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_reserves_get_restaurant_sections_workload_request import TransportReservesGetRestaurantSectionsWorkloadRequest
from iikocloud_client.models.transport_reserves_get_restaurant_sections_workload_response import TransportReservesGetRestaurantSectionsWorkloadResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_reserves_get_restaurant_sections_workload_request = iikocloud_client.TransportReservesGetRestaurantSectionsWorkloadRequest() # TransportReservesGetRestaurantSectionsWorkloadRequest |  (optional)

    try:
        # Returns all banquets/reserves for passed restaurant sections.
        api_response = await api_instance.api1_reserve_restaurant_sections_workload_post(authorization, timeout=timeout, transport_reserves_get_restaurant_sections_workload_request=transport_reserves_get_restaurant_sections_workload_request)
        print("The response of BanquetsReservesApi->api1_reserve_restaurant_sections_workload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->api1_reserve_restaurant_sections_workload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_get_restaurant_sections_workload_request** | [**TransportReservesGetRestaurantSectionsWorkloadRequest**](TransportReservesGetRestaurantSectionsWorkloadRequest.md)|  | [optional] 

### Return type

[**TransportReservesGetRestaurantSectionsWorkloadResponse**](TransportReservesGetRestaurantSectionsWorkloadResponse.md)

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

# **api1_reserve_status_by_id_post**
> TransportReservesReservesResponse api1_reserve_status_by_id_post(authorization, timeout=timeout, transport_reserves_reserves_by_id_request=transport_reserves_reserves_by_id_request)

Retrieve banquets/reserves statuses by IDs.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_reserves_reserves_by_id_request import TransportReservesReservesByIdRequest
from iikocloud_client.models.transport_reserves_reserves_response import TransportReservesReservesResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_reserves_reserves_by_id_request = iikocloud_client.TransportReservesReservesByIdRequest() # TransportReservesReservesByIdRequest |  (optional)

    try:
        # Retrieve banquets/reserves statuses by IDs.
        api_response = await api_instance.api1_reserve_status_by_id_post(authorization, timeout=timeout, transport_reserves_reserves_by_id_request=transport_reserves_reserves_by_id_request)
        print("The response of BanquetsReservesApi->api1_reserve_status_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->api1_reserve_status_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_reserves_reserves_by_id_request** | [**TransportReservesReservesByIdRequest**](TransportReservesReservesByIdRequest.md)|  | [optional] 

### Return type

[**TransportReservesReservesResponse**](TransportReservesReservesResponse.md)

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

