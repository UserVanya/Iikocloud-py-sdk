# iikocloud_client.OrdersApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_to_table_order**](OrdersApi.md#add_customer_to_table_order) | **POST** /api/1/order/add_customer | Add customer to order.
[**add_items_to_table_order**](OrdersApi.md#add_items_to_table_order) | **POST** /api/1/order/add_items | Add order items.
[**add_table_order_payments**](OrdersApi.md#add_table_order_payments) | **POST** /api/1/order/add_payments | Add order payments.
[**cancel_table_order**](OrdersApi.md#cancel_table_order) | **POST** /api/1/order/cancel | Cancel the table order.
[**change_table_order_external_data**](OrdersApi.md#change_table_order_external_data) | **POST** /api/1/order/change_external_data | Change table order external_data.
[**change_table_order_payments**](OrdersApi.md#change_table_order_payments) | **POST** /api/1/order/change_payments | Change table order&#39;s payments.
[**close_table_order**](OrdersApi.md#close_table_order) | **POST** /api/1/order/close | Close order.
[**create_table_order**](OrdersApi.md#create_table_order) | **POST** /api/1/order/create | Create order.
[**get_table_orders_by_id**](OrdersApi.md#get_table_orders_by_id) | **POST** /api/1/order/by_id | Retrieve orders by IDs.
[**get_table_orders_by_table**](OrdersApi.md#get_table_orders_by_table) | **POST** /api/1/order/by_table | Retrieve orders by tables.
[**initialize_table_orders_by_pos_orders**](OrdersApi.md#initialize_table_orders_by_pos_orders) | **POST** /api/1/order/init_by_posOrder | Init orders, created on POS, by POS orders.
[**initialize_table_orders_by_tables**](OrdersApi.md#initialize_table_orders_by_tables) | **POST** /api/1/order/init_by_table | Init orders, created on POS, by tables.


# **add_customer_to_table_order**
> CorrelationIdResponse add_customer_to_table_order(timeout=timeout, add_customer_to_table_order_request=add_customer_to_table_order_request)

Add customer to order.



 > Allowed from version `7.7.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_customer_to_table_order_request import AddCustomerToTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_customer_to_table_order_request = iikocloud_client.AddCustomerToTableOrderRequest() # AddCustomerToTableOrderRequest |  (optional)

    try:
        # Add customer to order.
        api_response = await api_instance.add_customer_to_table_order(timeout=timeout, add_customer_to_table_order_request=add_customer_to_table_order_request)
        print("The response of OrdersApi->add_customer_to_table_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->add_customer_to_table_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_customer_to_table_order_request** | [**AddCustomerToTableOrderRequest**](AddCustomerToTableOrderRequest.md)|  | [optional] 

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

# **add_items_to_table_order**
> CorrelationIdResponse add_items_to_table_order(timeout=timeout, add_items_to_table_order_request=add_items_to_table_order_request)

Add order items.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_items_to_table_order_request import AddItemsToTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_items_to_table_order_request = iikocloud_client.AddItemsToTableOrderRequest() # AddItemsToTableOrderRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.add_items_to_table_order(timeout=timeout, add_items_to_table_order_request=add_items_to_table_order_request)
        print("The response of OrdersApi->add_items_to_table_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->add_items_to_table_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_items_to_table_order_request** | [**AddItemsToTableOrderRequest**](AddItemsToTableOrderRequest.md)|  | [optional] 

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

# **add_table_order_payments**
> CorrelationIdResponse add_table_order_payments(timeout=timeout, add_order_payments_request=add_order_payments_request)

Add order payments.



 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.add_order_payments_request import AddOrderPaymentsRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    add_order_payments_request = iikocloud_client.AddOrderPaymentsRequest() # AddOrderPaymentsRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.add_table_order_payments(timeout=timeout, add_order_payments_request=add_order_payments_request)
        print("The response of OrdersApi->add_table_order_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->add_table_order_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **add_order_payments_request** | [**AddOrderPaymentsRequest**](AddOrderPaymentsRequest.md)|  | [optional] 

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

# **cancel_table_order**
> CorrelationIdResponse cancel_table_order(timeout=timeout, cancel_table_order_request=cancel_table_order_request)

Cancel the table order.



 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cancel_table_order_request import CancelTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    cancel_table_order_request = iikocloud_client.CancelTableOrderRequest() # CancelTableOrderRequest |  (optional)

    try:
        # Cancel the table order.
        api_response = await api_instance.cancel_table_order(timeout=timeout, cancel_table_order_request=cancel_table_order_request)
        print("The response of OrdersApi->cancel_table_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->cancel_table_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **cancel_table_order_request** | [**CancelTableOrderRequest**](CancelTableOrderRequest.md)|  | [optional] 

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

# **change_table_order_external_data**
> CorrelationIdResponse change_table_order_external_data(timeout=timeout, change_external_data_request=change_external_data_request)

Change table order external_data.



 > Restriction group: `Orders: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_external_data_request import ChangeExternalDataRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_external_data_request = iikocloud_client.ChangeExternalDataRequest() # ChangeExternalDataRequest |  (optional)

    try:
        # Change table order external_data.
        api_response = await api_instance.change_table_order_external_data(timeout=timeout, change_external_data_request=change_external_data_request)
        print("The response of OrdersApi->change_table_order_external_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->change_table_order_external_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_external_data_request** | [**ChangeExternalDataRequest**](ChangeExternalDataRequest.md)|  | [optional] 

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

# **change_table_order_payments**
> CorrelationIdResponse change_table_order_payments(timeout=timeout, change_payments_request=change_payments_request)

Change table order's payments.

> Method will fail if there are any processed payments in the order.
> If all payments in the order are unprocessed they will be removed and replaced with new ones.

 > Allowed from version `7.7.4`.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_payments_request import ChangePaymentsRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_payments_request = iikocloud_client.ChangePaymentsRequest() # ChangePaymentsRequest |  (optional)

    try:
        # Change table order's payments.
        api_response = await api_instance.change_table_order_payments(timeout=timeout, change_payments_request=change_payments_request)
        print("The response of OrdersApi->change_table_order_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->change_table_order_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_payments_request** | [**ChangePaymentsRequest**](ChangePaymentsRequest.md)|  | [optional] 

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

# **close_table_order**
> CorrelationIdResponse close_table_order(timeout=timeout, close_table_order_request=close_table_order_request)

Close order.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.close_table_order_request import CloseTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    close_table_order_request = iikocloud_client.CloseTableOrderRequest() # CloseTableOrderRequest |  (optional)

    try:
        # Close order.
        api_response = await api_instance.close_table_order(timeout=timeout, close_table_order_request=close_table_order_request)
        print("The response of OrdersApi->close_table_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->close_table_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **close_table_order_request** | [**CloseTableOrderRequest**](CloseTableOrderRequest.md)|  | [optional] 

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

# **create_table_order**
> TableOrderResponse create_table_order(timeout=timeout, create_table_order_request=create_table_order_request)

Create order.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.create_table_order_request import CreateTableOrderRequest
from iikocloud_client.models.table_order_response import TableOrderResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    create_table_order_request = iikocloud_client.CreateTableOrderRequest() # CreateTableOrderRequest |  (optional)

    try:
        # Create order.
        api_response = await api_instance.create_table_order(timeout=timeout, create_table_order_request=create_table_order_request)
        print("The response of OrdersApi->create_table_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_table_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **create_table_order_request** | [**CreateTableOrderRequest**](CreateTableOrderRequest.md)|  | [optional] 

### Return type

[**TableOrderResponse**](TableOrderResponse.md)

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

# **get_table_orders_by_id**
> TableOrdersResponse get_table_orders_by_id(timeout=timeout, get_table_orders_by_id_request=get_table_orders_by_id_request)

Retrieve orders by IDs.



 > Allowed from version `7.4.6`.

 > Restriction group: `Orders: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_table_orders_by_id_request import GetTableOrdersByIdRequest
from iikocloud_client.models.table_orders_response import TableOrdersResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_table_orders_by_id_request = iikocloud_client.GetTableOrdersByIdRequest() # GetTableOrdersByIdRequest |  (optional)

    try:
        # Retrieve orders by IDs.
        api_response = await api_instance.get_table_orders_by_id(timeout=timeout, get_table_orders_by_id_request=get_table_orders_by_id_request)
        print("The response of OrdersApi->get_table_orders_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_table_orders_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_table_orders_by_id_request** | [**GetTableOrdersByIdRequest**](GetTableOrdersByIdRequest.md)|  | [optional] 

### Return type

[**TableOrdersResponse**](TableOrdersResponse.md)

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

# **get_table_orders_by_table**
> TableOrdersResponse get_table_orders_by_table(timeout=timeout, get_table_orders_by_table_request=get_table_orders_by_table_request)

Retrieve orders by tables.



 > Allowed from version `7.4.6`.

 > Restriction group: `Orders: receiving`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_table_orders_by_table_request import GetTableOrdersByTableRequest
from iikocloud_client.models.table_orders_response import TableOrdersResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_table_orders_by_table_request = iikocloud_client.GetTableOrdersByTableRequest() # GetTableOrdersByTableRequest |  (optional)

    try:
        # Retrieve orders by tables.
        api_response = await api_instance.get_table_orders_by_table(timeout=timeout, get_table_orders_by_table_request=get_table_orders_by_table_request)
        print("The response of OrdersApi->get_table_orders_by_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_table_orders_by_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_table_orders_by_table_request** | [**GetTableOrdersByTableRequest**](GetTableOrdersByTableRequest.md)|  | [optional] 

### Return type

[**TableOrdersResponse**](TableOrdersResponse.md)

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

# **initialize_table_orders_by_pos_orders**
> CorrelationIdResponse initialize_table_orders_by_pos_orders(timeout=timeout, init_table_order_by_pos_order_request=init_table_order_by_pos_order_request)

Init orders, created on POS, by POS orders.



 > Allowed from version `7.7.1`.

 > Restriction group: `Orders: loading data`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.init_table_order_by_pos_order_request import InitTableOrderByPosOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    init_table_order_by_pos_order_request = iikocloud_client.InitTableOrderByPosOrderRequest() # InitTableOrderByPosOrderRequest |  (optional)

    try:
        # Init orders, created on POS, by POS orders.
        api_response = await api_instance.initialize_table_orders_by_pos_orders(timeout=timeout, init_table_order_by_pos_order_request=init_table_order_by_pos_order_request)
        print("The response of OrdersApi->initialize_table_orders_by_pos_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->initialize_table_orders_by_pos_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **init_table_order_by_pos_order_request** | [**InitTableOrderByPosOrderRequest**](InitTableOrderByPosOrderRequest.md)|  | [optional] 

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

# **initialize_table_orders_by_tables**
> CorrelationIdResponse initialize_table_orders_by_tables(timeout=timeout, init_table_order_request=init_table_order_request)

Init orders, created on POS, by tables.



 > Allowed from version `7.7.1`.

 > Restriction group: `Orders: loading data`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.init_table_order_request import InitTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    init_table_order_request = iikocloud_client.InitTableOrderRequest() # InitTableOrderRequest |  (optional)

    try:
        # Init orders, created on POS, by tables.
        api_response = await api_instance.initialize_table_orders_by_tables(timeout=timeout, init_table_order_request=init_table_order_request)
        print("The response of OrdersApi->initialize_table_orders_by_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->initialize_table_orders_by_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **init_table_order_request** | [**InitTableOrderRequest**](InitTableOrderRequest.md)|  | [optional] 

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

