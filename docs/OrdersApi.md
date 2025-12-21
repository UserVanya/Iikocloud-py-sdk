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
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_add_customer_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request=iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request)

Add customer to order.



 > Allowed from version `7.7.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request import IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request = iikocloud_client.IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest() # IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest |  (optional)

    try:
        # Add customer to order.
        api_response = await api_instance.order_add_customer_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request=iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request)
        print("The response of OrdersApi->order_add_customer_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_add_customer_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_table_orders_request_add_customer_to_table_order_request** | [**IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest**](IikoTransportPublicApiContractsTableOrdersRequestAddCustomerToTableOrderRequest.md)|  | [optional] 

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

# **order_add_items_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_add_items_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request=iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request)

Add order items.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request import IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request = iikocloud_client.IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest() # IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.order_add_items_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request=iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request)
        print("The response of OrdersApi->order_add_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_add_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_table_orders_request_add_items_to_table_order_request** | [**IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest**](IikoTransportPublicApiContractsTableOrdersRequestAddItemsToTableOrderRequest.md)|  | [optional] 

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

# **order_add_payments_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_add_payments_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_orders_common_add_order_payments_request=iiko_transport_public_api_contracts_orders_common_add_order_payments_request)

Add order payments.



 > Allowed from version `8.2.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_orders_common_add_order_payments_request import IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_orders_common_add_order_payments_request = iikocloud_client.IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest() # IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.order_add_payments_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_orders_common_add_order_payments_request=iiko_transport_public_api_contracts_orders_common_add_order_payments_request)
        print("The response of OrdersApi->order_add_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_add_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_orders_common_add_order_payments_request** | [**IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest**](IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest.md)|  | [optional] 

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

# **order_by_id_post**
> IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse order_by_id_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_id_request=iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_id_request)

Retrieve orders by IDs.



 > Allowed from version `7.4.6`.

 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_id_request import IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByIdRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_response_table_orders_response import IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_id_request = iikocloud_client.IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByIdRequest() # IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByIdRequest |  (optional)

    try:
        # Retrieve orders by IDs.
        api_response = await api_instance.order_by_id_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_id_request=iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_id_request)
        print("The response of OrdersApi->order_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_id_request** | [**IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByIdRequest**](IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByIdRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse**](IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse.md)

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

# **order_by_table_post**
> IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse order_by_table_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_table_request=iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_table_request)

Retrieve orders by tables.



 > Allowed from version `7.4.6`.

 > Restriction group: `Orders: receiving`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_table_request import IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByTableRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_response_table_orders_response import IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_table_request = iikocloud_client.IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByTableRequest() # IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByTableRequest |  (optional)

    try:
        # Retrieve orders by tables.
        api_response = await api_instance.order_by_table_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_table_request=iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_table_request)
        print("The response of OrdersApi->order_by_table_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_by_table_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_table_orders_request_get_table_orders_by_table_request** | [**IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByTableRequest**](IikoTransportPublicApiContractsTableOrdersRequestGetTableOrdersByTableRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse**](IikoTransportPublicApiContractsTableOrdersResponseTableOrdersResponse.md)

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

# **order_cancel_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_cancel_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_cancel_table_order_request=iiko_transport_public_api_contracts_deliveries_request_cancel_table_order_request)

Cancel the table order.



 > Allowed from version `9.0.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_cancel_table_order_request import IikoTransportPublicApiContractsDeliveriesRequestCancelTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_cancel_table_order_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestCancelTableOrderRequest() # IikoTransportPublicApiContractsDeliveriesRequestCancelTableOrderRequest |  (optional)

    try:
        # Cancel the table order.
        api_response = await api_instance.order_cancel_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_cancel_table_order_request=iiko_transport_public_api_contracts_deliveries_request_cancel_table_order_request)
        print("The response of OrdersApi->order_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_cancel_table_order_request** | [**IikoTransportPublicApiContractsDeliveriesRequestCancelTableOrderRequest**](IikoTransportPublicApiContractsDeliveriesRequestCancelTableOrderRequest.md)|  | [optional] 

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

# **order_change_external_data_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_change_external_data_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request)

Change table order external_data.



 > Restriction group: `Orders: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest |  (optional)

    try:
        # Change table order external_data.
        api_response = await api_instance.order_change_external_data_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request)
        print("The response of OrdersApi->order_change_external_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_change_external_data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest.md)|  | [optional] 

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

# **order_change_payments_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_change_payments_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request)

Change table order's payments.

> Method will fail if there are any processed payments in the order.
> If all payments in the order are unprocessed they will be removed and replaced with new ones.

 > Allowed from version `7.7.4`.

 > Restriction group: `Order payments: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest |  (optional)

    try:
        # Change table order's payments.
        api_response = await api_instance.order_change_payments_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request)
        print("The response of OrdersApi->order_change_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_change_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest.md)|  | [optional] 

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

# **order_close_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_close_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_close_table_order_request=iiko_transport_public_api_contracts_deliveries_request_close_table_order_request)

Close order.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_close_table_order_request import IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_close_table_order_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest() # IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest |  (optional)

    try:
        # Close order.
        api_response = await api_instance.order_close_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_close_table_order_request=iiko_transport_public_api_contracts_deliveries_request_close_table_order_request)
        print("The response of OrdersApi->order_close_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_close_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_close_table_order_request** | [**IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest**](IikoTransportPublicApiContractsDeliveriesRequestCloseTableOrderRequest.md)|  | [optional] 

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

# **order_create_post**
> IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse order_create_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_create_table_order_request=iiko_transport_public_api_contracts_table_orders_request_create_table_order_request)

Create order.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_create_table_order_request import IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_response_table_order_response import IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_table_orders_request_create_table_order_request = iikocloud_client.IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest() # IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest |  (optional)

    try:
        # Create order.
        api_response = await api_instance.order_create_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_create_table_order_request=iiko_transport_public_api_contracts_table_orders_request_create_table_order_request)
        print("The response of OrdersApi->order_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_table_orders_request_create_table_order_request** | [**IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest**](IikoTransportPublicApiContractsTableOrdersRequestCreateTableOrderRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse**](IikoTransportPublicApiContractsTableOrdersResponseTableOrderResponse.md)

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

# **order_init_by_pos_order_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_init_by_pos_order_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request=iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request)

Init orders, created on POS, by POS orders.



 > Allowed from version `7.7.1`.

 > Restriction group: `Orders: loading data`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request import IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request = iikocloud_client.IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest() # IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest |  (optional)

    try:
        # Init orders, created on POS, by POS orders.
        api_response = await api_instance.order_init_by_pos_order_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request=iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request)
        print("The response of OrdersApi->order_init_by_pos_order_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_init_by_pos_order_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_table_orders_request_init_table_order_by_pos_order_request** | [**IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest**](IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderByPosOrderRequest.md)|  | [optional] 

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

# **order_init_by_table_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_init_by_table_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_init_table_order_request=iiko_transport_public_api_contracts_table_orders_request_init_table_order_request)

Init orders, created on POS, by tables.



 > Allowed from version `7.7.1`.

 > Restriction group: `Orders: loading data`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_table_orders_request_init_table_order_request import IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest
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
    api_instance = iikocloud_client.OrdersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_table_orders_request_init_table_order_request = iikocloud_client.IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest() # IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest |  (optional)

    try:
        # Init orders, created on POS, by tables.
        api_response = await api_instance.order_init_by_table_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_table_orders_request_init_table_order_request=iiko_transport_public_api_contracts_table_orders_request_init_table_order_request)
        print("The response of OrdersApi->order_init_by_table_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->order_init_by_table_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_table_orders_request_init_table_order_request** | [**IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest**](IikoTransportPublicApiContractsTableOrdersRequestInitTableOrderRequest.md)|  | [optional] 

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

