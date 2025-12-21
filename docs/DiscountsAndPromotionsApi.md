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
> LoyaltyResultCalculateCheckinResponse loyalty_iiko_calculate_post(timeout=timeout, loyalty_result_calculate_checkin_request=loyalty_result_calculate_checkin_request)

Calculate checkin.

Calculate discounts and other loyalty items for an order.

 > Restriction group: `Loyalty: order calculate`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.loyalty_result_calculate_checkin_request import LoyaltyResultCalculateCheckinRequest
from iikocloud_client.models.loyalty_result_calculate_checkin_response import LoyaltyResultCalculateCheckinResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    loyalty_result_calculate_checkin_request = iikocloud_client.LoyaltyResultCalculateCheckinRequest() # LoyaltyResultCalculateCheckinRequest |  (optional)

    try:
        # Calculate checkin.
        api_response = await api_instance.loyalty_iiko_calculate_post(timeout=timeout, loyalty_result_calculate_checkin_request=loyalty_result_calculate_checkin_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_calculate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_calculate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **loyalty_result_calculate_checkin_request** | [**LoyaltyResultCalculateCheckinRequest**](LoyaltyResultCalculateCheckinRequest.md)|  | [optional] 

### Return type

[**LoyaltyResultCalculateCheckinResponse**](LoyaltyResultCalculateCheckinResponse.md)

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

# **loyalty_iiko_coupons_by_series_post**
> LoyaltyResultNotActivatedCouponResponse loyalty_iiko_coupons_by_series_post(timeout=timeout, loyalty_result_not_activated_coupon_request=loyalty_result_not_activated_coupon_request)

Get non-activated coupons

Get list of non-activated coupons.

 > Restriction group: `Loyalty: coupons`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.loyalty_result_not_activated_coupon_request import LoyaltyResultNotActivatedCouponRequest
from iikocloud_client.models.loyalty_result_not_activated_coupon_response import LoyaltyResultNotActivatedCouponResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    loyalty_result_not_activated_coupon_request = iikocloud_client.LoyaltyResultNotActivatedCouponRequest() # LoyaltyResultNotActivatedCouponRequest |  (optional)

    try:
        # Get non-activated coupons
        api_response = await api_instance.loyalty_iiko_coupons_by_series_post(timeout=timeout, loyalty_result_not_activated_coupon_request=loyalty_result_not_activated_coupon_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_coupons_by_series_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_coupons_by_series_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **loyalty_result_not_activated_coupon_request** | [**LoyaltyResultNotActivatedCouponRequest**](LoyaltyResultNotActivatedCouponRequest.md)|  | [optional] 

### Return type

[**LoyaltyResultNotActivatedCouponResponse**](LoyaltyResultNotActivatedCouponResponse.md)

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

# **loyalty_iiko_coupons_info_post**
> LoyaltyResultCouponInfoResponse loyalty_iiko_coupons_info_post(timeout=timeout, loyalty_result_coupon_info_request=loyalty_result_coupon_info_request)

Get coupon info.

Get information about the specified coupon.

 > Restriction group: `Loyalty: coupons`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.loyalty_result_coupon_info_request import LoyaltyResultCouponInfoRequest
from iikocloud_client.models.loyalty_result_coupon_info_response import LoyaltyResultCouponInfoResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    loyalty_result_coupon_info_request = iikocloud_client.LoyaltyResultCouponInfoRequest() # LoyaltyResultCouponInfoRequest |  (optional)

    try:
        # Get coupon info.
        api_response = await api_instance.loyalty_iiko_coupons_info_post(timeout=timeout, loyalty_result_coupon_info_request=loyalty_result_coupon_info_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_coupons_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_coupons_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **loyalty_result_coupon_info_request** | [**LoyaltyResultCouponInfoRequest**](LoyaltyResultCouponInfoRequest.md)|  | [optional] 

### Return type

[**LoyaltyResultCouponInfoResponse**](LoyaltyResultCouponInfoResponse.md)

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

# **loyalty_iiko_coupons_series_post**
> LoyaltyResultSeriesWithNotActivatedCouponsResponse loyalty_iiko_coupons_series_post(timeout=timeout, loyalty_result_series_with_not_activated_coupons_request=loyalty_result_series_with_not_activated_coupons_request)

Get coupon series with non-activated coupons.

Get a list of coupon series in which there are not deleted and not activated coupons.

 > Restriction group: `Loyalty: coupons`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.loyalty_result_series_with_not_activated_coupons_request import LoyaltyResultSeriesWithNotActivatedCouponsRequest
from iikocloud_client.models.loyalty_result_series_with_not_activated_coupons_response import LoyaltyResultSeriesWithNotActivatedCouponsResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    loyalty_result_series_with_not_activated_coupons_request = iikocloud_client.LoyaltyResultSeriesWithNotActivatedCouponsRequest() # LoyaltyResultSeriesWithNotActivatedCouponsRequest |  (optional)

    try:
        # Get coupon series with non-activated coupons.
        api_response = await api_instance.loyalty_iiko_coupons_series_post(timeout=timeout, loyalty_result_series_with_not_activated_coupons_request=loyalty_result_series_with_not_activated_coupons_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_coupons_series_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_coupons_series_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **loyalty_result_series_with_not_activated_coupons_request** | [**LoyaltyResultSeriesWithNotActivatedCouponsRequest**](LoyaltyResultSeriesWithNotActivatedCouponsRequest.md)|  | [optional] 

### Return type

[**LoyaltyResultSeriesWithNotActivatedCouponsResponse**](LoyaltyResultSeriesWithNotActivatedCouponsResponse.md)

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

# **loyalty_iiko_manual_condition_post**
> LoyaltyResultGetManualConditionsResponse loyalty_iiko_manual_condition_post(timeout=timeout, common_get_by_organization_id_request=common_get_by_organization_id_request)

Get manual conditions.

Get all organization's manual conditions.

 > Restriction group: `Loyalty: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.common_get_by_organization_id_request import CommonGetByOrganizationIdRequest
from iikocloud_client.models.loyalty_result_get_manual_conditions_response import LoyaltyResultGetManualConditionsResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    common_get_by_organization_id_request = iikocloud_client.CommonGetByOrganizationIdRequest() # CommonGetByOrganizationIdRequest |  (optional)

    try:
        # Get manual conditions.
        api_response = await api_instance.loyalty_iiko_manual_condition_post(timeout=timeout, common_get_by_organization_id_request=common_get_by_organization_id_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_manual_condition_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_manual_condition_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **common_get_by_organization_id_request** | [**CommonGetByOrganizationIdRequest**](CommonGetByOrganizationIdRequest.md)|  | [optional] 

### Return type

[**LoyaltyResultGetManualConditionsResponse**](LoyaltyResultGetManualConditionsResponse.md)

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

# **loyalty_iiko_program_post**
> OrganizationGetProgramsResponse loyalty_iiko_program_post(timeout=timeout, organization_get_programs_request=organization_get_programs_request)

Get programs.

Get all loyalty programs for organization.

 > Restriction group: `Loyalty: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.organization_get_programs_request import OrganizationGetProgramsRequest
from iikocloud_client.models.organization_get_programs_response import OrganizationGetProgramsResponse
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
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    organization_get_programs_request = iikocloud_client.OrganizationGetProgramsRequest() # OrganizationGetProgramsRequest |  (optional)

    try:
        # Get programs.
        api_response = await api_instance.loyalty_iiko_program_post(timeout=timeout, organization_get_programs_request=organization_get_programs_request)
        print("The response of DiscountsAndPromotionsApi->loyalty_iiko_program_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->loyalty_iiko_program_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **organization_get_programs_request** | [**OrganizationGetProgramsRequest**](OrganizationGetProgramsRequest.md)|  | [optional] 

### Return type

[**OrganizationGetProgramsResponse**](OrganizationGetProgramsResponse.md)

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

