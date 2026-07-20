# iikocloud_client.DiscountsAndPromotionsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_loyalty_checkin**](DiscountsAndPromotionsApi.md#calculate_loyalty_checkin) | **POST** /api/1/loyalty/iiko/calculate | Calculate checkin.
[**get_coupon_info**](DiscountsAndPromotionsApi.md#get_coupon_info) | **POST** /api/1/loyalty/iiko/coupons/info | Get coupon info.
[**get_coupon_series**](DiscountsAndPromotionsApi.md#get_coupon_series) | **POST** /api/1/loyalty/iiko/coupons/series | Get coupon series with non-activated coupons.
[**get_loyalty_manual_conditions**](DiscountsAndPromotionsApi.md#get_loyalty_manual_conditions) | **POST** /api/1/loyalty/iiko/manual_condition | Get manual conditions.
[**get_loyalty_programs**](DiscountsAndPromotionsApi.md#get_loyalty_programs) | **POST** /api/1/loyalty/iiko/program | Get programs.
[**get_non_activated_coupons_by_series**](DiscountsAndPromotionsApi.md#get_non_activated_coupons_by_series) | **POST** /api/1/loyalty/iiko/coupons/by_series | Get non-activated coupons


# **calculate_loyalty_checkin**
> CalculateCheckinResponse calculate_loyalty_checkin(timeout=timeout, calculate_checkin_request=calculate_checkin_request)

Calculate checkin.

Calculate discounts and other loyalty items for an order.

 > Restriction group: `Loyalty: order calculate`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.calculate_checkin_request import CalculateCheckinRequest
from iikocloud_client.models.calculate_checkin_response import CalculateCheckinResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    calculate_checkin_request = iikocloud_client.CalculateCheckinRequest() # CalculateCheckinRequest |  (optional)

    try:
        # Calculate checkin.
        api_response = await api_instance.calculate_loyalty_checkin(timeout=timeout, calculate_checkin_request=calculate_checkin_request)
        print("The response of DiscountsAndPromotionsApi->calculate_loyalty_checkin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->calculate_loyalty_checkin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **calculate_checkin_request** | [**CalculateCheckinRequest**](CalculateCheckinRequest.md)|  | [optional] 

### Return type

[**CalculateCheckinResponse**](CalculateCheckinResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_info**
> CouponInfoResponse get_coupon_info(timeout=timeout, coupon_info_request=coupon_info_request)

Get coupon info.

Get information about the specified coupon.

 > Restriction group: `Loyalty: coupons`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.coupon_info_request import CouponInfoRequest
from iikocloud_client.models.coupon_info_response import CouponInfoResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    coupon_info_request = iikocloud_client.CouponInfoRequest() # CouponInfoRequest |  (optional)

    try:
        # Get coupon info.
        api_response = await api_instance.get_coupon_info(timeout=timeout, coupon_info_request=coupon_info_request)
        print("The response of DiscountsAndPromotionsApi->get_coupon_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->get_coupon_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **coupon_info_request** | [**CouponInfoRequest**](CouponInfoRequest.md)|  | [optional] 

### Return type

[**CouponInfoResponse**](CouponInfoResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coupon_series**
> SeriesWithNotActivatedCouponsResponse get_coupon_series(timeout=timeout, series_with_not_activated_coupons_request=series_with_not_activated_coupons_request)

Get coupon series with non-activated coupons.

Get a list of coupon series in which there are not deleted and not activated coupons.

 > Restriction group: `Loyalty: coupons`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.series_with_not_activated_coupons_request import SeriesWithNotActivatedCouponsRequest
from iikocloud_client.models.series_with_not_activated_coupons_response import SeriesWithNotActivatedCouponsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    series_with_not_activated_coupons_request = iikocloud_client.SeriesWithNotActivatedCouponsRequest() # SeriesWithNotActivatedCouponsRequest |  (optional)

    try:
        # Get coupon series with non-activated coupons.
        api_response = await api_instance.get_coupon_series(timeout=timeout, series_with_not_activated_coupons_request=series_with_not_activated_coupons_request)
        print("The response of DiscountsAndPromotionsApi->get_coupon_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->get_coupon_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **series_with_not_activated_coupons_request** | [**SeriesWithNotActivatedCouponsRequest**](SeriesWithNotActivatedCouponsRequest.md)|  | [optional] 

### Return type

[**SeriesWithNotActivatedCouponsResponse**](SeriesWithNotActivatedCouponsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_manual_conditions**
> GetManualConditionsResponse get_loyalty_manual_conditions(timeout=timeout, get_by_organization_id_request=get_by_organization_id_request)

Get manual conditions.

Get all organization's manual conditions.

 > Restriction group: `Loyalty: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_by_organization_id_request import GetByOrganizationIdRequest
from iikocloud_client.models.get_manual_conditions_response import GetManualConditionsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_by_organization_id_request = iikocloud_client.GetByOrganizationIdRequest() # GetByOrganizationIdRequest |  (optional)

    try:
        # Get manual conditions.
        api_response = await api_instance.get_loyalty_manual_conditions(timeout=timeout, get_by_organization_id_request=get_by_organization_id_request)
        print("The response of DiscountsAndPromotionsApi->get_loyalty_manual_conditions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->get_loyalty_manual_conditions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_by_organization_id_request** | [**GetByOrganizationIdRequest**](GetByOrganizationIdRequest.md)|  | [optional] 

### Return type

[**GetManualConditionsResponse**](GetManualConditionsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_programs**
> GetProgramsResponse get_loyalty_programs(timeout=timeout, get_programs_request=get_programs_request)

Get programs.

Get all loyalty programs for organization.

 > Restriction group: `Loyalty: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_programs_request import GetProgramsRequest
from iikocloud_client.models.get_programs_response import GetProgramsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_programs_request = iikocloud_client.GetProgramsRequest() # GetProgramsRequest |  (optional)

    try:
        # Get programs.
        api_response = await api_instance.get_loyalty_programs(timeout=timeout, get_programs_request=get_programs_request)
        print("The response of DiscountsAndPromotionsApi->get_loyalty_programs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->get_loyalty_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_programs_request** | [**GetProgramsRequest**](GetProgramsRequest.md)|  | [optional] 

### Return type

[**GetProgramsResponse**](GetProgramsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_non_activated_coupons_by_series**
> NotActivatedCouponResponse get_non_activated_coupons_by_series(timeout=timeout, not_activated_coupon_request=not_activated_coupon_request)

Get non-activated coupons

Get list of non-activated coupons.

 > Restriction group: `Loyalty: coupons`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.not_activated_coupon_request import NotActivatedCouponRequest
from iikocloud_client.models.not_activated_coupon_response import NotActivatedCouponResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DiscountsAndPromotionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    not_activated_coupon_request = iikocloud_client.NotActivatedCouponRequest() # NotActivatedCouponRequest |  (optional)

    try:
        # Get non-activated coupons
        api_response = await api_instance.get_non_activated_coupons_by_series(timeout=timeout, not_activated_coupon_request=not_activated_coupon_request)
        print("The response of DiscountsAndPromotionsApi->get_non_activated_coupons_by_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsAndPromotionsApi->get_non_activated_coupons_by_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **not_activated_coupon_request** | [**NotActivatedCouponRequest**](NotActivatedCouponRequest.md)|  | [optional] 

### Return type

[**NotActivatedCouponResponse**](NotActivatedCouponResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

