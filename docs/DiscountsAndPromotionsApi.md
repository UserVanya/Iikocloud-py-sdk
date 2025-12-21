# iikocloud_client.DiscountsAndPromotionsApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loyalty_iiko_calculate_post**](DiscountsAndPromotionsApi.md#loyalty_iiko_calculate_post) | **POST** /loyalty/iiko/calculate | Calculate checkin.
[**loyalty_iiko_coupons_by_series_post**](DiscountsAndPromotionsApi.md#loyalty_iiko_coupons_by_series_post) | **POST** /loyalty/iiko/coupons/by_series | Get non-activated coupons
[**loyalty_iiko_coupons_info_post**](DiscountsAndPromotionsApi.md#loyalty_iiko_coupons_info_post) | **POST** /loyalty/iiko/coupons/info | Get coupon info.
[**loyalty_iiko_coupons_series_post**](DiscountsAndPromotionsApi.md#loyalty_iiko_coupons_series_post) | **POST** /loyalty/iiko/coupons/series | Get coupon series with non-activated coupons.
[**loyalty_iiko_manual_condition_post**](DiscountsAndPromotionsApi.md#loyalty_iiko_manual_condition_post) | **POST** /loyalty/iiko/manual_condition | Get manual conditions.
[**loyalty_iiko_program_post**](DiscountsAndPromotionsApi.md#loyalty_iiko_program_post) | **POST** /loyalty/iiko/program | Get programs.


# **loyalty_iiko_calculate_post**
> IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse loyalty_iiko_calculate_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request)

Calculate checkin.

Calculate discounts and other loyalty items for an order.

 > Restriction group: `Loyalty: order calculate`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest() # IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest |  (optional)

    try:
        # Calculate checkin.
        api_response = await api_instance.loyalty_iiko_calculate_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_calculate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_calculate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request** | [**IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest**](IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse**](IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse.md)

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

# **loyalty_iiko_coupons_by_series_post**
> IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponResponse loyalty_iiko_coupons_by_series_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request)

Get non-activated coupons

Get list of non-activated coupons.

 > Restriction group: `Loyalty: coupons`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest() # IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest |  (optional)

    try:
        # Get non-activated coupons
        api_response = await api_instance.loyalty_iiko_coupons_by_series_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_coupons_by_series_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_coupons_by_series_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request** | [**IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest**](IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponResponse**](IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponResponse.md)

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

# **loyalty_iiko_coupons_info_post**
> IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoResponse loyalty_iiko_coupons_info_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request)

Get coupon info.

Get information about the specified coupon.

 > Restriction group: `Loyalty: coupons`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest() # IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest |  (optional)

    try:
        # Get coupon info.
        api_response = await api_instance.loyalty_iiko_coupons_info_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_coupons_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_coupons_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request** | [**IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest**](IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoResponse**](IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoResponse.md)

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

# **loyalty_iiko_coupons_series_post**
> IikoNetServiceContractsApiIikoTransportLoyaltyResultSeriesWithNotActivatedCouponsResponse loyalty_iiko_coupons_series_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_series_with_not_activated_coupons_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_series_with_not_activated_coupons_request)

Get coupon series with non-activated coupons.

Get a list of coupon series in which there are not deleted and not activated coupons.

 > Restriction group: `Loyalty: coupons`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_series_with_not_activated_coupons_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultSeriesWithNotActivatedCouponsRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_series_with_not_activated_coupons_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultSeriesWithNotActivatedCouponsResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_loyalty_result_series_with_not_activated_coupons_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportLoyaltyResultSeriesWithNotActivatedCouponsRequest() # IikoNetServiceContractsApiIikoTransportLoyaltyResultSeriesWithNotActivatedCouponsRequest |  (optional)

    try:
        # Get coupon series with non-activated coupons.
        api_response = await api_instance.loyalty_iiko_coupons_series_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_loyalty_result_series_with_not_activated_coupons_request=iiko_net_service_contracts_api_iiko_transport_loyalty_result_series_with_not_activated_coupons_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_coupons_series_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_coupons_series_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_loyalty_result_series_with_not_activated_coupons_request** | [**IikoNetServiceContractsApiIikoTransportLoyaltyResultSeriesWithNotActivatedCouponsRequest**](IikoNetServiceContractsApiIikoTransportLoyaltyResultSeriesWithNotActivatedCouponsRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportLoyaltyResultSeriesWithNotActivatedCouponsResponse**](IikoNetServiceContractsApiIikoTransportLoyaltyResultSeriesWithNotActivatedCouponsResponse.md)

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

# **loyalty_iiko_manual_condition_post**
> IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse loyalty_iiko_manual_condition_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_common_get_by_organization_id_request=iiko_net_service_contracts_api_iiko_transport_common_get_by_organization_id_request)

Get manual conditions.

Get all organization's manual conditions.

 > Restriction group: `Loyalty: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_common_get_by_organization_id_request import IikoNetServiceContractsApiIikoTransportCommonGetByOrganizationIdRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_manual_conditions_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_common_get_by_organization_id_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCommonGetByOrganizationIdRequest() # IikoNetServiceContractsApiIikoTransportCommonGetByOrganizationIdRequest |  (optional)

    try:
        # Get manual conditions.
        api_response = await api_instance.loyalty_iiko_manual_condition_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_common_get_by_organization_id_request=iiko_net_service_contracts_api_iiko_transport_common_get_by_organization_id_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_manual_condition_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_manual_condition_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_common_get_by_organization_id_request** | [**IikoNetServiceContractsApiIikoTransportCommonGetByOrganizationIdRequest**](IikoNetServiceContractsApiIikoTransportCommonGetByOrganizationIdRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse**](IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse.md)

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

# **loyalty_iiko_program_post**
> IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse loyalty_iiko_program_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request=iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request)

Get programs.

Get all loyalty programs for organization.

 > Restriction group: `Loyalty: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request import IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_organization_get_programs_response import IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest() # IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest |  (optional)

    try:
        # Get programs.
        api_response = await api_instance.loyalty_iiko_program_post(authorization, timeout=timeout, iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request=iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_program_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_program_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_organization_get_programs_request** | [**IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest**](IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse**](IikoNetServiceContractsApiIikoTransportOrganizationGetProgramsResponse.md)

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

