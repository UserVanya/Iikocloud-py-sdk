# iikocloud_client.OrdersApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**order_add_customer_post**](OrdersApi.md#order_add_customer_post) | **POST** /order/add_customer | Add customer to order.
[**order_add_items_post**](OrdersApi.md#order_add_items_post) | **POST** /order/add_items | Add order items.
[**order_add_payments_post**](OrdersApi.md#order_add_payments_post) | **POST** /order/add_payments | Add order payments.
[**order_by_id_post**](OrdersApi.md#order_by_id_post) | **POST** /order/by_id | Retrieve orders by IDs.
[**order_by_table_post**](OrdersApi.md#order_by_table_post) | **POST** /order/by_table | Retrieve orders by tables.
[**order_cancel_post**](OrdersApi.md#order_cancel_post) | **POST** /order/cancel | Cancel the table order.
[**order_change_external_data_post**](OrdersApi.md#order_change_external_data_post) | **POST** /order/change_external_data | Change table order external_data.
[**order_change_payments_post**](OrdersApi.md#order_change_payments_post) | **POST** /order/change_payments | Change table order&#39;s payments.
[**order_close_post**](OrdersApi.md#order_close_post) | **POST** /order/close | Close order.
[**order_create_post**](OrdersApi.md#order_create_post) | **POST** /order/create | Create order.
[**order_init_by_pos_order_post**](OrdersApi.md#order_init_by_pos_order_post) | **POST** /order/init_by_posOrder | Init orders, created on POS, by POS orders.
[**order_init_by_table_post**](OrdersApi.md#order_init_by_table_post) | **POST** /order/init_by_table | Init orders, created on POS, by tables.


# **order_add_customer_post**
> CommonCorrelationIdResponse order_add_customer_post(timeout=timeout, table_orders_request_add_customer_to_table_order_request=table_orders_request_add_customer_to_table_order_request)

Add customer to order.



 > Allowed from version `7.7.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.table_orders_request_add_customer_to_table_order_request import TableOrdersRequestAddCustomerToTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    table_orders_request_add_customer_to_table_order_request = iikocloud_client.TableOrdersRequestAddCustomerToTableOrderRequest() # TableOrdersRequestAddCustomerToTableOrderRequest |  (optional)

    try:
        # Add customer to order.
        api_response = await api_instance.order_add_customer_post(timeout=timeout, table_orders_request_add_customer_to_table_order_request=table_orders_request_add_customer_to_table_order_request)
        print("The response of OrdersApi->order_add_customer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_add_customer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **table_orders_request_add_customer_to_table_order_request** | [**TableOrdersRequestAddCustomerToTableOrderRequest**](TableOrdersRequestAddCustomerToTableOrderRequest.md)|  | [optional] 

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

# **order_add_items_post**
> CommonCorrelationIdResponse order_add_items_post(timeout=timeout, table_orders_request_add_items_to_table_order_request=table_orders_request_add_items_to_table_order_request)

Add order items.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.table_orders_request_add_items_to_table_order_request import TableOrdersRequestAddItemsToTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    table_orders_request_add_items_to_table_order_request = iikocloud_client.TableOrdersRequestAddItemsToTableOrderRequest() # TableOrdersRequestAddItemsToTableOrderRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.order_add_items_post(timeout=timeout, table_orders_request_add_items_to_table_order_request=table_orders_request_add_items_to_table_order_request)
        print("The response of OrdersApi->order_add_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_add_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **table_orders_request_add_items_to_table_order_request** | [**TableOrdersRequestAddItemsToTableOrderRequest**](TableOrdersRequestAddItemsToTableOrderRequest.md)|  | [optional] 

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

# **order_add_payments_post**
> CommonCorrelationIdResponse order_add_payments_post(timeout=timeout, orders_common_add_order_payments_request=orders_common_add_order_payments_request)

Add order payments.



 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.orders_common_add_order_payments_request import OrdersCommonAddOrderPaymentsRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    orders_common_add_order_payments_request = iikocloud_client.OrdersCommonAddOrderPaymentsRequest() # OrdersCommonAddOrderPaymentsRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.order_add_payments_post(timeout=timeout, orders_common_add_order_payments_request=orders_common_add_order_payments_request)
        print("The response of OrdersApi->order_add_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_add_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **orders_common_add_order_payments_request** | [**OrdersCommonAddOrderPaymentsRequest**](OrdersCommonAddOrderPaymentsRequest.md)|  | [optional] 

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

# **order_by_id_post**
> TableOrdersResponseTableOrdersResponse order_by_id_post(timeout=timeout, table_orders_request_get_table_orders_by_id_request=table_orders_request_get_table_orders_by_id_request)

Retrieve orders by IDs.



 > Allowed from version `7.4.6`.

 > Restriction group: `Orders: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.table_orders_request_get_table_orders_by_id_request import TableOrdersRequestGetTableOrdersByIdRequest
from iikocloud_client.models.table_orders_response_table_orders_response import TableOrdersResponseTableOrdersResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    table_orders_request_get_table_orders_by_id_request = iikocloud_client.TableOrdersRequestGetTableOrdersByIdRequest() # TableOrdersRequestGetTableOrdersByIdRequest |  (optional)

    try:
        # Retrieve orders by IDs.
        api_response = await api_instance.order_by_id_post(timeout=timeout, table_orders_request_get_table_orders_by_id_request=table_orders_request_get_table_orders_by_id_request)
        print("The response of OrdersApi->order_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **table_orders_request_get_table_orders_by_id_request** | [**TableOrdersRequestGetTableOrdersByIdRequest**](TableOrdersRequestGetTableOrdersByIdRequest.md)|  | [optional] 

### Return type

[**TableOrdersResponseTableOrdersResponse**](TableOrdersResponseTableOrdersResponse.md)

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

# **order_by_table_post**
> TableOrdersResponseTableOrdersResponse order_by_table_post(timeout=timeout, table_orders_request_get_table_orders_by_table_request=table_orders_request_get_table_orders_by_table_request)

Retrieve orders by tables.



 > Allowed from version `7.4.6`.

 > Restriction group: `Orders: receiving`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.table_orders_request_get_table_orders_by_table_request import TableOrdersRequestGetTableOrdersByTableRequest
from iikocloud_client.models.table_orders_response_table_orders_response import TableOrdersResponseTableOrdersResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    table_orders_request_get_table_orders_by_table_request = iikocloud_client.TableOrdersRequestGetTableOrdersByTableRequest() # TableOrdersRequestGetTableOrdersByTableRequest |  (optional)

    try:
        # Retrieve orders by tables.
        api_response = await api_instance.order_by_table_post(timeout=timeout, table_orders_request_get_table_orders_by_table_request=table_orders_request_get_table_orders_by_table_request)
        print("The response of OrdersApi->order_by_table_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_by_table_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **table_orders_request_get_table_orders_by_table_request** | [**TableOrdersRequestGetTableOrdersByTableRequest**](TableOrdersRequestGetTableOrdersByTableRequest.md)|  | [optional] 

### Return type

[**TableOrdersResponseTableOrdersResponse**](TableOrdersResponseTableOrdersResponse.md)

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

# **order_cancel_post**
> CommonCorrelationIdResponse order_cancel_post(timeout=timeout, deliveries_request_cancel_table_order_request=deliveries_request_cancel_table_order_request)

Cancel the table order.



 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.deliveries_request_cancel_table_order_request import DeliveriesRequestCancelTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    deliveries_request_cancel_table_order_request = iikocloud_client.DeliveriesRequestCancelTableOrderRequest() # DeliveriesRequestCancelTableOrderRequest |  (optional)

    try:
        # Cancel the table order.
        api_response = await api_instance.order_cancel_post(timeout=timeout, deliveries_request_cancel_table_order_request=deliveries_request_cancel_table_order_request)
        print("The response of OrdersApi->order_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **deliveries_request_cancel_table_order_request** | [**DeliveriesRequestCancelTableOrderRequest**](DeliveriesRequestCancelTableOrderRequest.md)|  | [optional] 

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

# **order_change_external_data_post**
> CommonCorrelationIdResponse order_change_external_data_post(timeout=timeout, deliveries_request_update_order_change_external_data_request=deliveries_request_update_order_change_external_data_request)

Change table order external_data.



 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.deliveries_request_update_order_change_external_data_request import DeliveriesRequestUpdateOrderChangeExternalDataRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    deliveries_request_update_order_change_external_data_request = iikocloud_client.DeliveriesRequestUpdateOrderChangeExternalDataRequest() # DeliveriesRequestUpdateOrderChangeExternalDataRequest |  (optional)

    try:
        # Change table order external_data.
        api_response = await api_instance.order_change_external_data_post(timeout=timeout, deliveries_request_update_order_change_external_data_request=deliveries_request_update_order_change_external_data_request)
        print("The response of OrdersApi->order_change_external_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_change_external_data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **deliveries_request_update_order_change_external_data_request** | [**DeliveriesRequestUpdateOrderChangeExternalDataRequest**](DeliveriesRequestUpdateOrderChangeExternalDataRequest.md)|  | [optional] 

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

# **order_change_payments_post**
> CommonCorrelationIdResponse order_change_payments_post(timeout=timeout, deliveries_request_update_order_change_payments_request=deliveries_request_update_order_change_payments_request)

Change table order's payments.

> Method will fail if there are any processed payments in the order.
> If all payments in the order are unprocessed they will be removed and replaced with new ones.

 > Allowed from version `7.7.4`.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.deliveries_request_update_order_change_payments_request import DeliveriesRequestUpdateOrderChangePaymentsRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    deliveries_request_update_order_change_payments_request = iikocloud_client.DeliveriesRequestUpdateOrderChangePaymentsRequest() # DeliveriesRequestUpdateOrderChangePaymentsRequest |  (optional)

    try:
        # Change table order's payments.
        api_response = await api_instance.order_change_payments_post(timeout=timeout, deliveries_request_update_order_change_payments_request=deliveries_request_update_order_change_payments_request)
        print("The response of OrdersApi->order_change_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_change_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **deliveries_request_update_order_change_payments_request** | [**DeliveriesRequestUpdateOrderChangePaymentsRequest**](DeliveriesRequestUpdateOrderChangePaymentsRequest.md)|  | [optional] 

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

# **order_close_post**
> CommonCorrelationIdResponse order_close_post(timeout=timeout, deliveries_request_close_table_order_request=deliveries_request_close_table_order_request)

Close order.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.deliveries_request_close_table_order_request import DeliveriesRequestCloseTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    deliveries_request_close_table_order_request = iikocloud_client.DeliveriesRequestCloseTableOrderRequest() # DeliveriesRequestCloseTableOrderRequest |  (optional)

    try:
        # Close order.
        api_response = await api_instance.order_close_post(timeout=timeout, deliveries_request_close_table_order_request=deliveries_request_close_table_order_request)
        print("The response of OrdersApi->order_close_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_close_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **deliveries_request_close_table_order_request** | [**DeliveriesRequestCloseTableOrderRequest**](DeliveriesRequestCloseTableOrderRequest.md)|  | [optional] 

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

# **order_create_post**
> TableOrdersResponseTableOrderResponse order_create_post(timeout=timeout, table_orders_request_create_table_order_request=table_orders_request_create_table_order_request)

Create order.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.table_orders_request_create_table_order_request import TableOrdersRequestCreateTableOrderRequest
from iikocloud_client.models.table_orders_response_table_order_response import TableOrdersResponseTableOrderResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    table_orders_request_create_table_order_request = iikocloud_client.TableOrdersRequestCreateTableOrderRequest() # TableOrdersRequestCreateTableOrderRequest |  (optional)

    try:
        # Create order.
        api_response = await api_instance.order_create_post(timeout=timeout, table_orders_request_create_table_order_request=table_orders_request_create_table_order_request)
        print("The response of OrdersApi->order_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **table_orders_request_create_table_order_request** | [**TableOrdersRequestCreateTableOrderRequest**](TableOrdersRequestCreateTableOrderRequest.md)|  | [optional] 

### Return type

[**TableOrdersResponseTableOrderResponse**](TableOrdersResponseTableOrderResponse.md)

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

# **order_init_by_pos_order_post**
> CommonCorrelationIdResponse order_init_by_pos_order_post(timeout=timeout, table_orders_request_init_table_order_by_pos_order_request=table_orders_request_init_table_order_by_pos_order_request)

Init orders, created on POS, by POS orders.



 > Allowed from version `7.7.1`.

 > Restriction group: `Orders: loading data`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.table_orders_request_init_table_order_by_pos_order_request import TableOrdersRequestInitTableOrderByPosOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    table_orders_request_init_table_order_by_pos_order_request = iikocloud_client.TableOrdersRequestInitTableOrderByPosOrderRequest() # TableOrdersRequestInitTableOrderByPosOrderRequest |  (optional)

    try:
        # Init orders, created on POS, by POS orders.
        api_response = await api_instance.order_init_by_pos_order_post(timeout=timeout, table_orders_request_init_table_order_by_pos_order_request=table_orders_request_init_table_order_by_pos_order_request)
        print("The response of OrdersApi->order_init_by_pos_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_init_by_pos_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **table_orders_request_init_table_order_by_pos_order_request** | [**TableOrdersRequestInitTableOrderByPosOrderRequest**](TableOrdersRequestInitTableOrderByPosOrderRequest.md)|  | [optional] 

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

# **order_init_by_table_post**
> CommonCorrelationIdResponse order_init_by_table_post(timeout=timeout, table_orders_request_init_table_order_request=table_orders_request_init_table_order_request)

Init orders, created on POS, by tables.



 > Allowed from version `7.7.1`.

 > Restriction group: `Orders: loading data`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_correlation_id_response import CommonCorrelationIdResponse
from iikocloud_client.models.table_orders_request_init_table_order_request import TableOrdersRequestInitTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    table_orders_request_init_table_order_request = iikocloud_client.TableOrdersRequestInitTableOrderRequest() # TableOrdersRequestInitTableOrderRequest |  (optional)

    try:
        # Init orders, created on POS, by tables.
        api_response = await api_instance.order_init_by_table_post(timeout=timeout, table_orders_request_init_table_order_request=table_orders_request_init_table_order_request)
        print("The response of OrdersApi->order_init_by_table_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_init_by_table_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **table_orders_request_init_table_order_request** | [**TableOrdersRequestInitTableOrderRequest**](TableOrdersRequestInitTableOrderRequest.md)|  | [optional] 

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

