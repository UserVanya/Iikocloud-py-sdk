# iikocloud_client.DeliveriesCreateAndUpdateApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deliveries_add_items_post**](DeliveriesCreateAndUpdateApi.md#deliveries_add_items_post) | **POST** /deliveries/add_items | Add order items.
[**deliveries_add_payments_post**](DeliveriesCreateAndUpdateApi.md#deliveries_add_payments_post) | **POST** /deliveries/add_payments | Add order payments.
[**deliveries_cancel_confirmation_post**](DeliveriesCreateAndUpdateApi.md#deliveries_cancel_confirmation_post) | **POST** /deliveries/cancel_confirmation | Cancel delivery confirmation.
[**deliveries_cancel_post**](DeliveriesCreateAndUpdateApi.md#deliveries_cancel_post) | **POST** /deliveries/cancel | Cancel delivery order.
[**deliveries_change_comment_post**](DeliveriesCreateAndUpdateApi.md#deliveries_change_comment_post) | **POST** /deliveries/change_comment | Change delivery comment.
[**deliveries_change_complete_before_post**](DeliveriesCreateAndUpdateApi.md#deliveries_change_complete_before_post) | **POST** /deliveries/change_complete_before | Change time when client wants the order to be delivered.
[**deliveries_change_delivery_point_post**](DeliveriesCreateAndUpdateApi.md#deliveries_change_delivery_point_post) | **POST** /deliveries/change_delivery_point | Change order&#39;s delivery point information.
[**deliveries_change_driver_info_post**](DeliveriesCreateAndUpdateApi.md#deliveries_change_driver_info_post) | **POST** /deliveries/change_driver_info | Change driver info.
[**deliveries_change_external_data_post**](DeliveriesCreateAndUpdateApi.md#deliveries_change_external_data_post) | **POST** /deliveries/change_external_data | Change delivery external data.
[**deliveries_change_operator_post**](DeliveriesCreateAndUpdateApi.md#deliveries_change_operator_post) | **POST** /deliveries/change_operator | Assign/change the order operator.
[**deliveries_change_payments_post**](DeliveriesCreateAndUpdateApi.md#deliveries_change_payments_post) | **POST** /deliveries/change_payments | Change order&#39;s payments.
[**deliveries_change_service_type_post**](DeliveriesCreateAndUpdateApi.md#deliveries_change_service_type_post) | **POST** /deliveries/change_service_type | Change order&#39;s delivery type.
[**deliveries_close_post**](DeliveriesCreateAndUpdateApi.md#deliveries_close_post) | **POST** /deliveries/close | Close order.
[**deliveries_confirm_post**](DeliveriesCreateAndUpdateApi.md#deliveries_confirm_post) | **POST** /deliveries/confirm | Confirm delivery.
[**deliveries_create_post**](DeliveriesCreateAndUpdateApi.md#deliveries_create_post) | **POST** /deliveries/create | Create delivery.
[**deliveries_print_delivery_bill_post**](DeliveriesCreateAndUpdateApi.md#deliveries_print_delivery_bill_post) | **POST** /deliveries/print_delivery_bill | Print delivery bill.
[**deliveries_update_order_courier_post**](DeliveriesCreateAndUpdateApi.md#deliveries_update_order_courier_post) | **POST** /deliveries/update_order_courier | Update order courier.
[**deliveries_update_order_delivery_status_post**](DeliveriesCreateAndUpdateApi.md#deliveries_update_order_delivery_status_post) | **POST** /deliveries/update_order_delivery_status | Update delivery status.
[**deliveries_update_order_payments_post**](DeliveriesCreateAndUpdateApi.md#deliveries_update_order_payments_post) | **POST** /deliveries/update_order_payments | Update order payment details.
[**deliveries_update_order_problem_post**](DeliveriesCreateAndUpdateApi.md#deliveries_update_order_problem_post) | **POST** /deliveries/update_order_problem | Update order problem.
[**deliveries_update_tracking_link_post**](DeliveriesCreateAndUpdateApi.md#deliveries_update_tracking_link_post) | **POST** /deliveries/update_tracking_link | Update tracking link of an order.
[**order_print_bill_post**](DeliveriesCreateAndUpdateApi.md#order_print_bill_post) | **POST** /order/print_bill | Print bill.


# **deliveries_add_items_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_add_items_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_add_order_items_request=iiko_transport_public_api_contracts_deliveries_request_add_order_items_request)

Add order items.



 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_add_order_items_request import IikoTransportPublicApiContractsDeliveriesRequestAddOrderItemsRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_add_order_items_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestAddOrderItemsRequest() # IikoTransportPublicApiContractsDeliveriesRequestAddOrderItemsRequest |  (optional)

    try:
        # Add order items.
        api_response = await api_instance.deliveries_add_items_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_add_order_items_request=iiko_transport_public_api_contracts_deliveries_request_add_order_items_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_add_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_add_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_add_order_items_request** | [**IikoTransportPublicApiContractsDeliveriesRequestAddOrderItemsRequest**](IikoTransportPublicApiContractsDeliveriesRequestAddOrderItemsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_add_payments_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_add_payments_post(timeout=timeout, iiko_transport_public_api_contracts_orders_common_add_order_payments_request=iiko_transport_public_api_contracts_orders_common_add_order_payments_request)

Add order payments.



 > Allowed from version `8.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_orders_common_add_order_payments_request = iikocloud_client.IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest() # IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest |  (optional)

    try:
        # Add order payments.
        api_response = await api_instance.deliveries_add_payments_post(timeout=timeout, iiko_transport_public_api_contracts_orders_common_add_order_payments_request=iiko_transport_public_api_contracts_orders_common_add_order_payments_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_add_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_add_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_orders_common_add_order_payments_request** | [**IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest**](IikoTransportPublicApiContractsOrdersCommonAddOrderPaymentsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_cancel_confirmation_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_cancel_confirmation_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request=iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request)

Cancel delivery confirmation.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest |  (optional)

    try:
        # Cancel delivery confirmation.
        api_response = await api_instance.deliveries_cancel_confirmation_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request=iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_cancel_confirmation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_cancel_confirmation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_cancel_delivery_confirmation_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCancelDeliveryConfirmationRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_cancel_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_cancel_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_cancel_order_request=iiko_transport_public_api_contracts_deliveries_request_cancel_order_request)

Cancel delivery order.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_cancel_order_request import IikoTransportPublicApiContractsDeliveriesRequestCancelOrderRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_cancel_order_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestCancelOrderRequest() # IikoTransportPublicApiContractsDeliveriesRequestCancelOrderRequest |  (optional)

    try:
        # Cancel delivery order.
        api_response = await api_instance.deliveries_cancel_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_cancel_order_request=iiko_transport_public_api_contracts_deliveries_request_cancel_order_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_cancel_order_request** | [**IikoTransportPublicApiContractsDeliveriesRequestCancelOrderRequest**](IikoTransportPublicApiContractsDeliveriesRequestCancelOrderRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_change_comment_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_change_comment_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request)

Change delivery comment.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest |  (optional)

    try:
        # Change delivery comment.
        api_response = await api_instance.deliveries_change_comment_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_change_comment_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_change_comment_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_comment_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryCommentRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_change_complete_before_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_change_complete_before_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_complete_before_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_complete_before_request)

Change time when client wants the order to be delivered.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_complete_before_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_change_complete_before_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest |  (optional)

    try:
        # Change time when client wants the order to be delivered.
        api_response = await api_instance.deliveries_change_complete_before_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_complete_before_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_complete_before_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_change_complete_before_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_change_complete_before_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_change_complete_before_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeCompleteBeforeRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_change_delivery_point_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_change_delivery_point_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request)

Change order's delivery point information.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest |  (optional)

    try:
        # Change order's delivery point information.
        api_response = await api_instance.deliveries_change_delivery_point_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_change_delivery_point_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_change_delivery_point_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_point_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryPointRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_change_driver_info_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_change_driver_info_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_change_driver_info_request=iiko_transport_public_api_contracts_deliveries_request_change_driver_info_request)

Change driver info.



 > Allowed from version `8.6.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order driver: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_change_driver_info_request import IikoTransportPublicApiContractsDeliveriesRequestChangeDriverInfoRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_change_driver_info_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestChangeDriverInfoRequest() # IikoTransportPublicApiContractsDeliveriesRequestChangeDriverInfoRequest |  (optional)

    try:
        # Change driver info.
        api_response = await api_instance.deliveries_change_driver_info_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_change_driver_info_request=iiko_transport_public_api_contracts_deliveries_request_change_driver_info_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_change_driver_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_change_driver_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_change_driver_info_request** | [**IikoTransportPublicApiContractsDeliveriesRequestChangeDriverInfoRequest**](IikoTransportPublicApiContractsDeliveriesRequestChangeDriverInfoRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_change_external_data_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_change_external_data_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request)

Change delivery external data.



 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest |  (optional)

    try:
        # Change delivery external data.
        api_response = await api_instance.deliveries_change_external_data_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_change_external_data_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_change_external_data_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_change_external_data_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeExternalDataRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_change_operator_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_change_operator_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request)

Assign/change the order operator.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest |  (optional)

    try:
        # Assign/change the order operator.
        api_response = await api_instance.deliveries_change_operator_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_change_operator_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_change_operator_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_change_delivery_operator_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeDeliveryOperatorRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_change_payments_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_change_payments_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request)

Change order's payments.

> Method will fail if there are any processed payments in the order.
> If all payments in the order are unprocessed they will be removed and replaced with new ones.

 > Allowed from version `7.6.3`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order payments: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest |  (optional)

    try:
        # Change order's payments.
        api_response = await api_instance.deliveries_change_payments_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_change_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_change_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_change_payments_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangePaymentsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_change_service_type_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_change_service_type_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request)

Change order's delivery type.



 > Allowed from version `7.5.4`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest |  (optional)

    try:
        # Change order's delivery type.
        api_response = await api_instance.deliveries_change_service_type_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request=iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_change_service_type_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_change_service_type_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_change_service_type_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderChangeServiceTypeRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_close_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_close_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request=iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request)

Close order.

> Before version `8.0.6` it's possible to close deliveries with `DeliveryByClient`
orderServiceType only, starting from version `8.0.6` it's also possible to close
`DeliveryByCourier` deiveries in the DeliveryStatus `OnWay` or `Delivered` .

 > Allowed from version `7.4.6`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request import IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest() # IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest |  (optional)

    try:
        # Close order.
        api_response = await api_instance.deliveries_close_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request=iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_close_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_close_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_close_delivery_order_request** | [**IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest**](IikoTransportPublicApiContractsDeliveriesRequestCloseDeliveryOrderRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_confirm_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_confirm_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_confirm_delivery_request=iiko_transport_public_api_contracts_deliveries_request_update_order_confirm_delivery_request)

Confirm delivery.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_confirm_delivery_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderConfirmDeliveryRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_confirm_delivery_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderConfirmDeliveryRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderConfirmDeliveryRequest |  (optional)

    try:
        # Confirm delivery.
        api_response = await api_instance.deliveries_confirm_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_confirm_delivery_request=iiko_transport_public_api_contracts_deliveries_request_update_order_confirm_delivery_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_confirm_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_confirm_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_confirm_delivery_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderConfirmDeliveryRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderConfirmDeliveryRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_create_post**
> IikoTransportPublicApiContractsDeliveriesResponseOrderResponse deliveries_create_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_create_order_request=iiko_transport_public_api_contracts_deliveries_request_create_order_request)

Create delivery.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: creating`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_request import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_response_order_response import IikoTransportPublicApiContractsDeliveriesResponseOrderResponse
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_create_order_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest() # IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest |  (optional)

    try:
        # Create delivery.
        api_response = await api_instance.deliveries_create_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_create_order_request=iiko_transport_public_api_contracts_deliveries_request_create_order_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_create_order_request** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveriesResponseOrderResponse**](IikoTransportPublicApiContractsDeliveriesResponseOrderResponse.md)

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

# **deliveries_print_delivery_bill_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_print_delivery_bill_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_print_delivery_bill_request=iiko_transport_public_api_contracts_deliveries_request_print_delivery_bill_request)

Print delivery bill.



 > Allowed from version `7.6.1`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Orders: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_print_delivery_bill_request import IikoTransportPublicApiContractsDeliveriesRequestPrintDeliveryBillRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_print_delivery_bill_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestPrintDeliveryBillRequest() # IikoTransportPublicApiContractsDeliveriesRequestPrintDeliveryBillRequest |  (optional)

    try:
        # Print delivery bill.
        api_response = await api_instance.deliveries_print_delivery_bill_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_print_delivery_bill_request=iiko_transport_public_api_contracts_deliveries_request_print_delivery_bill_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_print_delivery_bill_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_print_delivery_bill_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_print_delivery_bill_request** | [**IikoTransportPublicApiContractsDeliveriesRequestPrintDeliveryBillRequest**](IikoTransportPublicApiContractsDeliveriesRequestPrintDeliveryBillRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_update_order_courier_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_update_order_courier_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request=iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request)

Update order courier.



 > Allowed from version `7.1.5`.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order driver: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest |  (optional)

    try:
        # Update order courier.
        api_response = await api_instance.deliveries_update_order_courier_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request=iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_update_order_courier_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_update_order_courier_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_courier_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderCourierRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_update_order_delivery_status_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_update_order_delivery_status_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request=iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request)

Update delivery status.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest |  (optional)

    try:
        # Update delivery status.
        api_response = await api_instance.deliveries_update_order_delivery_status_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request=iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_update_order_delivery_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_update_order_delivery_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_delivery_status_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateDeliveryStatusRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_update_order_payments_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_update_order_payments_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request=iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request)

Update order payment details.

> Deprecated, use `api/1/deliveries/change_payments` method instead.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Deprecated`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest |  (optional)

    try:
        # Update order payment details.
        api_response = await api_instance.deliveries_update_order_payments_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request=iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_update_order_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_update_order_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_update_order_problem_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_update_order_problem_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request=iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request)

Update order problem.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Order status: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest |  (optional)

    try:
        # Update order problem.
        api_response = await api_instance.deliveries_update_order_problem_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request=iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request)
        print("The response of DeliveriesCreateAndUpdateApi->deliveries_update_order_problem_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_update_order_problem_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_problem_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderProblemRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **deliveries_update_tracking_link_post**
> deliveries_update_tracking_link_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request=iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request)

Update tracking link of an order.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest |  (optional)

    try:
        # Update tracking link of an order.
        await api_instance.deliveries_update_tracking_link_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request=iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->deliveries_update_tracking_link_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_tracking_link_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateTrackingLinkRequest.md)|  | [optional] 

### Return type

void (empty response body)

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

# **order_print_bill_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse order_print_bill_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_print_bill_request=iiko_transport_public_api_contracts_deliveries_request_print_bill_request)

Print bill.



 > This method is a command. Use `api/1/commands/status` method to get the progress status.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_print_bill_request import IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest
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
    api_instance = iikocloud_client.DeliveriesCreateAndUpdateApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_print_bill_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest() # IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest |  (optional)

    try:
        # Print bill.
        api_response = await api_instance.order_print_bill_post(timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_print_bill_request=iiko_transport_public_api_contracts_deliveries_request_print_bill_request)
        print("The response of DeliveriesCreateAndUpdateApi->order_print_bill_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveriesCreateAndUpdateApi->order_print_bill_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_print_bill_request** | [**IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest**](IikoTransportPublicApiContractsDeliveriesRequestPrintBillRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

