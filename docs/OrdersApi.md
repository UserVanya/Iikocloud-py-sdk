# iikocloud_client.OrdersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_order_add_customer_post**](OrdersApi.md#api1_order_add_customer_post) | **POST** /api/1/order/add_customer | Add customer to order.
[**api1_order_add_items_post**](OrdersApi.md#api1_order_add_items_post) | **POST** /api/1/order/add_items | Add order items.
[**api1_order_add_payments_post**](OrdersApi.md#api1_order_add_payments_post) | **POST** /api/1/order/add_payments | Add order payments.
[**api1_order_by_id_post**](OrdersApi.md#api1_order_by_id_post) | **POST** /api/1/order/by_id | Retrieve orders by IDs.
[**api1_order_by_table_post**](OrdersApi.md#api1_order_by_table_post) | **POST** /api/1/order/by_table | Retrieve orders by tables.
[**api1_order_change_external_data_post**](OrdersApi.md#api1_order_change_external_data_post) | **POST** /api/1/order/change_external_data | Change table order external_data.
[**api1_order_change_payments_post**](OrdersApi.md#api1_order_change_payments_post) | **POST** /api/1/order/change_payments | Change table order&#39;s payments.
[**api1_order_close_post**](OrdersApi.md#api1_order_close_post) | **POST** /api/1/order/close | Close order.
[**api1_order_create_post**](OrdersApi.md#api1_order_create_post) | **POST** /api/1/order/create | Create order.
[**api1_order_init_by_pos_order_post**](OrdersApi.md#api1_order_init_by_pos_order_post) | **POST** /api/1/order/init_by_posOrder | Init orders, created on POS, by POS orders.
[**api1_order_init_by_table_post**](OrdersApi.md#api1_order_init_by_table_post) | **POST** /api/1/order/init_by_table | Init orders, created on POS, by tables.


# **api1_order_add_customer_post**
> TransportCommonCorrelationIdResponse api1_order_add_customer_post(authorization, timeout=timeout, transport_table_orders_request_add_customer_to_table_order_request=transport_table_orders_request_add_customer_to_table_order_request)

Add customer to order.



 > Allowed from version `7.7.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_table_orders_request_add_customer_to_table_order_request import TransportTableOrdersRequestAddCustomerToTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_table_orders_request_add_customer_to_table_order_request = iikocloud_client.TransportTableOrdersRequestAddCustomerToTableOrderRequest() # TransportTableOrdersRequestAddCustomerToTableOrderRequest |  (optional)

    try:
        # Add customer to order.
        api_response = await api_instance.api1_order_add_customer_post(authorization, timeout=timeout, transport_table_orders_request_add_customer_to_table_order_request=transport_table_orders_request_add_customer_to_table_order_request)
        print("The response of OrdersApi->api1_order_add_customer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_add_customer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_table_orders_request_add_customer_to_table_order_request** | [**TransportTableOrdersRequestAddCustomerToTableOrderRequest**](TransportTableOrdersRequestAddCustomerToTableOrderRequest.md)|  | [optional] 

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

# **api1_order_add_items_post**
> TransportCommonCorrelationIdResponse api1_order_add_items_post(authorization, timeout=timeout, transport_table_orders_request_add_items_to_table_order_request=transport_table_orders_request_add_items_to_table_order_request)

Add order items.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_table_orders_request_add_items_to_table_order_request import TransportTableOrdersRequestAddItemsToTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_table_orders_request_add_items_to_table_order_request = iikocloud_client.TransportTableOrdersRequestAddItemsToTableOrderRequest() # TransportTableOrdersRequestAddItemsToTableOrderRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.api1_order_add_items_post(authorization, timeout=timeout, transport_table_orders_request_add_items_to_table_order_request=transport_table_orders_request_add_items_to_table_order_request)
        print("The response of OrdersApi->api1_order_add_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_add_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_table_orders_request_add_items_to_table_order_request** | [**TransportTableOrdersRequestAddItemsToTableOrderRequest**](TransportTableOrdersRequestAddItemsToTableOrderRequest.md)|  | [optional] 

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

# **api1_order_add_payments_post**
> TransportCommonCorrelationIdResponse api1_order_add_payments_post(authorization, timeout=timeout, transport_orders_common_add_order_payments_request=transport_orders_common_add_order_payments_request)

Add order payments.



 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_orders_common_add_order_payments_request import TransportOrdersCommonAddOrderPaymentsRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_orders_common_add_order_payments_request = iikocloud_client.TransportOrdersCommonAddOrderPaymentsRequest() # TransportOrdersCommonAddOrderPaymentsRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.api1_order_add_payments_post(authorization, timeout=timeout, transport_orders_common_add_order_payments_request=transport_orders_common_add_order_payments_request)
        print("The response of OrdersApi->api1_order_add_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_add_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_orders_common_add_order_payments_request** | [**TransportOrdersCommonAddOrderPaymentsRequest**](TransportOrdersCommonAddOrderPaymentsRequest.md)|  | [optional] 

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

# **api1_order_by_id_post**
> TransportTableOrdersResponseTableOrdersResponse api1_order_by_id_post(authorization, timeout=timeout, transport_table_orders_request_get_table_orders_by_id_request=transport_table_orders_request_get_table_orders_by_id_request)

Retrieve orders by IDs.



 > Allowed from version `7.4.6`.

 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_table_orders_request_get_table_orders_by_id_request import TransportTableOrdersRequestGetTableOrdersByIdRequest
from iikocloud_client.models.transport_table_orders_response_table_orders_response import TransportTableOrdersResponseTableOrdersResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_table_orders_request_get_table_orders_by_id_request = iikocloud_client.TransportTableOrdersRequestGetTableOrdersByIdRequest() # TransportTableOrdersRequestGetTableOrdersByIdRequest |  (optional)

    try:
        # Retrieve orders by IDs.
        api_response = await api_instance.api1_order_by_id_post(authorization, timeout=timeout, transport_table_orders_request_get_table_orders_by_id_request=transport_table_orders_request_get_table_orders_by_id_request)
        print("The response of OrdersApi->api1_order_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_table_orders_request_get_table_orders_by_id_request** | [**TransportTableOrdersRequestGetTableOrdersByIdRequest**](TransportTableOrdersRequestGetTableOrdersByIdRequest.md)|  | [optional] 

### Return type

[**TransportTableOrdersResponseTableOrdersResponse**](TransportTableOrdersResponseTableOrdersResponse.md)

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

# **api1_order_by_table_post**
> TransportTableOrdersResponseTableOrdersResponse api1_order_by_table_post(authorization, timeout=timeout, transport_table_orders_request_get_table_orders_by_table_request=transport_table_orders_request_get_table_orders_by_table_request)

Retrieve orders by tables.



 > Allowed from version `7.4.6`.

 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_table_orders_request_get_table_orders_by_table_request import TransportTableOrdersRequestGetTableOrdersByTableRequest
from iikocloud_client.models.transport_table_orders_response_table_orders_response import TransportTableOrdersResponseTableOrdersResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_table_orders_request_get_table_orders_by_table_request = iikocloud_client.TransportTableOrdersRequestGetTableOrdersByTableRequest() # TransportTableOrdersRequestGetTableOrdersByTableRequest |  (optional)

    try:
        # Retrieve orders by tables.
        api_response = await api_instance.api1_order_by_table_post(authorization, timeout=timeout, transport_table_orders_request_get_table_orders_by_table_request=transport_table_orders_request_get_table_orders_by_table_request)
        print("The response of OrdersApi->api1_order_by_table_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_by_table_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_table_orders_request_get_table_orders_by_table_request** | [**TransportTableOrdersRequestGetTableOrdersByTableRequest**](TransportTableOrdersRequestGetTableOrdersByTableRequest.md)|  | [optional] 

### Return type

[**TransportTableOrdersResponseTableOrdersResponse**](TransportTableOrdersResponseTableOrdersResponse.md)

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

# **api1_order_change_external_data_post**
> TransportCommonCorrelationIdResponse api1_order_change_external_data_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_external_data_request=transport_deliveries_request_update_order_change_external_data_request)

Change table order external_data.



 > Restriction group: `Orders: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_deliveries_request_update_order_change_external_data_request import TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_change_external_data_request = iikocloud_client.TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest() # TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest |  (optional)

    try:
        # Change table order external_data.
        api_response = await api_instance.api1_order_change_external_data_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_external_data_request=transport_deliveries_request_update_order_change_external_data_request)
        print("The response of OrdersApi->api1_order_change_external_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_change_external_data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_change_external_data_request** | [**TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest**](TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest.md)|  | [optional] 

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

# **api1_order_change_payments_post**
> TransportCommonCorrelationIdResponse api1_order_change_payments_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_payments_request=transport_deliveries_request_update_order_change_payments_request)

Change table order's payments.

> Method will fail if there are any processed payments in the order.
> If all payments in the order are unprocessed they will be removed and replaced with new ones.

 > Allowed from version `7.7.4`.

 > Restriction group: `Order payments: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_deliveries_request_update_order_change_payments_request import TransportDeliveriesRequestUpdateOrderChangePaymentsRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_change_payments_request = iikocloud_client.TransportDeliveriesRequestUpdateOrderChangePaymentsRequest() # TransportDeliveriesRequestUpdateOrderChangePaymentsRequest |  (optional)

    try:
        # Change table order's payments.
        api_response = await api_instance.api1_order_change_payments_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_payments_request=transport_deliveries_request_update_order_change_payments_request)
        print("The response of OrdersApi->api1_order_change_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_change_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_change_payments_request** | [**TransportDeliveriesRequestUpdateOrderChangePaymentsRequest**](TransportDeliveriesRequestUpdateOrderChangePaymentsRequest.md)|  | [optional] 

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

# **api1_order_close_post**
> TransportCommonCorrelationIdResponse api1_order_close_post(authorization, timeout=timeout, transport_deliveries_request_close_table_order_request=transport_deliveries_request_close_table_order_request)

Close order.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_deliveries_request_close_table_order_request import TransportDeliveriesRequestCloseTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_close_table_order_request = iikocloud_client.TransportDeliveriesRequestCloseTableOrderRequest() # TransportDeliveriesRequestCloseTableOrderRequest |  (optional)

    try:
        # Close order.
        api_response = await api_instance.api1_order_close_post(authorization, timeout=timeout, transport_deliveries_request_close_table_order_request=transport_deliveries_request_close_table_order_request)
        print("The response of OrdersApi->api1_order_close_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_close_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_close_table_order_request** | [**TransportDeliveriesRequestCloseTableOrderRequest**](TransportDeliveriesRequestCloseTableOrderRequest.md)|  | [optional] 

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

# **api1_order_create_post**
> TransportTableOrdersResponseTableOrderResponse api1_order_create_post(authorization, timeout=timeout, transport_table_orders_request_create_table_order_request=transport_table_orders_request_create_table_order_request)

Create order.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_table_orders_request_create_table_order_request import TransportTableOrdersRequestCreateTableOrderRequest
from iikocloud_client.models.transport_table_orders_response_table_order_response import TransportTableOrdersResponseTableOrderResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_table_orders_request_create_table_order_request = iikocloud_client.TransportTableOrdersRequestCreateTableOrderRequest() # TransportTableOrdersRequestCreateTableOrderRequest |  (optional)

    try:
        # Create order.
        api_response = await api_instance.api1_order_create_post(authorization, timeout=timeout, transport_table_orders_request_create_table_order_request=transport_table_orders_request_create_table_order_request)
        print("The response of OrdersApi->api1_order_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_table_orders_request_create_table_order_request** | [**TransportTableOrdersRequestCreateTableOrderRequest**](TransportTableOrdersRequestCreateTableOrderRequest.md)|  | [optional] 

### Return type

[**TransportTableOrdersResponseTableOrderResponse**](TransportTableOrdersResponseTableOrderResponse.md)

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

# **api1_order_init_by_pos_order_post**
> TransportCommonCorrelationIdResponse api1_order_init_by_pos_order_post(authorization, timeout=timeout, transport_table_orders_request_init_table_order_by_pos_order_request=transport_table_orders_request_init_table_order_by_pos_order_request)

Init orders, created on POS, by POS orders.



 > Allowed from version `7.7.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: loading data`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_table_orders_request_init_table_order_by_pos_order_request import TransportTableOrdersRequestInitTableOrderByPosOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_table_orders_request_init_table_order_by_pos_order_request = iikocloud_client.TransportTableOrdersRequestInitTableOrderByPosOrderRequest() # TransportTableOrdersRequestInitTableOrderByPosOrderRequest |  (optional)

    try:
        # Init orders, created on POS, by POS orders.
        api_response = await api_instance.api1_order_init_by_pos_order_post(authorization, timeout=timeout, transport_table_orders_request_init_table_order_by_pos_order_request=transport_table_orders_request_init_table_order_by_pos_order_request)
        print("The response of OrdersApi->api1_order_init_by_pos_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_init_by_pos_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_table_orders_request_init_table_order_by_pos_order_request** | [**TransportTableOrdersRequestInitTableOrderByPosOrderRequest**](TransportTableOrdersRequestInitTableOrderByPosOrderRequest.md)|  | [optional] 

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

# **api1_order_init_by_table_post**
> TransportCommonCorrelationIdResponse api1_order_init_by_table_post(authorization, timeout=timeout, transport_table_orders_request_init_table_order_request=transport_table_orders_request_init_table_order_request)

Init orders, created on POS, by tables.



 > Allowed from version `7.7.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: loading data`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_table_orders_request_init_table_order_request import TransportTableOrdersRequestInitTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_table_orders_request_init_table_order_request = iikocloud_client.TransportTableOrdersRequestInitTableOrderRequest() # TransportTableOrdersRequestInitTableOrderRequest |  (optional)

    try:
        # Init orders, created on POS, by tables.
        api_response = await api_instance.api1_order_init_by_table_post(authorization, timeout=timeout, transport_table_orders_request_init_table_order_request=transport_table_orders_request_init_table_order_request)
        print("The response of OrdersApi->api1_order_init_by_table_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->api1_order_init_by_table_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_table_orders_request_init_table_order_request** | [**TransportTableOrdersRequestInitTableOrderRequest**](TransportTableOrdersRequestInitTableOrderRequest.md)|  | [optional] 

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

