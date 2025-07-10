# iiko_cloud_client.MenuApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_combo_calculate_post**](MenuApi.md#api1_combo_calculate_post) | **POST** /api/1/combo/calculate | Calculate combo price
[**api1_combo_post**](MenuApi.md#api1_combo_post) | **POST** /api/1/combo | Get combos info
[**api1_nomenclature_post**](MenuApi.md#api1_nomenclature_post) | **POST** /api/1/nomenclature | Menu.
[**api1_stop_lists_add_post**](MenuApi.md#api1_stop_lists_add_post) | **POST** /api/1/stop_lists/add | Add items to out-of-stock list.  (You should have extra rights to use this method).
[**api1_stop_lists_check_post**](MenuApi.md#api1_stop_lists_check_post) | **POST** /api/1/stop_lists/check | Check items in out-of-stock list.
[**api1_stop_lists_clear_post**](MenuApi.md#api1_stop_lists_clear_post) | **POST** /api/1/stop_lists/clear | Clear out-of-stock list.  (You should have extra rights to use this method).
[**api1_stop_lists_post**](MenuApi.md#api1_stop_lists_post) | **POST** /api/1/stop_lists | Out-of-stock items.
[**api1_stop_lists_remove_post**](MenuApi.md#api1_stop_lists_remove_post) | **POST** /api/1/stop_lists/remove | Remove items from out-of-stock list.  (You should have extra rights to use this method).
[**api2_menu_by_id_post**](MenuApi.md#api2_menu_by_id_post) | **POST** /api/2/menu/by_id | Retrieve external menu by ID.
[**api2_menu_post**](MenuApi.md#api2_menu_post) | **POST** /api/2/menu | External menus with price categories.


# **api1_combo_calculate_post**
> NetLoyaltyResultCalculateComboPriceResponse api1_combo_calculate_post(authorization, timeout=timeout, net_loyalty_result_calculate_combo_price_request=net_loyalty_result_calculate_combo_price_request)

Calculate combo price

Make combo price calculation.

 > Restriction group: `Loyalty: order calculate`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.net_loyalty_result_calculate_combo_price_request import NetLoyaltyResultCalculateComboPriceRequest
from iiko_cloud_client.models.net_loyalty_result_calculate_combo_price_response import NetLoyaltyResultCalculateComboPriceResponse
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_loyalty_result_calculate_combo_price_request = iiko_cloud_client.NetLoyaltyResultCalculateComboPriceRequest() # NetLoyaltyResultCalculateComboPriceRequest |  (optional)

    try:
        # Calculate combo price
        api_response = await api_instance.api1_combo_calculate_post(authorization, timeout=timeout, net_loyalty_result_calculate_combo_price_request=net_loyalty_result_calculate_combo_price_request)
        print("The response of MenuApi->api1_combo_calculate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api1_combo_calculate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_loyalty_result_calculate_combo_price_request** | [**NetLoyaltyResultCalculateComboPriceRequest**](NetLoyaltyResultCalculateComboPriceRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultCalculateComboPriceResponse**](NetLoyaltyResultCalculateComboPriceResponse.md)

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

# **api1_combo_post**
> NetLoyaltyResultGetCombosInfoResponse api1_combo_post(authorization, timeout=timeout, net_loyalty_result_get_combos_info_request=net_loyalty_result_get_combos_info_request)

Get combos info

Get all organization's combos.

 > Restriction group: `Data: menu`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.net_loyalty_result_get_combos_info_request import NetLoyaltyResultGetCombosInfoRequest
from iiko_cloud_client.models.net_loyalty_result_get_combos_info_response import NetLoyaltyResultGetCombosInfoResponse
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_loyalty_result_get_combos_info_request = iiko_cloud_client.NetLoyaltyResultGetCombosInfoRequest() # NetLoyaltyResultGetCombosInfoRequest |  (optional)

    try:
        # Get combos info
        api_response = await api_instance.api1_combo_post(authorization, timeout=timeout, net_loyalty_result_get_combos_info_request=net_loyalty_result_get_combos_info_request)
        print("The response of MenuApi->api1_combo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api1_combo_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_loyalty_result_get_combos_info_request** | [**NetLoyaltyResultGetCombosInfoRequest**](NetLoyaltyResultGetCombosInfoRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultGetCombosInfoResponse**](NetLoyaltyResultGetCombosInfoResponse.md)

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

# **api1_nomenclature_post**
> TransportNomenclatureNomenclatureResponse api1_nomenclature_post(authorization, timeout=timeout, transport_nomenclature_nomenclature_request=transport_nomenclature_nomenclature_request)

Menu.

> Sourced from RMS Data Exchange Export menu.

 > Restriction group: `Data: menu`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_nomenclature_nomenclature_request import TransportNomenclatureNomenclatureRequest
from iiko_cloud_client.models.transport_nomenclature_nomenclature_response import TransportNomenclatureNomenclatureResponse
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_nomenclature_nomenclature_request = iiko_cloud_client.TransportNomenclatureNomenclatureRequest() # TransportNomenclatureNomenclatureRequest |  (optional)

    try:
        # Menu.
        api_response = await api_instance.api1_nomenclature_post(authorization, timeout=timeout, transport_nomenclature_nomenclature_request=transport_nomenclature_nomenclature_request)
        print("The response of MenuApi->api1_nomenclature_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api1_nomenclature_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_nomenclature_nomenclature_request** | [**TransportNomenclatureNomenclatureRequest**](TransportNomenclatureNomenclatureRequest.md)|  | [optional] 

### Return type

[**TransportNomenclatureNomenclatureResponse**](TransportNomenclatureNomenclatureResponse.md)

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

# **api1_stop_lists_add_post**
> TransportCommonCorrelationIdResponse api1_stop_lists_add_post(authorization, timeout=timeout, transport_stop_lists_add_products_to_stop_list_request=transport_stop_lists_add_products_to_stop_list_request)

Add items to out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_stop_lists_add_products_to_stop_list_request import TransportStopListsAddProductsToStopListRequest
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_add_products_to_stop_list_request = iiko_cloud_client.TransportStopListsAddProductsToStopListRequest() # TransportStopListsAddProductsToStopListRequest |  (optional)

    try:
        # Add items to out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.api1_stop_lists_add_post(authorization, timeout=timeout, transport_stop_lists_add_products_to_stop_list_request=transport_stop_lists_add_products_to_stop_list_request)
        print("The response of MenuApi->api1_stop_lists_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api1_stop_lists_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_add_products_to_stop_list_request** | [**TransportStopListsAddProductsToStopListRequest**](TransportStopListsAddProductsToStopListRequest.md)|  | [optional] 

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

# **api1_stop_lists_check_post**
> TransportStopListsCheckStopListResponse api1_stop_lists_check_post(authorization, timeout=timeout, transport_stop_lists_check_stop_list_request=transport_stop_lists_check_stop_list_request)

Check items in out-of-stock list.



 > Restriction group: `Orders: creating`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_stop_lists_check_stop_list_request import TransportStopListsCheckStopListRequest
from iiko_cloud_client.models.transport_stop_lists_check_stop_list_response import TransportStopListsCheckStopListResponse
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_check_stop_list_request = iiko_cloud_client.TransportStopListsCheckStopListRequest() # TransportStopListsCheckStopListRequest |  (optional)

    try:
        # Check items in out-of-stock list.
        api_response = await api_instance.api1_stop_lists_check_post(authorization, timeout=timeout, transport_stop_lists_check_stop_list_request=transport_stop_lists_check_stop_list_request)
        print("The response of MenuApi->api1_stop_lists_check_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api1_stop_lists_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_check_stop_list_request** | [**TransportStopListsCheckStopListRequest**](TransportStopListsCheckStopListRequest.md)|  | [optional] 

### Return type

[**TransportStopListsCheckStopListResponse**](TransportStopListsCheckStopListResponse.md)

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

# **api1_stop_lists_clear_post**
> TransportCommonCorrelationIdResponse api1_stop_lists_clear_post(authorization, timeout=timeout, transport_stop_lists_clear_stop_list_request=transport_stop_lists_clear_stop_list_request)

Clear out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_stop_lists_clear_stop_list_request import TransportStopListsClearStopListRequest
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_clear_stop_list_request = iiko_cloud_client.TransportStopListsClearStopListRequest() # TransportStopListsClearStopListRequest |  (optional)

    try:
        # Clear out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.api1_stop_lists_clear_post(authorization, timeout=timeout, transport_stop_lists_clear_stop_list_request=transport_stop_lists_clear_stop_list_request)
        print("The response of MenuApi->api1_stop_lists_clear_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api1_stop_lists_clear_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_clear_stop_list_request** | [**TransportStopListsClearStopListRequest**](TransportStopListsClearStopListRequest.md)|  | [optional] 

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

# **api1_stop_lists_post**
> TransportStopListsStopListsResponse api1_stop_lists_post(authorization, timeout=timeout, transport_stop_lists_stop_lists_request=transport_stop_lists_stop_lists_request)

Out-of-stock items.



 > Restriction group: `Data: stoplists`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_stop_lists_stop_lists_request import TransportStopListsStopListsRequest
from iiko_cloud_client.models.transport_stop_lists_stop_lists_response import TransportStopListsStopListsResponse
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_stop_lists_request = iiko_cloud_client.TransportStopListsStopListsRequest() # TransportStopListsStopListsRequest |  (optional)

    try:
        # Out-of-stock items.
        api_response = await api_instance.api1_stop_lists_post(authorization, timeout=timeout, transport_stop_lists_stop_lists_request=transport_stop_lists_stop_lists_request)
        print("The response of MenuApi->api1_stop_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api1_stop_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_stop_lists_request** | [**TransportStopListsStopListsRequest**](TransportStopListsStopListsRequest.md)|  | [optional] 

### Return type

[**TransportStopListsStopListsResponse**](TransportStopListsStopListsResponse.md)

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

# **api1_stop_lists_remove_post**
> TransportCommonCorrelationIdResponse api1_stop_lists_remove_post(authorization, timeout=timeout, transport_stop_lists_remove_products_from_stop_list_request=transport_stop_lists_remove_products_from_stop_list_request)

Remove items from out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iiko_cloud_client.models.transport_stop_lists_remove_products_from_stop_list_request import TransportStopListsRemoveProductsFromStopListRequest
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_stop_lists_remove_products_from_stop_list_request = iiko_cloud_client.TransportStopListsRemoveProductsFromStopListRequest() # TransportStopListsRemoveProductsFromStopListRequest |  (optional)

    try:
        # Remove items from out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.api1_stop_lists_remove_post(authorization, timeout=timeout, transport_stop_lists_remove_products_from_stop_list_request=transport_stop_lists_remove_products_from_stop_list_request)
        print("The response of MenuApi->api1_stop_lists_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api1_stop_lists_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_stop_lists_remove_products_from_stop_list_request** | [**TransportStopListsRemoveProductsFromStopListRequest**](TransportStopListsRemoveProductsFromStopListRequest.md)|  | [optional] 

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

# **api2_menu_by_id_post**
> ExternalMenuPreset api2_menu_by_id_post(authorization, timeout=timeout, transport_nomenclature_menu_request=transport_nomenclature_menu_request)

Retrieve external menu by ID.

> Sourced from Web External menu.

 > Restriction group: `Data: menu`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.external_menu_preset import ExternalMenuPreset
from iiko_cloud_client.models.transport_nomenclature_menu_request import TransportNomenclatureMenuRequest
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_nomenclature_menu_request = iiko_cloud_client.TransportNomenclatureMenuRequest() # TransportNomenclatureMenuRequest |  (optional)

    try:
        # Retrieve external menu by ID.
        api_response = await api_instance.api2_menu_by_id_post(authorization, timeout=timeout, transport_nomenclature_menu_request=transport_nomenclature_menu_request)
        print("The response of MenuApi->api2_menu_by_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api2_menu_by_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_nomenclature_menu_request** | [**TransportNomenclatureMenuRequest**](TransportNomenclatureMenuRequest.md)|  | [optional] 

### Return type

[**ExternalMenuPreset**](ExternalMenuPreset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api2_menu_post**
> TransportNomenclatureMenusDataResponse api2_menu_post(authorization, timeout=timeout)

External menus with price categories.



 > Restriction group: `Data: menu`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.transport_nomenclature_menus_data_response import TransportNomenclatureMenusDataResponse
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
    api_instance = iiko_cloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # External menus with price categories.
        api_response = await api_instance.api2_menu_post(authorization, timeout=timeout)
        print("The response of MenuApi->api2_menu_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->api2_menu_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**TransportNomenclatureMenusDataResponse**](TransportNomenclatureMenusDataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

