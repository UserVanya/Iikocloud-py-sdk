# iikocloud_client.MenuApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api2_menu_by_id_post**](MenuApi.md#api2_menu_by_id_post) | **POST** /api/2/menu/by_id | Retrieve external menu by ID.
[**api2_menu_post**](MenuApi.md#api2_menu_post) | **POST** /api/2/menu | External menus with price categories.
[**combo_calculate_post**](MenuApi.md#combo_calculate_post) | **POST** /combo/calculate | Calculate combo price
[**combo_post**](MenuApi.md#combo_post) | **POST** /combo | Get combos info
[**nomenclature_post**](MenuApi.md#nomenclature_post) | **POST** /nomenclature | Menu.
[**stop_lists_add_post**](MenuApi.md#stop_lists_add_post) | **POST** /stop_lists/add | Add items to out-of-stock list.  (You should have extra rights to use this method).
[**stop_lists_check_post**](MenuApi.md#stop_lists_check_post) | **POST** /stop_lists/check | Check items in out-of-stock list.
[**stop_lists_clear_post**](MenuApi.md#stop_lists_clear_post) | **POST** /stop_lists/clear | Clear out-of-stock list.  (You should have extra rights to use this method).
[**stop_lists_post**](MenuApi.md#stop_lists_post) | **POST** /stop_lists | Out-of-stock items.
[**stop_lists_remove_post**](MenuApi.md#stop_lists_remove_post) | **POST** /stop_lists/remove | Remove items from out-of-stock list.  (You should have extra rights to use this method).


# **api2_menu_by_id_post**
> Api2MenuByIdPost200Response api2_menu_by_id_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_nomenclature_menu_request=iiko_transport_public_api_contracts_nomenclature_menu_request)

Retrieve external menu by ID.

> Sourced from Web External menu.

 > Restriction group: `Data: menu`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.api2_menu_by_id_post200_response import Api2MenuByIdPost200Response
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_menu_request import IikoTransportPublicApiContractsNomenclatureMenuRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_nomenclature_menu_request = {"externalMenuId":"15#3","organizationIds":["706e5f4a-3efa-49f0-8f1c-15a6c1603e1f"],"version":2} # IikoTransportPublicApiContractsNomenclatureMenuRequest |  (optional)

    try:
        # Retrieve external menu by ID.
        api_response = await api_instance.api2_menu_by_id_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_nomenclature_menu_request=iiko_transport_public_api_contracts_nomenclature_menu_request)
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
 **iiko_transport_public_api_contracts_nomenclature_menu_request** | [**IikoTransportPublicApiContractsNomenclatureMenuRequest**](IikoTransportPublicApiContractsNomenclatureMenuRequest.md)|  | [optional] 

### Return type

[**Api2MenuByIdPost200Response**](Api2MenuByIdPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api2_menu_post**
> IikoTransportPublicApiContractsNomenclatureMenusDataResponse api2_menu_post(authorization, timeout=timeout)

External menus with price categories.



 > Restriction group: `Data: menu`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_menus_data_response import IikoTransportPublicApiContractsNomenclatureMenusDataResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
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

[**IikoTransportPublicApiContractsNomenclatureMenusDataResponse**](IikoTransportPublicApiContractsNomenclatureMenusDataResponse.md)

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

# **combo_calculate_post**
> IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse combo_calculate_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request)

Calculate combo price

Make combo price calculation.

 > Restriction group: `Loyalty: order calculate`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest() # IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest |  (optional)

    try:
        # Calculate combo price
        api_response = await api_instance.combo_calculate_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request)
        print("The response of MenuApi->combo_calculate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->combo_calculate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_combo_price_request** | [**IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest**](IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse**](IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateComboPriceResponse.md)

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

# **combo_post**
> IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse combo_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_request)

Get combos info

Get all organization's combos.

 > Restriction group: `Data: menu`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoRequest() # IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoRequest |  (optional)

    try:
        # Get combos info
        api_response = await api_instance.combo_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_request)
        print("The response of MenuApi->combo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->combo_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_request** | [**IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoRequest**](IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse**](IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse.md)

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

# **nomenclature_post**
> IikoTransportPublicApiContractsNomenclatureNomenclatureResponse nomenclature_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_nomenclature_nomenclature_request=iiko_transport_public_api_contracts_nomenclature_nomenclature_request)

Menu.

> Sourced from RMS Data Exchange Export menu.

 > Restriction group: `Data: menu`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_nomenclature_request import IikoTransportPublicApiContractsNomenclatureNomenclatureRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_nomenclature_response import IikoTransportPublicApiContractsNomenclatureNomenclatureResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_nomenclature_nomenclature_request = iikocloud_client.IikoTransportPublicApiContractsNomenclatureNomenclatureRequest() # IikoTransportPublicApiContractsNomenclatureNomenclatureRequest |  (optional)

    try:
        # Menu.
        api_response = await api_instance.nomenclature_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_nomenclature_nomenclature_request=iiko_transport_public_api_contracts_nomenclature_nomenclature_request)
        print("The response of MenuApi->nomenclature_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->nomenclature_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_nomenclature_nomenclature_request** | [**IikoTransportPublicApiContractsNomenclatureNomenclatureRequest**](IikoTransportPublicApiContractsNomenclatureNomenclatureRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsNomenclatureNomenclatureResponse**](IikoTransportPublicApiContractsNomenclatureNomenclatureResponse.md)

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

# **stop_lists_add_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse stop_lists_add_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request=iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request)

Add items to out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request import IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request = iikocloud_client.IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest() # IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest |  (optional)

    try:
        # Add items to out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.stop_lists_add_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request=iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request)
        print("The response of MenuApi->stop_lists_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request** | [**IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest**](IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest.md)|  | [optional] 

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

# **stop_lists_check_post**
> IikoTransportPublicApiContractsStopListsCheckStopListResponse stop_lists_check_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_check_stop_list_request=iiko_transport_public_api_contracts_stop_lists_check_stop_list_request)

Check items in out-of-stock list.



 > Restriction group: `Orders: creating`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_check_stop_list_request import IikoTransportPublicApiContractsStopListsCheckStopListRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_check_stop_list_response import IikoTransportPublicApiContractsStopListsCheckStopListResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_stop_lists_check_stop_list_request = iikocloud_client.IikoTransportPublicApiContractsStopListsCheckStopListRequest() # IikoTransportPublicApiContractsStopListsCheckStopListRequest |  (optional)

    try:
        # Check items in out-of-stock list.
        api_response = await api_instance.stop_lists_check_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_check_stop_list_request=iiko_transport_public_api_contracts_stop_lists_check_stop_list_request)
        print("The response of MenuApi->stop_lists_check_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_stop_lists_check_stop_list_request** | [**IikoTransportPublicApiContractsStopListsCheckStopListRequest**](IikoTransportPublicApiContractsStopListsCheckStopListRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsStopListsCheckStopListResponse**](IikoTransportPublicApiContractsStopListsCheckStopListResponse.md)

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

# **stop_lists_clear_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse stop_lists_clear_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request=iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request)

Clear out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request import IikoTransportPublicApiContractsStopListsClearStopListRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request = iikocloud_client.IikoTransportPublicApiContractsStopListsClearStopListRequest() # IikoTransportPublicApiContractsStopListsClearStopListRequest |  (optional)

    try:
        # Clear out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.stop_lists_clear_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request=iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request)
        print("The response of MenuApi->stop_lists_clear_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_clear_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_stop_lists_clear_stop_list_request** | [**IikoTransportPublicApiContractsStopListsClearStopListRequest**](IikoTransportPublicApiContractsStopListsClearStopListRequest.md)|  | [optional] 

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

# **stop_lists_post**
> IikoTransportPublicApiContractsStopListsStopListsResponse stop_lists_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_stop_lists_request=iiko_transport_public_api_contracts_stop_lists_stop_lists_request)

Out-of-stock items.



 > Restriction group: `Data: stoplists`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_stop_lists_request import IikoTransportPublicApiContractsStopListsStopListsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_stop_lists_response import IikoTransportPublicApiContractsStopListsStopListsResponse
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
    api_instance = iikocloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_stop_lists_stop_lists_request = iikocloud_client.IikoTransportPublicApiContractsStopListsStopListsRequest() # IikoTransportPublicApiContractsStopListsStopListsRequest |  (optional)

    try:
        # Out-of-stock items.
        api_response = await api_instance.stop_lists_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_stop_lists_request=iiko_transport_public_api_contracts_stop_lists_stop_lists_request)
        print("The response of MenuApi->stop_lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_stop_lists_stop_lists_request** | [**IikoTransportPublicApiContractsStopListsStopListsRequest**](IikoTransportPublicApiContractsStopListsStopListsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsStopListsStopListsResponse**](IikoTransportPublicApiContractsStopListsStopListsResponse.md)

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

# **stop_lists_remove_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse stop_lists_remove_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request=iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request)

Remove items from out-of-stock list.  (You should have extra rights to use this method).



 > Allowed from version `8.6.1`.

 > Restriction group: `Data: changing stoplists`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request import IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest
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
    api_instance = iikocloud_client.MenuApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request = iikocloud_client.IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest() # IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest |  (optional)

    try:
        # Remove items from out-of-stock list.  (You should have extra rights to use this method).
        api_response = await api_instance.stop_lists_remove_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request=iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request)
        print("The response of MenuApi->stop_lists_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MenuApi->stop_lists_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request** | [**IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest**](IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest.md)|  | [optional] 

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

