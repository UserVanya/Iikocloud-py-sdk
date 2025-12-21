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
> IikoTransportPublicApiContractsCommonCorrelationIdResponse reserve_add_items_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request=iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request)

Add order items.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request import IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request = iikocloud_client.IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest() # IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.reserve_add_items_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request=iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request)
        print("The response of BanquetsReservesApi->reserve_add_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_add_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_add_order_items_to_banquet_request** | [**IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest**](IikoTransportPublicApiContractsReservesAddOrderItemsToBanquetRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **reserve_add_payments_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse reserve_add_payments_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request=iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request)

Add order payments.

Available only for banquets.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request import IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request = iikocloud_client.IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest() # IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.reserve_add_payments_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request=iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request)
        print("The response of BanquetsReservesApi->reserve_add_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_add_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_add_order_payments_to_banquet_request** | [**IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest**](IikoTransportPublicApiContractsReservesAddOrderPaymentsToBanquetRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **reserve_available_organizations_post**
> IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse reserve_available_organizations_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_organizations_get_organizations_request=iiko_transport_public_api_contracts_organizations_get_organizations_request)

Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_get_organizations_request import IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_get_organizations_response import IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_organizations_get_organizations_request = iikocloud_client.IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest() # IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest |  (optional)

    try:
        # Returns all organizations of current account (determined by Authorization request header) for which banquet/reserve booking are available.
        api_response = await api_instance.reserve_available_organizations_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_organizations_get_organizations_request=iiko_transport_public_api_contracts_organizations_get_organizations_request)
        print("The response of BanquetsReservesApi->reserve_available_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_available_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_organizations_get_organizations_request** | [**IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest**](IikoTransportPublicApiContractsOrganizationsGetOrganizationsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse**](IikoTransportPublicApiContractsOrganizationsGetOrganizationsResponse.md)

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

# **reserve_available_restaurant_sections_post**
> IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse reserve_available_restaurant_sections_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request=iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request)

Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request import IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_get_restaurant_sections_response import IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request = iikocloud_client.IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest() # IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest |  (optional)

    try:
        # Returns all restaurant sections of specified terminal groups, for which banquet/reserve booking are available.
        api_response = await api_instance.reserve_available_restaurant_sections_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request=iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request)
        print("The response of BanquetsReservesApi->reserve_available_restaurant_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_available_restaurant_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_get_restaurant_sections_request** | [**IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest**](IikoTransportPublicApiContractsReservesGetRestaurantSectionsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse**](IikoTransportPublicApiContractsReservesGetRestaurantSectionsResponse.md)

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

# **reserve_available_terminal_groups_post**
> IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse reserve_available_terminal_groups_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request=iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request)

Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: preparing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request import IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_groups_response import IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request = iikocloud_client.IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest() # IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest |  (optional)

    try:
        # Returns all terminal groups of specified organizations, for which banquet/reserve booking are available.
        api_response = await api_instance.reserve_available_terminal_groups_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request=iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request)
        print("The response of BanquetsReservesApi->reserve_available_terminal_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_available_terminal_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request** | [**IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest**](IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse**](IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse.md)

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

# **reserve_cancel_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse reserve_cancel_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_cancel_reserve_request=iiko_transport_public_api_contracts_reserves_cancel_reserve_request)

Cancel reservation due to some reason.

Available only for reserves with status 'New'.

 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_cancel_reserve_request import IikoTransportPublicApiContractsReservesCancelReserveRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_cancel_reserve_request = iikocloud_client.IikoTransportPublicApiContractsReservesCancelReserveRequest() # IikoTransportPublicApiContractsReservesCancelReserveRequest |  (optional)

    try:
        # Cancel reservation due to some reason.
        api_response = await api_instance.reserve_cancel_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_cancel_reserve_request=iiko_transport_public_api_contracts_reserves_cancel_reserve_request)
        print("The response of BanquetsReservesApi->reserve_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_cancel_reserve_request** | [**IikoTransportPublicApiContractsReservesCancelReserveRequest**](IikoTransportPublicApiContractsReservesCancelReserveRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **reserve_change_estimated_start_time_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse reserve_change_estimated_start_time_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request=iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request)

Change reserve/banquet estimated start time.



 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request import IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request = iikocloud_client.IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest() # IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest |  (optional)

    try:
        # Change reserve/banquet estimated start time.
        api_response = await api_instance.reserve_change_estimated_start_time_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request=iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request)
        print("The response of BanquetsReservesApi->reserve_change_estimated_start_time_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_change_estimated_start_time_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_change_reserve_estimated_start_time_request** | [**IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest**](IikoTransportPublicApiContractsReservesChangeReserveEstimatedStartTimeRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **reserve_change_items_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse reserve_change_items_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request=iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request)

Change order items.

Available only for banquets.

 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request import IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request = iikocloud_client.IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest() # IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest |  (optional)

    try:
        # Change order items.
        api_response = await api_instance.reserve_change_items_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request=iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request)
        print("The response of BanquetsReservesApi->reserve_change_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_change_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_change_banquet_order_items_request** | [**IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest**](IikoTransportPublicApiContractsReservesChangeBanquetOrderItemsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **reserve_change_tables_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse reserve_change_tables_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_change_reserve_tables_request=iiko_transport_public_api_contracts_reserves_change_reserve_tables_request)

Change reserve/banquet tables.



 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_change_reserve_tables_request import IikoTransportPublicApiContractsReservesChangeReserveTablesRequest
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_change_reserve_tables_request = iikocloud_client.IikoTransportPublicApiContractsReservesChangeReserveTablesRequest() # IikoTransportPublicApiContractsReservesChangeReserveTablesRequest |  (optional)

    try:
        # Change reserve/banquet tables.
        api_response = await api_instance.reserve_change_tables_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_change_reserve_tables_request=iiko_transport_public_api_contracts_reserves_change_reserve_tables_request)
        print("The response of BanquetsReservesApi->reserve_change_tables_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_change_tables_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_change_reserve_tables_request** | [**IikoTransportPublicApiContractsReservesChangeReserveTablesRequest**](IikoTransportPublicApiContractsReservesChangeReserveTablesRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **reserve_create_post**
> IikoTransportPublicApiContractsReservesReserveResponse reserve_create_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_create_reserve_request=iiko_transport_public_api_contracts_reserves_create_reserve_request)

Create banquet/reserve.



 > Allowed from version `7.1.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_create_reserve_request import IikoTransportPublicApiContractsReservesCreateReserveRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_reserve_response import IikoTransportPublicApiContractsReservesReserveResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_create_reserve_request = iikocloud_client.IikoTransportPublicApiContractsReservesCreateReserveRequest() # IikoTransportPublicApiContractsReservesCreateReserveRequest |  (optional)

    try:
        # Create banquet/reserve.
        api_response = await api_instance.reserve_create_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_create_reserve_request=iiko_transport_public_api_contracts_reserves_create_reserve_request)
        print("The response of BanquetsReservesApi->reserve_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_create_reserve_request** | [**IikoTransportPublicApiContractsReservesCreateReserveRequest**](IikoTransportPublicApiContractsReservesCreateReserveRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsReservesReserveResponse**](IikoTransportPublicApiContractsReservesReserveResponse.md)

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

# **reserve_restaurant_sections_workload_post**
> IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse reserve_restaurant_sections_workload_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_request=iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_request)

Returns all banquets/reserves for passed restaurant sections.



 > Allowed from version `7.1.5`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_request import IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_response import IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_request = iikocloud_client.IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadRequest() # IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadRequest |  (optional)

    try:
        # Returns all banquets/reserves for passed restaurant sections.
        api_response = await api_instance.reserve_restaurant_sections_workload_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_request=iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_request)
        print("The response of BanquetsReservesApi->reserve_restaurant_sections_workload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_restaurant_sections_workload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_get_restaurant_sections_workload_request** | [**IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadRequest**](IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse**](IikoTransportPublicApiContractsReservesGetRestaurantSectionsWorkloadResponse.md)

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

# **reserve_status_by_id_post**
> IikoTransportPublicApiContractsReservesReservesResponse reserve_status_by_id_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_reserves_by_id_request=iiko_transport_public_api_contracts_reserves_reserves_by_id_request)

Retrieve banquets/reserves statuses by IDs.



 > Allowed from version `7.1.5`.

 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_reserves_by_id_request import IikoTransportPublicApiContractsReservesReservesByIdRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_reserves_reserves_response import IikoTransportPublicApiContractsReservesReservesResponse
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
    api_instance = iikocloud_client.BanquetsReservesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_reserves_reserves_by_id_request = iikocloud_client.IikoTransportPublicApiContractsReservesReservesByIdRequest() # IikoTransportPublicApiContractsReservesReservesByIdRequest |  (optional)

    try:
        # Retrieve banquets/reserves statuses by IDs.
        api_response = await api_instance.reserve_status_by_id_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_reserves_reserves_by_id_request=iiko_transport_public_api_contracts_reserves_reserves_by_id_request)
        print("The response of BanquetsReservesApi->reserve_status_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BanquetsReservesApi->reserve_status_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_reserves_reserves_by_id_request** | [**IikoTransportPublicApiContractsReservesReservesByIdRequest**](IikoTransportPublicApiContractsReservesReservesByIdRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsReservesReservesResponse**](IikoTransportPublicApiContractsReservesReservesResponse.md)

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

