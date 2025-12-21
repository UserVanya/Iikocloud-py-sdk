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
> object loyalty_iiko_customer_card_add_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request=iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request)

Add card.

Add new card for customer.

 > Restriction group: `Guests: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request import IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest() # IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest |  (optional)

    try:
        # Add card.
        api_response = await api_instance.loyalty_iiko_customer_card_add_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request=iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request)
        print("The response of CustomersApi->loyalty_iiko_customer_card_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_card_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_add_magnet_card_request** | [**IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest**](IikoNetServiceContractsApiIikoTransportCustomerAddMagnetCardRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_card_remove_post**
> object loyalty_iiko_customer_card_remove_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_delete_magnet_card_request=iiko_net_service_contracts_api_iiko_transport_customer_delete_magnet_card_request)

Delete card.

Delete existing card for customer.

 > Restriction group: `Guests: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_delete_magnet_card_request import IikoNetServiceContractsApiIikoTransportCustomerDeleteMagnetCardRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_delete_magnet_card_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerDeleteMagnetCardRequest() # IikoNetServiceContractsApiIikoTransportCustomerDeleteMagnetCardRequest |  (optional)

    try:
        # Delete card.
        api_response = await api_instance.loyalty_iiko_customer_card_remove_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_delete_magnet_card_request=iiko_net_service_contracts_api_iiko_transport_customer_delete_magnet_card_request)
        print("The response of CustomersApi->loyalty_iiko_customer_card_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_card_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_delete_magnet_card_request** | [**IikoNetServiceContractsApiIikoTransportCustomerDeleteMagnetCardRequest**](IikoNetServiceContractsApiIikoTransportCustomerDeleteMagnetCardRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_create_or_update_post**
> IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerResponse loyalty_iiko_customer_create_or_update_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request=iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request)

Create or update customer.

Create or update customer info by id or phone or card track.

 > Restriction group: `Guests: creating`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request import IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_response import IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest() # IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest |  (optional)

    try:
        # Create or update customer.
        api_response = await api_instance.loyalty_iiko_customer_create_or_update_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request=iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request)
        print("The response of CustomersApi->loyalty_iiko_customer_create_or_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_create_or_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_create_or_update_customer_request** | [**IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest**](IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerResponse**](IikoNetServiceContractsApiIikoTransportCustomerCreateOrUpdateCustomerResponse.md)

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

# **loyalty_iiko_customer_info_post**
> IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoResponse loyalty_iiko_customer_info_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request=iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request)

Get customer info.

Get customer info by specified criterion.

 > Restriction group: `Guests: info`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request import IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_response import IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest() # IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest |  (optional)

    try:
        # Get customer info.
        api_response = await api_instance.loyalty_iiko_customer_info_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request=iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request)
        print("The response of CustomersApi->loyalty_iiko_customer_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_get_customer_info_request** | [**IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest**](IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoResponse**](IikoNetServiceContractsApiIikoTransportCustomerGetCustomerInfoResponse.md)

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

# **loyalty_iiko_customer_program_add_post**
> IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramResponse loyalty_iiko_customer_program_add_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request=iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request)

Add customer to program.

Add new customer for program.

 > Restriction group: `Guests: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request import IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_response import IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest() # IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest |  (optional)

    try:
        # Add customer to program.
        api_response = await api_instance.loyalty_iiko_customer_program_add_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request=iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request)
        print("The response of CustomersApi->loyalty_iiko_customer_program_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_program_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_add_customer_to_program_request** | [**IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest**](IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramResponse**](IikoNetServiceContractsApiIikoTransportCustomerAddCustomerToProgramResponse.md)

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

# **loyalty_iiko_customer_wallet_cancel_hold_post**
> object loyalty_iiko_customer_wallet_cancel_hold_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request=iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request)

Cancel hold money.

Cancel holding transaction that created earlier.

 > Restriction group: `Loyalty: wallets`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request import IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest() # IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest |  (optional)

    try:
        # Cancel hold money.
        api_response = await api_instance.loyalty_iiko_customer_wallet_cancel_hold_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request=iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_cancel_hold_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_cancel_hold_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_cancel_hold_money_request** | [**IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest**](IikoNetServiceContractsApiIikoTransportCustomerCancelHoldMoneyRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_wallet_chargeoff_post**
> object loyalty_iiko_customer_wallet_chargeoff_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request=iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request)

Withdraw balance.

Withdraw customer balance.

 > Restriction group: `Loyalty: wallets`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request import IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest() # IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest |  (optional)

    try:
        # Withdraw balance.
        api_response = await api_instance.loyalty_iiko_customer_wallet_chargeoff_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request=iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_chargeoff_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_chargeoff_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request** | [**IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest**](IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_wallet_hold_post**
> IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse loyalty_iiko_customer_wallet_hold_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request=iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request)

Hold money.

Hold customer's money in loyalty program. Payment will be process on POS during processing of an order.

 > Restriction group: `Loyalty: wallets`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request import IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_hold_money_response import IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest() # IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest |  (optional)

    try:
        # Hold money.
        api_response = await api_instance.loyalty_iiko_customer_wallet_hold_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request=iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_hold_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_hold_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_hold_money_request** | [**IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest**](IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse**](IikoNetServiceContractsApiIikoTransportCustomerHoldMoneyResponse.md)

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

# **loyalty_iiko_customer_wallet_topup_post**
> object loyalty_iiko_customer_wallet_topup_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request=iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request)

Refill balance.

Refill customer balance.

 > Restriction group: `Loyalty: wallets`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request import IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest() # IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest |  (optional)

    try:
        # Refill balance.
        api_response = await api_instance.loyalty_iiko_customer_wallet_topup_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request=iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request)
        print("The response of CustomersApi->loyalty_iiko_customer_wallet_topup_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_customer_wallet_topup_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_change_user_balance_request** | [**IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest**](IikoNetServiceContractsApiIikoTransportCustomerChangeUserBalanceRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_delete_customers_post**
> IikoNetServiceContractsApiIikoTransportCustomerDeleteCustomersResponse loyalty_iiko_delete_customers_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_delete_customers_request=iiko_net_service_contracts_api_iiko_transport_customer_delete_customers_request)

Logical deletion of customers.

Mark customers as deleted.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_delete_customers_request import IikoNetServiceContractsApiIikoTransportCustomerDeleteCustomersRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_delete_customers_response import IikoNetServiceContractsApiIikoTransportCustomerDeleteCustomersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_delete_customers_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerDeleteCustomersRequest() # IikoNetServiceContractsApiIikoTransportCustomerDeleteCustomersRequest |  (optional)

    try:
        # Logical deletion of customers.
        api_response = await api_instance.loyalty_iiko_delete_customers_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_delete_customers_request=iiko_net_service_contracts_api_iiko_transport_customer_delete_customers_request)
        print("The response of CustomersApi->loyalty_iiko_delete_customers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_delete_customers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_delete_customers_request** | [**IikoNetServiceContractsApiIikoTransportCustomerDeleteCustomersRequest**](IikoNetServiceContractsApiIikoTransportCustomerDeleteCustomersRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportCustomerDeleteCustomersResponse**](IikoNetServiceContractsApiIikoTransportCustomerDeleteCustomersResponse.md)

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

# **loyalty_iiko_get_counters_post**
> IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersResponse loyalty_iiko_get_counters_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request)

Get counters.

Get customer orders count and sum for different period.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest() # IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest |  (optional)

    try:
        # Get counters.
        api_response = await api_instance.loyalty_iiko_get_counters_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request)
        print("The response of CustomersApi->loyalty_iiko_get_counters_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_get_counters_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_counters_request** | [**IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest**](IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersResponse**](IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCountersResponse.md)

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

# **loyalty_iiko_restore_customers_post**
> IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse loyalty_iiko_restore_customers_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request=iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request)

Logical recovery of customers.

Removing deletion flags for customers.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request import IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_response import IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse
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
    api_instance = iikocloud_client.CustomersApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest() # IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest |  (optional)

    try:
        # Logical recovery of customers.
        api_response = await api_instance.loyalty_iiko_restore_customers_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request=iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request)
        print("The response of CustomersApi->loyalty_iiko_restore_customers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->loyalty_iiko_restore_customers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_restore_customers_request** | [**IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest**](IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse**](IikoNetServiceContractsApiIikoTransportCustomerRestoreCustomersResponse.md)

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

