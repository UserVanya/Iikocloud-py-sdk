# iikocloud_client.DiscountsAndPromotionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_loyalty_iiko_calculate_post**](DiscountsAndPromotionsApi.md#api1_loyalty_iiko_calculate_post) | **POST** /api/1/loyalty/iiko/calculate | Calculate checkin.
[**api1_loyalty_iiko_coupons_by_series_post**](DiscountsAndPromotionsApi.md#api1_loyalty_iiko_coupons_by_series_post) | **POST** /api/1/loyalty/iiko/coupons/by_series | Get non-activated coupons
[**api1_loyalty_iiko_coupons_info_post**](DiscountsAndPromotionsApi.md#api1_loyalty_iiko_coupons_info_post) | **POST** /api/1/loyalty/iiko/coupons/info | Get coupon info.
[**api1_loyalty_iiko_coupons_series_post**](DiscountsAndPromotionsApi.md#api1_loyalty_iiko_coupons_series_post) | **POST** /api/1/loyalty/iiko/coupons/series | Get coupon series with non-activated coupons.
[**api1_loyalty_iiko_manual_condition_post**](DiscountsAndPromotionsApi.md#api1_loyalty_iiko_manual_condition_post) | **POST** /api/1/loyalty/iiko/manual_condition | Get manual conditions.
[**api1_loyalty_iiko_program_post**](DiscountsAndPromotionsApi.md#api1_loyalty_iiko_program_post) | **POST** /api/1/loyalty/iiko/program | Get programs.


# **api1_loyalty_iiko_calculate_post**
> NetLoyaltyResultCalculateCheckinResponse api1_loyalty_iiko_calculate_post(authorization, timeout=timeout, net_loyalty_result_calculate_checkin_request=net_loyalty_result_calculate_checkin_request)

Calculate checkin.

Calculate discounts and other loyalty items for an order.

 > Restriction group: `Loyalty: order calculate`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.net_loyalty_result_calculate_checkin_request import NetLoyaltyResultCalculateCheckinRequest
from iikocloud_client.models.net_loyalty_result_calculate_checkin_response import NetLoyaltyResultCalculateCheckinResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_loyalty_result_calculate_checkin_request = iikocloud_client.NetLoyaltyResultCalculateCheckinRequest() # NetLoyaltyResultCalculateCheckinRequest |  (optional)

    try:
        # Calculate checkin.
        api_response = await api_instance.api1_loyalty_iiko_calculate_post(authorization, timeout=timeout, net_loyalty_result_calculate_checkin_request=net_loyalty_result_calculate_checkin_request)
        print("The response of DiscountsAndPromotionsApi->api1_loyalty_iiko_calculate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->api1_loyalty_iiko_calculate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_loyalty_result_calculate_checkin_request** | [**NetLoyaltyResultCalculateCheckinRequest**](NetLoyaltyResultCalculateCheckinRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultCalculateCheckinResponse**](NetLoyaltyResultCalculateCheckinResponse.md)

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

# **api1_loyalty_iiko_coupons_by_series_post**
> NetLoyaltyResultNotActivatedCouponResponse api1_loyalty_iiko_coupons_by_series_post(authorization, timeout=timeout, net_loyalty_result_not_activated_coupon_request=net_loyalty_result_not_activated_coupon_request)

Get non-activated coupons

Get list of non-activated coupons.

 > Restriction group: `Loyalty: coupons`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.net_loyalty_result_not_activated_coupon_request import NetLoyaltyResultNotActivatedCouponRequest
from iikocloud_client.models.net_loyalty_result_not_activated_coupon_response import NetLoyaltyResultNotActivatedCouponResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_loyalty_result_not_activated_coupon_request = iikocloud_client.NetLoyaltyResultNotActivatedCouponRequest() # NetLoyaltyResultNotActivatedCouponRequest |  (optional)

    try:
        # Get non-activated coupons
        api_response = await api_instance.api1_loyalty_iiko_coupons_by_series_post(authorization, timeout=timeout, net_loyalty_result_not_activated_coupon_request=net_loyalty_result_not_activated_coupon_request)
        print("The response of DiscountsAndPromotionsApi->api1_loyalty_iiko_coupons_by_series_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->api1_loyalty_iiko_coupons_by_series_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_loyalty_result_not_activated_coupon_request** | [**NetLoyaltyResultNotActivatedCouponRequest**](NetLoyaltyResultNotActivatedCouponRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultNotActivatedCouponResponse**](NetLoyaltyResultNotActivatedCouponResponse.md)

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

# **api1_loyalty_iiko_coupons_info_post**
> NetLoyaltyResultCouponInfoResponse api1_loyalty_iiko_coupons_info_post(authorization, timeout=timeout, net_loyalty_result_coupon_info_request=net_loyalty_result_coupon_info_request)

Get coupon info.

Get information about the specified coupon.

 > Restriction group: `Loyalty: coupons`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.net_loyalty_result_coupon_info_request import NetLoyaltyResultCouponInfoRequest
from iikocloud_client.models.net_loyalty_result_coupon_info_response import NetLoyaltyResultCouponInfoResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_loyalty_result_coupon_info_request = iikocloud_client.NetLoyaltyResultCouponInfoRequest() # NetLoyaltyResultCouponInfoRequest |  (optional)

    try:
        # Get coupon info.
        api_response = await api_instance.api1_loyalty_iiko_coupons_info_post(authorization, timeout=timeout, net_loyalty_result_coupon_info_request=net_loyalty_result_coupon_info_request)
        print("The response of DiscountsAndPromotionsApi->api1_loyalty_iiko_coupons_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->api1_loyalty_iiko_coupons_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_loyalty_result_coupon_info_request** | [**NetLoyaltyResultCouponInfoRequest**](NetLoyaltyResultCouponInfoRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultCouponInfoResponse**](NetLoyaltyResultCouponInfoResponse.md)

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

# **api1_loyalty_iiko_coupons_series_post**
> NetLoyaltyResultSeriesWithNotActivatedCouponsResponse api1_loyalty_iiko_coupons_series_post(authorization, timeout=timeout, net_loyalty_result_series_with_not_activated_coupons_request=net_loyalty_result_series_with_not_activated_coupons_request)

Get coupon series with non-activated coupons.

Get a list of coupon series in which there are not deleted and not activated coupons.

 > Restriction group: `Loyalty: coupons`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.net_loyalty_result_series_with_not_activated_coupons_request import NetLoyaltyResultSeriesWithNotActivatedCouponsRequest
from iikocloud_client.models.net_loyalty_result_series_with_not_activated_coupons_response import NetLoyaltyResultSeriesWithNotActivatedCouponsResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_loyalty_result_series_with_not_activated_coupons_request = iikocloud_client.NetLoyaltyResultSeriesWithNotActivatedCouponsRequest() # NetLoyaltyResultSeriesWithNotActivatedCouponsRequest |  (optional)

    try:
        # Get coupon series with non-activated coupons.
        api_response = await api_instance.api1_loyalty_iiko_coupons_series_post(authorization, timeout=timeout, net_loyalty_result_series_with_not_activated_coupons_request=net_loyalty_result_series_with_not_activated_coupons_request)
        print("The response of DiscountsAndPromotionsApi->api1_loyalty_iiko_coupons_series_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->api1_loyalty_iiko_coupons_series_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_loyalty_result_series_with_not_activated_coupons_request** | [**NetLoyaltyResultSeriesWithNotActivatedCouponsRequest**](NetLoyaltyResultSeriesWithNotActivatedCouponsRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultSeriesWithNotActivatedCouponsResponse**](NetLoyaltyResultSeriesWithNotActivatedCouponsResponse.md)

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

# **api1_loyalty_iiko_manual_condition_post**
> NetLoyaltyResultGetManualConditionsResponse api1_loyalty_iiko_manual_condition_post(authorization, timeout=timeout, net_common_get_by_organization_id_request=net_common_get_by_organization_id_request)

Get manual conditions.

Get all organization's manual conditions.

 > Restriction group: `Loyalty: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.net_common_get_by_organization_id_request import NetCommonGetByOrganizationIdRequest
from iikocloud_client.models.net_loyalty_result_get_manual_conditions_response import NetLoyaltyResultGetManualConditionsResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_common_get_by_organization_id_request = iikocloud_client.NetCommonGetByOrganizationIdRequest() # NetCommonGetByOrganizationIdRequest |  (optional)

    try:
        # Get manual conditions.
        api_response = await api_instance.api1_loyalty_iiko_manual_condition_post(authorization, timeout=timeout, net_common_get_by_organization_id_request=net_common_get_by_organization_id_request)
        print("The response of DiscountsAndPromotionsApi->api1_loyalty_iiko_manual_condition_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->api1_loyalty_iiko_manual_condition_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_common_get_by_organization_id_request** | [**NetCommonGetByOrganizationIdRequest**](NetCommonGetByOrganizationIdRequest.md)|  | [optional] 

### Return type

[**NetLoyaltyResultGetManualConditionsResponse**](NetLoyaltyResultGetManualConditionsResponse.md)

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

# **api1_loyalty_iiko_program_post**
> NetOrganizationGetProgramsResponse api1_loyalty_iiko_program_post(authorization, timeout=timeout, net_organization_get_programs_request=net_organization_get_programs_request)

Get programs.

Get all loyalty programs for organization.

 > Restriction group: `Loyalty: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.net_organization_get_programs_request import NetOrganizationGetProgramsRequest
from iikocloud_client.models.net_organization_get_programs_response import NetOrganizationGetProgramsResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_organization_get_programs_request = iikocloud_client.NetOrganizationGetProgramsRequest() # NetOrganizationGetProgramsRequest |  (optional)

    try:
        # Get programs.
        api_response = await api_instance.api1_loyalty_iiko_program_post(authorization, timeout=timeout, net_organization_get_programs_request=net_organization_get_programs_request)
        print("The response of DiscountsAndPromotionsApi->api1_loyalty_iiko_program_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->api1_loyalty_iiko_program_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_organization_get_programs_request** | [**NetOrganizationGetProgramsRequest**](NetOrganizationGetProgramsRequest.md)|  | [optional] 

### Return type

[**NetOrganizationGetProgramsResponse**](NetOrganizationGetProgramsResponse.md)

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

