# iiko_cloud_client.DeliveriesCreateAndUpdateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_deliveries_add_items_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_add_items_post) | **POST** /api/1/deliveries/add_items | Add order items.
[**api1_deliveries_add_payments_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_add_payments_post) | **POST** /api/1/deliveries/add_payments | Add order payments.
[**api1_deliveries_cancel_confirmation_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_cancel_confirmation_post) | **POST** /api/1/deliveries/cancel_confirmation | Cancel delivery confirmation.
[**api1_deliveries_cancel_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_cancel_post) | **POST** /api/1/deliveries/cancel | Cancel delivery order.
[**api1_deliveries_change_comment_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_change_comment_post) | **POST** /api/1/deliveries/change_comment | Change delivery comment.
[**api1_deliveries_change_complete_before_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_change_complete_before_post) | **POST** /api/1/deliveries/change_complete_before | Change time when client wants the order to be delivered.
[**api1_deliveries_change_delivery_point_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_change_delivery_point_post) | **POST** /api/1/deliveries/change_delivery_point | Change order&#39;s delivery point information.
[**api1_deliveries_change_driver_info_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_change_driver_info_post) | **POST** /api/1/deliveries/change_driver_info | Change driver info.
[**api1_deliveries_change_external_data_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_change_external_data_post) | **POST** /api/1/deliveries/change_external_data | Change delivery external data.
[**api1_deliveries_change_operator_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_change_operator_post) | **POST** /api/1/deliveries/change_operator | Assign/change the order operator.
[**api1_deliveries_change_payments_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_change_payments_post) | **POST** /api/1/deliveries/change_payments | Change order&#39;s payments.
[**api1_deliveries_change_service_type_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_change_service_type_post) | **POST** /api/1/deliveries/change_service_type | Change order&#39;s delivery type.
[**api1_deliveries_close_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_close_post) | **POST** /api/1/deliveries/close | Close order.
[**api1_deliveries_confirm_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_confirm_post) | **POST** /api/1/deliveries/confirm | Confirm delivery.
[**api1_deliveries_create_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_create_post) | **POST** /api/1/deliveries/create | Create delivery.
[**api1_deliveries_print_delivery_bill_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_print_delivery_bill_post) | **POST** /api/1/deliveries/print_delivery_bill | Print delivery bill.
[**api1_deliveries_update_order_courier_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_update_order_courier_post) | **POST** /api/1/deliveries/update_order_courier | Update order courier.
[**api1_deliveries_update_order_delivery_status_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_update_order_delivery_status_post) | **POST** /api/1/deliveries/update_order_delivery_status | Update delivery status.
[**api1_deliveries_update_order_payments_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_update_order_payments_post) | **POST** /api/1/deliveries/update_order_payments | Update order payment details.
[**api1_deliveries_update_order_problem_post**](DeliveriesCreateAndUpdateApi.md#api1_deliveries_update_order_problem_post) | **POST** /api/1/deliveries/update_order_problem | Update order problem.


# **api1_deliveries_add_items_post**
> TransportCommonCorrelationIdResponse api1_deliveries_add_items_post(authorization, timeout=timeout, transport_deliveries_request_add_order_items_request=transport_deliveries_request_add_order_items_request)

Add order items.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_add_order_items_request import TransportDeliveriesRequestAddOrderItemsRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_add_order_items_request = iiko_cloud_client.TransportDeliveriesRequestAddOrderItemsRequest() # TransportDeliveriesRequestAddOrderItemsRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.api1_deliveries_add_items_post(authorization, timeout=timeout, transport_deliveries_request_add_order_items_request=transport_deliveries_request_add_order_items_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_add_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_add_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_add_order_items_request** | [**TransportDeliveriesRequestAddOrderItemsRequest**](TransportDeliveriesRequestAddOrderItemsRequest.md)|  | [optional] 

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

# **api1_deliveries_add_payments_post**
> TransportCommonCorrelationIdResponse api1_deliveries_add_payments_post(authorization, timeout=timeout, transport_orders_common_add_order_payments_request=transport_orders_common_add_order_payments_request)

Add order payments.



 > Allowed from version `8.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_orders_common_add_order_payments_request import TransportOrdersCommonAddOrderPaymentsRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_orders_common_add_order_payments_request = iiko_cloud_client.TransportOrdersCommonAddOrderPaymentsRequest() # TransportOrdersCommonAddOrderPaymentsRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.api1_deliveries_add_payments_post(authorization, timeout=timeout, transport_orders_common_add_order_payments_request=transport_orders_common_add_order_payments_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_add_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_add_payments_post: %s\n" % e)
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

# **api1_deliveries_cancel_confirmation_post**
> TransportCommonCorrelationIdResponse api1_deliveries_cancel_confirmation_post(authorization, timeout=timeout, transport_deliveries_request_update_order_cancel_delivery_confirmation_request=transport_deliveries_request_update_order_cancel_delivery_confirmation_request)

Cancel delivery confirmation.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_cancel_delivery_confirmation_request import TransportDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_cancel_delivery_confirmation_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest() # TransportDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest |  (optional)

    try:
        # Cancel delivery confirmation.
        api_response = await api_instance.api1_deliveries_cancel_confirmation_post(authorization, timeout=timeout, transport_deliveries_request_update_order_cancel_delivery_confirmation_request=transport_deliveries_request_update_order_cancel_delivery_confirmation_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_cancel_confirmation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_cancel_confirmation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_cancel_delivery_confirmation_request** | [**TransportDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest**](TransportDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest.md)|  | [optional] 

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

# **api1_deliveries_cancel_post**
> TransportCommonCorrelationIdResponse api1_deliveries_cancel_post(authorization, timeout=timeout, transport_deliveries_request_cancel_order_request=transport_deliveries_request_cancel_order_request)

Cancel delivery order.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_cancel_order_request import TransportDeliveriesRequestCancelOrderRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_cancel_order_request = iiko_cloud_client.TransportDeliveriesRequestCancelOrderRequest() # TransportDeliveriesRequestCancelOrderRequest |  (optional)

    try:
        # Cancel delivery order.
        api_response = await api_instance.api1_deliveries_cancel_post(authorization, timeout=timeout, transport_deliveries_request_cancel_order_request=transport_deliveries_request_cancel_order_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_cancel_order_request** | [**TransportDeliveriesRequestCancelOrderRequest**](TransportDeliveriesRequestCancelOrderRequest.md)|  | [optional] 

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

# **api1_deliveries_change_comment_post**
> TransportCommonCorrelationIdResponse api1_deliveries_change_comment_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_delivery_comment_request=transport_deliveries_request_update_order_change_delivery_comment_request)

Change delivery comment.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_delivery_comment_request import TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_change_delivery_comment_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest() # TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest |  (optional)

    try:
        # Change delivery comment.
        api_response = await api_instance.api1_deliveries_change_comment_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_delivery_comment_request=transport_deliveries_request_update_order_change_delivery_comment_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_change_comment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_change_comment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_change_delivery_comment_request** | [**TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest**](TransportDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.md)|  | [optional] 

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

# **api1_deliveries_change_complete_before_post**
> TransportCommonCorrelationIdResponse api1_deliveries_change_complete_before_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_complete_before_request=transport_deliveries_request_update_order_change_complete_before_request)

Change time when client wants the order to be delivered.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_complete_before_request import TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_change_complete_before_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest() # TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest |  (optional)

    try:
        # Change time when client wants the order to be delivered.
        api_response = await api_instance.api1_deliveries_change_complete_before_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_complete_before_request=transport_deliveries_request_update_order_change_complete_before_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_change_complete_before_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_change_complete_before_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_change_complete_before_request** | [**TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest**](TransportDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest.md)|  | [optional] 

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

# **api1_deliveries_change_delivery_point_post**
> TransportCommonCorrelationIdResponse api1_deliveries_change_delivery_point_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_delivery_point_request=transport_deliveries_request_update_order_change_delivery_point_request)

Change order's delivery point information.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_delivery_point_request import TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_change_delivery_point_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest() # TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest |  (optional)

    try:
        # Change order's delivery point information.
        api_response = await api_instance.api1_deliveries_change_delivery_point_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_delivery_point_request=transport_deliveries_request_update_order_change_delivery_point_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_change_delivery_point_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_change_delivery_point_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_change_delivery_point_request** | [**TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest**](TransportDeliveriesRequestUpdateOrderChangeDeliveryPointRequest.md)|  | [optional] 

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

# **api1_deliveries_change_driver_info_post**
> TransportCommonCorrelationIdResponse api1_deliveries_change_driver_info_post(authorization, timeout=timeout, transport_deliveries_request_change_driver_info_request=transport_deliveries_request_change_driver_info_request)

Change driver info.



 > Allowed from version `8.6.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order driver: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_change_driver_info_request import TransportDeliveriesRequestChangeDriverInfoRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_change_driver_info_request = iiko_cloud_client.TransportDeliveriesRequestChangeDriverInfoRequest() # TransportDeliveriesRequestChangeDriverInfoRequest |  (optional)

    try:
        # Change driver info.
        api_response = await api_instance.api1_deliveries_change_driver_info_post(authorization, timeout=timeout, transport_deliveries_request_change_driver_info_request=transport_deliveries_request_change_driver_info_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_change_driver_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_change_driver_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_change_driver_info_request** | [**TransportDeliveriesRequestChangeDriverInfoRequest**](TransportDeliveriesRequestChangeDriverInfoRequest.md)|  | [optional] 

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

# **api1_deliveries_change_external_data_post**
> TransportCommonCorrelationIdResponse api1_deliveries_change_external_data_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_external_data_request=transport_deliveries_request_update_order_change_external_data_request)

Change delivery external data.



 > Restriction group: `Orders: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_external_data_request import TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_change_external_data_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest() # TransportDeliveriesRequestUpdateOrderChangeExternalDataRequest |  (optional)

    try:
        # Change delivery external data.
        api_response = await api_instance.api1_deliveries_change_external_data_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_external_data_request=transport_deliveries_request_update_order_change_external_data_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_change_external_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_change_external_data_post: %s\n" % e)
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

# **api1_deliveries_change_operator_post**
> TransportCommonCorrelationIdResponse api1_deliveries_change_operator_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_delivery_operator_request=transport_deliveries_request_update_order_change_delivery_operator_request)

Assign/change the order operator.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_delivery_operator_request import TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_change_delivery_operator_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest() # TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest |  (optional)

    try:
        # Assign/change the order operator.
        api_response = await api_instance.api1_deliveries_change_operator_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_delivery_operator_request=transport_deliveries_request_update_order_change_delivery_operator_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_change_operator_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_change_operator_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_change_delivery_operator_request** | [**TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest**](TransportDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest.md)|  | [optional] 

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

# **api1_deliveries_change_payments_post**
> TransportCommonCorrelationIdResponse api1_deliveries_change_payments_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_payments_request=transport_deliveries_request_update_order_change_payments_request)

Change order's payments.

> Method will fail if there are any processed payments in the order.
> If all payments in the order are unprocessed they will be removed and replaced with new ones.

 > Allowed from version `7.6.3`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_payments_request import TransportDeliveriesRequestUpdateOrderChangePaymentsRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_change_payments_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderChangePaymentsRequest() # TransportDeliveriesRequestUpdateOrderChangePaymentsRequest |  (optional)

    try:
        # Change order's payments.
        api_response = await api_instance.api1_deliveries_change_payments_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_payments_request=transport_deliveries_request_update_order_change_payments_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_change_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_change_payments_post: %s\n" % e)
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

# **api1_deliveries_change_service_type_post**
> TransportCommonCorrelationIdResponse api1_deliveries_change_service_type_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_service_type_request=transport_deliveries_request_update_order_change_service_type_request)

Change order's delivery type.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_change_service_type_request import TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_change_service_type_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest() # TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest |  (optional)

    try:
        # Change order's delivery type.
        api_response = await api_instance.api1_deliveries_change_service_type_post(authorization, timeout=timeout, transport_deliveries_request_update_order_change_service_type_request=transport_deliveries_request_update_order_change_service_type_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_change_service_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_change_service_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_change_service_type_request** | [**TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest**](TransportDeliveriesRequestUpdateOrderChangeServiceTypeRequest.md)|  | [optional] 

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

# **api1_deliveries_close_post**
> TransportCommonCorrelationIdResponse api1_deliveries_close_post(authorization, timeout=timeout, transport_deliveries_request_close_delivery_order_request=transport_deliveries_request_close_delivery_order_request)

Close order.

> Before version `8.0.6` it's possible to close deliveries with `DeliveryByClient`
orderServiceType only, starting from version `8.0.6` it's also possible to close
`DeliveryByCourier` deiveries in the DeliveryStatus `OnWay` or `Delivered` .

 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_close_delivery_order_request import TransportDeliveriesRequestCloseDeliveryOrderRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_close_delivery_order_request = iiko_cloud_client.TransportDeliveriesRequestCloseDeliveryOrderRequest() # TransportDeliveriesRequestCloseDeliveryOrderRequest |  (optional)

    try:
        # Close order.
        api_response = await api_instance.api1_deliveries_close_post(authorization, timeout=timeout, transport_deliveries_request_close_delivery_order_request=transport_deliveries_request_close_delivery_order_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_close_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_close_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_close_delivery_order_request** | [**TransportDeliveriesRequestCloseDeliveryOrderRequest**](TransportDeliveriesRequestCloseDeliveryOrderRequest.md)|  | [optional] 

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

# **api1_deliveries_confirm_post**
> TransportCommonCorrelationIdResponse api1_deliveries_confirm_post(authorization, timeout=timeout, transport_deliveries_request_update_order_confirm_delivery_request=transport_deliveries_request_update_order_confirm_delivery_request)

Confirm delivery.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_confirm_delivery_request import TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_confirm_delivery_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest() # TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest |  (optional)

    try:
        # Confirm delivery.
        api_response = await api_instance.api1_deliveries_confirm_post(authorization, timeout=timeout, transport_deliveries_request_update_order_confirm_delivery_request=transport_deliveries_request_update_order_confirm_delivery_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_confirm_delivery_request** | [**TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest**](TransportDeliveriesRequestUpdateOrderConfirmDeliveryRequest.md)|  | [optional] 

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

# **api1_deliveries_create_post**
> TransportDeliveriesResponseOrderResponse api1_deliveries_create_post(authorization, timeout=timeout, transport_deliveries_request_create_order_request=transport_deliveries_request_create_order_request)

Create delivery.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_deliveries_request_create_order_request import TransportDeliveriesRequestCreateOrderRequest
from iiko_cloud_client.models.transport_deliveries_response_order_response import TransportDeliveriesResponseOrderResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_create_order_request = iiko_cloud_client.TransportDeliveriesRequestCreateOrderRequest() # TransportDeliveriesRequestCreateOrderRequest |  (optional)

    try:
        # Create delivery.
        api_response = await api_instance.api1_deliveries_create_post(authorization, timeout=timeout, transport_deliveries_request_create_order_request=transport_deliveries_request_create_order_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_create_order_request** | [**TransportDeliveriesRequestCreateOrderRequest**](TransportDeliveriesRequestCreateOrderRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseOrderResponse**](TransportDeliveriesResponseOrderResponse.md)

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

# **api1_deliveries_print_delivery_bill_post**
> TransportCommonCorrelationIdResponse api1_deliveries_print_delivery_bill_post(authorization, timeout=timeout, transport_deliveries_request_print_delivery_bill_request=transport_deliveries_request_print_delivery_bill_request)

Print delivery bill.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_print_delivery_bill_request import TransportDeliveriesRequestPrintDeliveryBillRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_print_delivery_bill_request = iiko_cloud_client.TransportDeliveriesRequestPrintDeliveryBillRequest() # TransportDeliveriesRequestPrintDeliveryBillRequest |  (optional)

    try:
        # Print delivery bill.
        api_response = await api_instance.api1_deliveries_print_delivery_bill_post(authorization, timeout=timeout, transport_deliveries_request_print_delivery_bill_request=transport_deliveries_request_print_delivery_bill_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_print_delivery_bill_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_print_delivery_bill_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_print_delivery_bill_request** | [**TransportDeliveriesRequestPrintDeliveryBillRequest**](TransportDeliveriesRequestPrintDeliveryBillRequest.md)|  | [optional] 

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

# **api1_deliveries_update_order_courier_post**
> TransportCommonCorrelationIdResponse api1_deliveries_update_order_courier_post(authorization, timeout=timeout, transport_deliveries_request_update_order_courier_request=transport_deliveries_request_update_order_courier_request)

Update order courier.



 > Allowed from version `7.1.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order driver: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_courier_request import TransportDeliveriesRequestUpdateOrderCourierRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_courier_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderCourierRequest() # TransportDeliveriesRequestUpdateOrderCourierRequest |  (optional)

    try:
        # Update order courier.
        api_response = await api_instance.api1_deliveries_update_order_courier_post(authorization, timeout=timeout, transport_deliveries_request_update_order_courier_request=transport_deliveries_request_update_order_courier_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_update_order_courier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_update_order_courier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_courier_request** | [**TransportDeliveriesRequestUpdateOrderCourierRequest**](TransportDeliveriesRequestUpdateOrderCourierRequest.md)|  | [optional] 

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

# **api1_deliveries_update_order_delivery_status_post**
> TransportCommonCorrelationIdResponse api1_deliveries_update_order_delivery_status_post(authorization, timeout=timeout, transport_deliveries_request_update_delivery_status_request=transport_deliveries_request_update_delivery_status_request)

Update delivery status.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_delivery_status_request import TransportDeliveriesRequestUpdateDeliveryStatusRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_delivery_status_request = iiko_cloud_client.TransportDeliveriesRequestUpdateDeliveryStatusRequest() # TransportDeliveriesRequestUpdateDeliveryStatusRequest |  (optional)

    try:
        # Update delivery status.
        api_response = await api_instance.api1_deliveries_update_order_delivery_status_post(authorization, timeout=timeout, transport_deliveries_request_update_delivery_status_request=transport_deliveries_request_update_delivery_status_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_update_order_delivery_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_update_order_delivery_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_delivery_status_request** | [**TransportDeliveriesRequestUpdateDeliveryStatusRequest**](TransportDeliveriesRequestUpdateDeliveryStatusRequest.md)|  | [optional] 

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

# **api1_deliveries_update_order_payments_post**
> TransportCommonCorrelationIdResponse api1_deliveries_update_order_payments_post(authorization, timeout=timeout, transport_deliveries_request_update_order_payments_request=transport_deliveries_request_update_order_payments_request)

Update order payment details.

> Deprecated, use `api/1/deliveries/change_payments` method instead.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Deprecated`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_payments_request import TransportDeliveriesRequestUpdateOrderPaymentsRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_payments_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderPaymentsRequest() # TransportDeliveriesRequestUpdateOrderPaymentsRequest |  (optional)

    try:
        # Update order payment details.
        api_response = await api_instance.api1_deliveries_update_order_payments_post(authorization, timeout=timeout, transport_deliveries_request_update_order_payments_request=transport_deliveries_request_update_order_payments_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_update_order_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_update_order_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_payments_request** | [**TransportDeliveriesRequestUpdateOrderPaymentsRequest**](TransportDeliveriesRequestUpdateOrderPaymentsRequest.md)|  | [optional] 

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

# **api1_deliveries_update_order_problem_post**
> TransportCommonCorrelationIdResponse api1_deliveries_update_order_problem_post(authorization, timeout=timeout, transport_deliveries_request_update_order_problem_request=transport_deliveries_request_update_order_problem_request)

Update order problem.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_deliveries_request_update_order_problem_request import TransportDeliveriesRequestUpdateOrderProblemRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.DeliveriesCreateAndUpdateApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_problem_request = iiko_cloud_client.TransportDeliveriesRequestUpdateOrderProblemRequest() # TransportDeliveriesRequestUpdateOrderProblemRequest |  (optional)

    try:
        # Update order problem.
        api_response = await api_instance.api1_deliveries_update_order_problem_post(authorization, timeout=timeout, transport_deliveries_request_update_order_problem_request=transport_deliveries_request_update_order_problem_request)
        print("The response of DeliveriesCreateAndUpdateApi->api1_deliveries_update_order_problem_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->api1_deliveries_update_order_problem_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_problem_request** | [**TransportDeliveriesRequestUpdateOrderProblemRequest**](TransportDeliveriesRequestUpdateOrderProblemRequest.md)|  | [optional] 

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

