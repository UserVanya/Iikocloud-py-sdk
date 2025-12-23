# OrganizationsExtendedOrganizationInfo

Organization details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country. | 
**restaurant_address** | **str** | Restaurant address. | 
**latitude** | **float** | Latitude. | 
**longitude** | **float** | Longitude. | 
**use_uae_addressing_system** | **bool** | Regional setting \&quot;Use the UAE Addressing System\&quot;. | 
**version** | **str** | RMS version. | 
**currency_iso_name** | **str** | ISO currency code (for example: RUB, USD, EUR). | 
**currency_minimum_denomination** | **float** | Value rounding of position. | 
**country_phone_code** | **str** | Country dialing code. | 
**marketing_source_required_in_delivery** | **bool** | Require mandatory marketing source input when creating a delivery. | 
**default_delivery_city_id** | **str** | Default delivery city. | 
**delivery_city_ids** | **List[str]** | Delivery cities. | 
**delivery_service_type** | [**OrganizationsDeliverySettingsServiceType**](OrganizationsDeliverySettingsServiceType.md) | Delivery type. | 
**delivery_order_payment_settings** | [**OrganizationsDeliveryOrderPaymentSettings**](OrganizationsDeliveryOrderPaymentSettings.md) | Delivery order payment settings. | [optional] 
**default_call_center_payment_type_id** | **str** | Default payment type for CallCenter. | 
**order_item_comment_enabled** | **bool** | Allow text comments for order items (in all restaurant sections). | 
**inn** | **str** | Restaurant&#x60;s INN (Taxpayer Identification Number). | 
**address_format_type** | [**OrganizationsAddressFormatType**](OrganizationsAddressFormatType.md) | Address format type. | 
**is_confirmation_enabled** | **bool** | Determines whether to use delivery confirmation. | 
**confirm_allowed_interval_in_minutes** | **int** | Confirm orders time interval. | 
**is_cloud** | **bool** | Determines whether organization is hosted in iikoCloud. | 
**is_anonymous_guests_allowed** | **bool** | If the store allows orders for anonymous guests, then it is not necessary to transfer  information about the guest as part of the delivery order. You can only transfer  the phone number and optionally name of the guest, which will not be stored in the guest base  and will only be used for the delivery of a current delivery order. | [optional] 
**address_lookup** | [**List[AddressHintsAddressHintsServiceType]**](AddressHintsAddressHintsServiceType.md) | Available address lookup services. | 

## Example

```python
from iikocloud_client.models.organizations_extended_organization_info import OrganizationsExtendedOrganizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsExtendedOrganizationInfo from a JSON string
organizations_extended_organization_info_instance = OrganizationsExtendedOrganizationInfo.from_json(json)
# print the JSON string representation of the object
print(OrganizationsExtendedOrganizationInfo.to_json())

# convert the object into a dict
organizations_extended_organization_info_dict = organizations_extended_organization_info_instance.to_dict()
# create an instance of OrganizationsExtendedOrganizationInfo from a dict
organizations_extended_organization_info_from_dict = OrganizationsExtendedOrganizationInfo.from_dict(organizations_extended_organization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


