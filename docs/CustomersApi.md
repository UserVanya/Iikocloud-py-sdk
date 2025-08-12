# iikocloud_client.CustomersApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loyalty_iiko_customer_card_add_post**](CustomersApi.md#loyalty_iiko_customer_card_add_post) | **POST** /loyalty/iiko/customer/card/add | Add card.
[**loyalty_iiko_customer_card_remove_post**](CustomersApi.md#loyalty_iiko_customer_card_remove_post) | **POST** /loyalty/iiko/customer/card/remove | Delete card.
[**loyalty_iiko_customer_create_or_update_post**](CustomersApi.md#loyalty_iiko_customer_create_or_update_post) | **POST** /loyalty/iiko/customer/create_or_update | Create or update customer.
[**loyalty_iiko_customer_info_post**](CustomersApi.md#loyalty_iiko_customer_info_post) | **POST** /loyalty/iiko/customer/info | Get customer info.
[**loyalty_iiko_customer_program_add_post**](CustomersApi.md#loyalty_iiko_customer_program_add_post) | **POST** /loyalty/iiko/customer/program/add | Add customer to program.
[**loyalty_iiko_customer_wallet_cancel_hold_post**](CustomersApi.md#loyalty_iiko_customer_wallet_cancel_hold_post) | **POST** /loyalty/iiko/customer/wallet/cancel_hold | Cancel hold money.
[**loyalty_iiko_customer_wallet_chargeoff_post**](CustomersApi.md#loyalty_iiko_customer_wallet_chargeoff_post) | **POST** /loyalty/iiko/customer/wallet/chargeoff | Withdraw balance.
[**loyalty_iiko_customer_wallet_hold_post**](CustomersApi.md#loyalty_iiko_customer_wallet_hold_post) | **POST** /loyalty/iiko/customer/wallet/hold | Hold money.
[**loyalty_iiko_customer_wallet_topup_post**](CustomersApi.md#loyalty_iiko_customer_wallet_topup_post) | **POST** /loyalty/iiko/customer/wallet/topup | Refill balance.
[**loyalty_iiko_delete_customers_post**](CustomersApi.md#loyalty_iiko_delete_customers_post) | **POST** /loyalty/iiko/delete_customers | Logical deletion of customers.
[**loyalty_iiko_get_counters_post**](CustomersApi.md#loyalty_iiko_get_counters_post) | **POST** /loyalty/iiko/get_counters | Get counters.
[**loyalty_iiko_restore_customers_post**](CustomersApi.md#loyalty_iiko_restore_customers_post) | **POST** /loyalty/iiko/restore_customers | Logical recovery of customers.


# **loyalty_iiko_customer_card_add_post**
> object loyalty_iiko_customer_card_add_post(timeout=timeout, net_customer_add_magnet_card_request=net_customer_add_magnet_card_request)

Add card.

Add new card for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_add_magnet_card_request import NetCustomerAddMagnetCardRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_add_magnet_card_request = iikocloud_client.NetCustomerAddMagnetCardRequest() # NetCustomerAddMagnetCardRequest |  (optional)

    try:
        # Add card.
        api_response = await api_instance.loyalty_iiko_customer_card_add_post(timeout=timeout, net_customer_add_magnet_card_request=net_customer_add_magnet_card_request)
        print("The response of CustomersApi->loyalty_iiko_customer_card_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_card_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_add_magnet_card_request** | [**NetCustomerAddMagnetCardRequest**](NetCustomerAddMagnetCardRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_card_remove_post**
> object loyalty_iiko_customer_card_remove_post(timeout=timeout, net_customer_delete_magnet_card_request=net_customer_delete_magnet_card_request)

Delete card.

Delete existing card for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_delete_magnet_card_request import NetCustomerDeleteMagnetCardRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_delete_magnet_card_request = iikocloud_client.NetCustomerDeleteMagnetCardRequest() # NetCustomerDeleteMagnetCardRequest |  (optional)

    try:
        # Delete card.
        api_response = await api_instance.loyalty_iiko_customer_card_remove_post(timeout=timeout, net_customer_delete_magnet_card_request=net_customer_delete_magnet_card_request)
        print("The response of CustomersApi->loyalty_iiko_customer_card_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_card_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_delete_magnet_card_request** | [**NetCustomerDeleteMagnetCardRequest**](NetCustomerDeleteMagnetCardRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_create_or_update_post**
> NetCustomerCreateOrUpdateCustomerResponse loyalty_iiko_customer_create_or_update_post(timeout=timeout, net_customer_create_or_update_customer_request=net_customer_create_or_update_customer_request)

Create or update customer.

Create or update customer info by id or phone or card track.

 > Restriction group: `Guests: creating`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_create_or_update_customer_request import NetCustomerCreateOrUpdateCustomerRequest
from iikocloud_client.models.net_customer_create_or_update_customer_response import NetCustomerCreateOrUpdateCustomerResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_create_or_update_customer_request = iikocloud_client.NetCustomerCreateOrUpdateCustomerRequest() # NetCustomerCreateOrUpdateCustomerRequest |  (optional)

    try:
        # Create or update customer.
        api_response = await api_instance.loyalty_iiko_customer_create_or_update_post(timeout=timeout, net_customer_create_or_update_customer_request=net_customer_create_or_update_customer_request)
        print("The response of CustomersApi->loyalty_iiko_customer_create_or_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_create_or_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_create_or_update_customer_request** | [**NetCustomerCreateOrUpdateCustomerRequest**](NetCustomerCreateOrUpdateCustomerRequest.md)|  | [optional] 

### Return type

[**NetCustomerCreateOrUpdateCustomerResponse**](NetCustomerCreateOrUpdateCustomerResponse.md)

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

# **loyalty_iiko_customer_info_post**
> NetCustomerGetCustomerInfoResponse loyalty_iiko_customer_info_post(timeout=timeout, net_customer_get_customer_info_request=net_customer_get_customer_info_request)

Get customer info.

Get customer info by specified criterion.

 > Restriction group: `Guests: info`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_get_customer_info_request import NetCustomerGetCustomerInfoRequest
from iikocloud_client.models.net_customer_get_customer_info_response import NetCustomerGetCustomerInfoResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_get_customer_info_request = iikocloud_client.NetCustomerGetCustomerInfoRequest() # NetCustomerGetCustomerInfoRequest |  (optional)

    try:
        # Get customer info.
        api_response = await api_instance.loyalty_iiko_customer_info_post(timeout=timeout, net_customer_get_customer_info_request=net_customer_get_customer_info_request)
        print("The response of CustomersApi->loyalty_iiko_customer_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_get_customer_info_request** | [**NetCustomerGetCustomerInfoRequest**](NetCustomerGetCustomerInfoRequest.md)|  | [optional] 

### Return type

[**NetCustomerGetCustomerInfoResponse**](NetCustomerGetCustomerInfoResponse.md)

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

# **loyalty_iiko_customer_program_add_post**
> NetCustomerAddCustomerToProgramResponse loyalty_iiko_customer_program_add_post(timeout=timeout, net_customer_add_customer_to_program_request=net_customer_add_customer_to_program_request)

Add customer to program.

Add new customer for program.

 > Restriction group: `Guests: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_add_customer_to_program_request import NetCustomerAddCustomerToProgramRequest
from iikocloud_client.models.net_customer_add_customer_to_program_response import NetCustomerAddCustomerToProgramResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_add_customer_to_program_request = iikocloud_client.NetCustomerAddCustomerToProgramRequest() # NetCustomerAddCustomerToProgramRequest |  (optional)

    try:
        # Add customer to program.
        api_response = await api_instance.loyalty_iiko_customer_program_add_post(timeout=timeout, net_customer_add_customer_to_program_request=net_customer_add_customer_to_program_request)
        print("The response of CustomersApi->loyalty_iiko_customer_program_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_program_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_add_customer_to_program_request** | [**NetCustomerAddCustomerToProgramRequest**](NetCustomerAddCustomerToProgramRequest.md)|  | [optional] 

### Return type

[**NetCustomerAddCustomerToProgramResponse**](NetCustomerAddCustomerToProgramResponse.md)

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

# **loyalty_iiko_customer_wallet_cancel_hold_post**
> object loyalty_iiko_customer_wallet_cancel_hold_post(timeout=timeout, net_customer_cancel_hold_money_request=net_customer_cancel_hold_money_request)

Cancel hold money.

Cancel holding transaction that created earlier.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_cancel_hold_money_request import NetCustomerCancelHoldMoneyRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_cancel_hold_money_request = iikocloud_client.NetCustomerCancelHoldMoneyRequest() # NetCustomerCancelHoldMoneyRequest |  (optional)

    try:
        # Cancel hold money.
        api_response = await api_instance.loyalty_iiko_customer_wallet_cancel_hold_post(timeout=timeout, net_customer_cancel_hold_money_request=net_customer_cancel_hold_money_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_cancel_hold_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_cancel_hold_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_cancel_hold_money_request** | [**NetCustomerCancelHoldMoneyRequest**](NetCustomerCancelHoldMoneyRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_wallet_chargeoff_post**
> object loyalty_iiko_customer_wallet_chargeoff_post(timeout=timeout, net_customer_change_user_balance_request=net_customer_change_user_balance_request)

Withdraw balance.

Withdraw customer balance.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_change_user_balance_request import NetCustomerChangeUserBalanceRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_change_user_balance_request = iikocloud_client.NetCustomerChangeUserBalanceRequest() # NetCustomerChangeUserBalanceRequest |  (optional)

    try:
        # Withdraw balance.
        api_response = await api_instance.loyalty_iiko_customer_wallet_chargeoff_post(timeout=timeout, net_customer_change_user_balance_request=net_customer_change_user_balance_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_chargeoff_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_chargeoff_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_change_user_balance_request** | [**NetCustomerChangeUserBalanceRequest**](NetCustomerChangeUserBalanceRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_wallet_hold_post**
> NetCustomerHoldMoneyResponse loyalty_iiko_customer_wallet_hold_post(timeout=timeout, net_customer_hold_money_request=net_customer_hold_money_request)

Hold money.

Hold customer's money in loyalty program. Payment will be process on POS during processing of an order.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_hold_money_request import NetCustomerHoldMoneyRequest
from iikocloud_client.models.net_customer_hold_money_response import NetCustomerHoldMoneyResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_hold_money_request = iikocloud_client.NetCustomerHoldMoneyRequest() # NetCustomerHoldMoneyRequest |  (optional)

    try:
        # Hold money.
        api_response = await api_instance.loyalty_iiko_customer_wallet_hold_post(timeout=timeout, net_customer_hold_money_request=net_customer_hold_money_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_hold_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_hold_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_hold_money_request** | [**NetCustomerHoldMoneyRequest**](NetCustomerHoldMoneyRequest.md)|  | [optional] 

### Return type

[**NetCustomerHoldMoneyResponse**](NetCustomerHoldMoneyResponse.md)

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

# **loyalty_iiko_customer_wallet_topup_post**
> object loyalty_iiko_customer_wallet_topup_post(timeout=timeout, net_customer_change_user_balance_request=net_customer_change_user_balance_request)

Refill balance.

Refill customer balance.

 > Restriction group: `Loyalty: wallets`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_change_user_balance_request import NetCustomerChangeUserBalanceRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_change_user_balance_request = iikocloud_client.NetCustomerChangeUserBalanceRequest() # NetCustomerChangeUserBalanceRequest |  (optional)

    try:
        # Refill balance.
        api_response = await api_instance.loyalty_iiko_customer_wallet_topup_post(timeout=timeout, net_customer_change_user_balance_request=net_customer_change_user_balance_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_topup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_topup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_change_user_balance_request** | [**NetCustomerChangeUserBalanceRequest**](NetCustomerChangeUserBalanceRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_delete_customers_post**
> NetCustomerDeleteCustomersResponse loyalty_iiko_delete_customers_post(timeout=timeout, net_customer_delete_customers_request=net_customer_delete_customers_request)

Logical deletion of customers.

Mark customers as deleted.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_delete_customers_request import NetCustomerDeleteCustomersRequest
from iikocloud_client.models.net_customer_delete_customers_response import NetCustomerDeleteCustomersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_delete_customers_request = iikocloud_client.NetCustomerDeleteCustomersRequest() # NetCustomerDeleteCustomersRequest |  (optional)

    try:
        # Logical deletion of customers.
        api_response = await api_instance.loyalty_iiko_delete_customers_post(timeout=timeout, net_customer_delete_customers_request=net_customer_delete_customers_request)
        print("The response of CustomersApi->loyalty_iiko_delete_customers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_delete_customers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_delete_customers_request** | [**NetCustomerDeleteCustomersRequest**](NetCustomerDeleteCustomersRequest.md)|  | [optional] 

### Return type

[**NetCustomerDeleteCustomersResponse**](NetCustomerDeleteCustomersResponse.md)

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

# **loyalty_iiko_get_counters_post**
> NetLoyaltyResultGetCountersResponse loyalty_iiko_get_counters_post(timeout=timeout, net_loyalty_result_get_counters_request=net_loyalty_result_get_counters_request)

Get counters.

Get customer orders count and sum for different period.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_loyalty_result_get_counters_request import NetLoyaltyResultGetCountersRequest
from iikocloud_client.models.net_loyalty_result_get_counters_response import NetLoyaltyResultGetCountersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_loyalty_result_get_counters_request = iikocloud_client.NetLoyaltyResultGetCountersRequest() # NetLoyaltyResultGetCountersRequest |  (optional)

    try:
        # Get counters.
        api_response = await api_instance.loyalty_iiko_get_counters_post(timeout=timeout, net_loyalty_result_get_counters_request=net_loyalty_result_get_counters_request)
        print("The response of CustomersApi->loyalty_iiko_get_counters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_get_counters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_loyalty_result_get_counters_request** | [**NetLoyaltyResultGetCountersRequest**](NetLoyaltyResultGetCountersRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultGetCountersResponse**](NetLoyaltyResultGetCountersResponse.md)

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

# **loyalty_iiko_restore_customers_post**
> NetCustomerRestoreCustomersResponse loyalty_iiko_restore_customers_post(timeout=timeout, net_customer_restore_customers_request=net_customer_restore_customers_request)

Logical recovery of customers.

Removing deletion flags for customers.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.net_customer_restore_customers_request import NetCustomerRestoreCustomersRequest
from iikocloud_client.models.net_customer_restore_customers_response import NetCustomerRestoreCustomersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_restore_customers_request = iikocloud_client.NetCustomerRestoreCustomersRequest() # NetCustomerRestoreCustomersRequest |  (optional)

    try:
        # Logical recovery of customers.
        api_response = await api_instance.loyalty_iiko_restore_customers_post(timeout=timeout, net_customer_restore_customers_request=net_customer_restore_customers_request)
        print("The response of CustomersApi->loyalty_iiko_restore_customers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_restore_customers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_restore_customers_request** | [**NetCustomerRestoreCustomersRequest**](NetCustomerRestoreCustomersRequest.md)|  | [optional] 

### Return type

[**NetCustomerRestoreCustomersResponse**](NetCustomerRestoreCustomersResponse.md)

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

