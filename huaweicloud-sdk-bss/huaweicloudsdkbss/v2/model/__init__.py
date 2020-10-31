# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkbss.v2.model.account_balance_v2 import AccountBalanceV2
from huaweicloudsdkbss.v2.model.account_balance_v3 import AccountBalanceV3
from huaweicloudsdkbss.v2.model.account_manager import AccountManager
from huaweicloudsdkbss.v2.model.add_postal_req import AddPostalReq
from huaweicloudsdkbss.v2.model.adjust_account_req import AdjustAccountReq
from huaweicloudsdkbss.v2.model.adjust_coupon_quotas_req import AdjustCouponQuotasReq
from huaweicloudsdkbss.v2.model.adjust_record_v2 import AdjustRecordV2
from huaweicloudsdkbss.v2.model.adjust_to_indirect_partner_req import AdjustToIndirectPartnerReq
from huaweicloudsdkbss.v2.model.agent_pay_info import AgentPayInfo
from huaweicloudsdkbss.v2.model.amount_infomation import AmountInfomation
from huaweicloudsdkbss.v2.model.amount_infomation_v2 import AmountInfomationV2
from huaweicloudsdkbss.v2.model.apply_enterprise_realname_auths_req import ApplyEnterpriseRealnameAuthsReq
from huaweicloudsdkbss.v2.model.apply_individual_realname_auths_req import ApplyIndividualRealnameAuthsReq
from huaweicloudsdkbss.v2.model.auto_renewal_resources_request import AutoRenewalResourcesRequest
from huaweicloudsdkbss.v2.model.auto_renewal_resources_response import AutoRenewalResourcesResponse
from huaweicloudsdkbss.v2.model.balance_type_deduct_sum_v2 import BalanceTypeDeductSumV2
from huaweicloudsdkbss.v2.model.bank_card_info_v2 import BankCardInfoV2
from huaweicloudsdkbss.v2.model.batch_set_sub_customer_discount_request import BatchSetSubCustomerDiscountRequest
from huaweicloudsdkbss.v2.model.batch_set_sub_customer_discount_response import BatchSetSubCustomerDiscountResponse
from huaweicloudsdkbss.v2.model.bill_sum_info_v2 import BillSumInfoV2
from huaweicloudsdkbss.v2.model.bill_sum_record_info_v2 import BillSumRecordInfoV2
from huaweicloudsdkbss.v2.model.cancel_auto_renewal_resources_request import CancelAutoRenewalResourcesRequest
from huaweicloudsdkbss.v2.model.cancel_auto_renewal_resources_response import CancelAutoRenewalResourcesResponse
from huaweicloudsdkbss.v2.model.cancel_customer_order_req import CancelCustomerOrderReq
from huaweicloudsdkbss.v2.model.cancel_customer_order_request import CancelCustomerOrderRequest
from huaweicloudsdkbss.v2.model.cancel_customer_order_response import CancelCustomerOrderResponse
from huaweicloudsdkbss.v2.model.cancel_resources_subscription_request import CancelResourcesSubscriptionRequest
from huaweicloudsdkbss.v2.model.cancel_resources_subscription_response import CancelResourcesSubscriptionResponse
from huaweicloudsdkbss.v2.model.change_enterprise_realname_authentication_request import ChangeEnterpriseRealnameAuthenticationRequest
from huaweicloudsdkbss.v2.model.change_enterprise_realname_authentication_response import ChangeEnterpriseRealnameAuthenticationResponse
from huaweicloudsdkbss.v2.model.change_enterprise_realname_auths_req import ChangeEnterpriseRealnameAuthsReq
from huaweicloudsdkbss.v2.model.check_subcustomer_user_req import CheckSubcustomerUserReq
from huaweicloudsdkbss.v2.model.check_user_identity_request import CheckUserIdentityRequest
from huaweicloudsdkbss.v2.model.check_user_identity_response import CheckUserIdentityResponse
from huaweicloudsdkbss.v2.model.city import City
from huaweicloudsdkbss.v2.model.county import County
from huaweicloudsdkbss.v2.model.coupon_info_v2 import CouponInfoV2
from huaweicloudsdkbss.v2.model.coupon_quota_v2 import CouponQuotaV2
from huaweicloudsdkbss.v2.model.coupon_record_v2 import CouponRecordV2
from huaweicloudsdkbss.v2.model.coupon_simple_info import CouponSimpleInfo
from huaweicloudsdkbss.v2.model.coupon_simple_info_order_pay import CouponSimpleInfoOrderPay
from huaweicloudsdkbss.v2.model.create_customer_v2_req import CreateCustomerV2Req
from huaweicloudsdkbss.v2.model.create_enterprise_project_auth_request import CreateEnterpriseProjectAuthRequest
from huaweicloudsdkbss.v2.model.create_enterprise_project_auth_response import CreateEnterpriseProjectAuthResponse
from huaweicloudsdkbss.v2.model.create_enterprise_realname_authentication_request import CreateEnterpriseRealnameAuthenticationRequest
from huaweicloudsdkbss.v2.model.create_enterprise_realname_authentication_response import CreateEnterpriseRealnameAuthenticationResponse
from huaweicloudsdkbss.v2.model.create_partner_coupons_req import CreatePartnerCouponsReq
from huaweicloudsdkbss.v2.model.create_partner_coupons_request import CreatePartnerCouponsRequest
from huaweicloudsdkbss.v2.model.create_partner_coupons_response import CreatePartnerCouponsResponse
from huaweicloudsdkbss.v2.model.create_personal_realname_auth_request import CreatePersonalRealnameAuthRequest
from huaweicloudsdkbss.v2.model.create_personal_realname_auth_response import CreatePersonalRealnameAuthResponse
from huaweicloudsdkbss.v2.model.create_postal_request import CreatePostalRequest
from huaweicloudsdkbss.v2.model.create_postal_response import CreatePostalResponse
from huaweicloudsdkbss.v2.model.create_sub_customer_req_v2 import CreateSubCustomerReqV2
from huaweicloudsdkbss.v2.model.create_sub_customer_request import CreateSubCustomerRequest
from huaweicloudsdkbss.v2.model.create_sub_customer_response import CreateSubCustomerResponse
from huaweicloudsdkbss.v2.model.create_sub_enterprise_account_request import CreateSubEnterpriseAccountRequest
from huaweicloudsdkbss.v2.model.create_sub_enterprise_account_response import CreateSubEnterpriseAccountResponse
from huaweicloudsdkbss.v2.model.customer_balances_v2 import CustomerBalancesV2
from huaweicloudsdkbss.v2.model.customer_info_v2 import CustomerInfoV2
from huaweicloudsdkbss.v2.model.customer_information import CustomerInformation
from huaweicloudsdkbss.v2.model.customer_on_demand_resource import CustomerOnDemandResource
from huaweicloudsdkbss.v2.model.customer_order_entity import CustomerOrderEntity
from huaweicloudsdkbss.v2.model.customer_order_v2 import CustomerOrderV2
from huaweicloudsdkbss.v2.model.customer_postal_address_v2 import CustomerPostalAddressV2
from huaweicloudsdkbss.v2.model.delete_postal_request import DeletePostalRequest
from huaweicloudsdkbss.v2.model.delete_postal_response import DeletePostalResponse
from huaweicloudsdkbss.v2.model.demand_discount_rating_result import DemandDiscountRatingResult
from huaweicloudsdkbss.v2.model.demand_product_info import DemandProductInfo
from huaweicloudsdkbss.v2.model.demand_product_rating_result import DemandProductRatingResult
from huaweicloudsdkbss.v2.model.discount_entry import DiscountEntry
from huaweicloudsdkbss.v2.model.discount_item_v2 import DiscountItemV2
from huaweicloudsdkbss.v2.model.em_child_node_v2 import EmChildNodeV2
from huaweicloudsdkbss.v2.model.enterprise_person_new import EnterprisePersonNew
from huaweicloudsdkbss.v2.model.error_detail import ErrorDetail
from huaweicloudsdkbss.v2.model.i_coupon_use_limit_info_v2 import ICouponUseLimitInfoV2
from huaweicloudsdkbss.v2.model.i_query_user_coupons_result_v2 import IQueryUserCouponsResultV2
from huaweicloudsdkbss.v2.model.i_query_user_partner_coupons_result_v2 import IQueryUserPartnerCouponsResultV2
from huaweicloudsdkbss.v2.model.indirect_partner_info import IndirectPartnerInfo
from huaweicloudsdkbss.v2.model.issued_coupon_quota import IssuedCouponQuota
from huaweicloudsdkbss.v2.model.limit_info_v2 import LimitInfoV2
from huaweicloudsdkbss.v2.model.limit_value import LimitValue
from huaweicloudsdkbss.v2.model.list_cities_request import ListCitiesRequest
from huaweicloudsdkbss.v2.model.list_cities_response import ListCitiesResponse
from huaweicloudsdkbss.v2.model.list_counties_request import ListCountiesRequest
from huaweicloudsdkbss.v2.model.list_counties_response import ListCountiesResponse
from huaweicloudsdkbss.v2.model.list_coupon_quotas_records_request import ListCouponQuotasRecordsRequest
from huaweicloudsdkbss.v2.model.list_coupon_quotas_records_response import ListCouponQuotasRecordsResponse
from huaweicloudsdkbss.v2.model.list_customer_bills_fee_records_request import ListCustomerBillsFeeRecordsRequest
from huaweicloudsdkbss.v2.model.list_customer_bills_fee_records_response import ListCustomerBillsFeeRecordsResponse
from huaweicloudsdkbss.v2.model.list_customer_on_demand_resources_request import ListCustomerOnDemandResourcesRequest
from huaweicloudsdkbss.v2.model.list_customer_on_demand_resources_response import ListCustomerOnDemandResourcesResponse
from huaweicloudsdkbss.v2.model.list_customer_orders_request import ListCustomerOrdersRequest
from huaweicloudsdkbss.v2.model.list_customer_orders_response import ListCustomerOrdersResponse
from huaweicloudsdkbss.v2.model.list_customers_balances_detail_request import ListCustomersBalancesDetailRequest
from huaweicloudsdkbss.v2.model.list_customers_balances_detail_response import ListCustomersBalancesDetailResponse
from huaweicloudsdkbss.v2.model.list_customerself_resource_record_details_request import ListCustomerselfResourceRecordDetailsRequest
from huaweicloudsdkbss.v2.model.list_customerself_resource_record_details_response import ListCustomerselfResourceRecordDetailsResponse
from huaweicloudsdkbss.v2.model.list_customerself_resource_records_request import ListCustomerselfResourceRecordsRequest
from huaweicloudsdkbss.v2.model.list_customerself_resource_records_response import ListCustomerselfResourceRecordsResponse
from huaweicloudsdkbss.v2.model.list_enterprise_multi_account_request import ListEnterpriseMultiAccountRequest
from huaweicloudsdkbss.v2.model.list_enterprise_multi_account_response import ListEnterpriseMultiAccountResponse
from huaweicloudsdkbss.v2.model.list_enterprise_organizations_request import ListEnterpriseOrganizationsRequest
from huaweicloudsdkbss.v2.model.list_enterprise_organizations_response import ListEnterpriseOrganizationsResponse
from huaweicloudsdkbss.v2.model.list_enterprise_sub_customers_request import ListEnterpriseSubCustomersRequest
from huaweicloudsdkbss.v2.model.list_enterprise_sub_customers_response import ListEnterpriseSubCustomersResponse
from huaweicloudsdkbss.v2.model.list_indirect_partners_request import ListIndirectPartnersRequest
from huaweicloudsdkbss.v2.model.list_indirect_partners_response import ListIndirectPartnersResponse
from huaweicloudsdkbss.v2.model.list_issued_coupon_quotas_request import ListIssuedCouponQuotasRequest
from huaweicloudsdkbss.v2.model.list_issued_coupon_quotas_response import ListIssuedCouponQuotasResponse
from huaweicloudsdkbss.v2.model.list_issued_partner_coupons_request import ListIssuedPartnerCouponsRequest
from huaweicloudsdkbss.v2.model.list_issued_partner_coupons_response import ListIssuedPartnerCouponsResponse
from huaweicloudsdkbss.v2.model.list_on_demand_resource_ratings_request import ListOnDemandResourceRatingsRequest
from huaweicloudsdkbss.v2.model.list_on_demand_resource_ratings_response import ListOnDemandResourceRatingsResponse
from huaweicloudsdkbss.v2.model.list_order_coupons_by_order_id_request import ListOrderCouponsByOrderIdRequest
from huaweicloudsdkbss.v2.model.list_order_coupons_by_order_id_response import ListOrderCouponsByOrderIdResponse
from huaweicloudsdkbss.v2.model.list_partner_adjust_records_request import ListPartnerAdjustRecordsRequest
from huaweicloudsdkbss.v2.model.list_partner_adjust_records_response import ListPartnerAdjustRecordsResponse
from huaweicloudsdkbss.v2.model.list_partner_balances_request import ListPartnerBalancesRequest
from huaweicloudsdkbss.v2.model.list_partner_balances_response import ListPartnerBalancesResponse
from huaweicloudsdkbss.v2.model.list_partner_coupons_record_request import ListPartnerCouponsRecordRequest
from huaweicloudsdkbss.v2.model.list_partner_coupons_record_response import ListPartnerCouponsRecordResponse
from huaweicloudsdkbss.v2.model.list_partner_pay_orders_request import ListPartnerPayOrdersRequest
from huaweicloudsdkbss.v2.model.list_partner_pay_orders_response import ListPartnerPayOrdersResponse
from huaweicloudsdkbss.v2.model.list_pay_per_use_customer_resources_request import ListPayPerUseCustomerResourcesRequest
from huaweicloudsdkbss.v2.model.list_pay_per_use_customer_resources_response import ListPayPerUseCustomerResourcesResponse
from huaweicloudsdkbss.v2.model.list_postal_address_request import ListPostalAddressRequest
from huaweicloudsdkbss.v2.model.list_postal_address_response import ListPostalAddressResponse
from huaweicloudsdkbss.v2.model.list_provinces_request import ListProvincesRequest
from huaweicloudsdkbss.v2.model.list_provinces_response import ListProvincesResponse
from huaweicloudsdkbss.v2.model.list_quota_coupons_request import ListQuotaCouponsRequest
from huaweicloudsdkbss.v2.model.list_quota_coupons_response import ListQuotaCouponsResponse
from huaweicloudsdkbss.v2.model.list_rate_on_period_detail_request import ListRateOnPeriodDetailRequest
from huaweicloudsdkbss.v2.model.list_rate_on_period_detail_response import ListRateOnPeriodDetailResponse
from huaweicloudsdkbss.v2.model.list_resource_types_request import ListResourceTypesRequest
from huaweicloudsdkbss.v2.model.list_resource_types_response import ListResourceTypesResponse
from huaweicloudsdkbss.v2.model.list_resource_usages_request import ListResourceUsagesRequest
from huaweicloudsdkbss.v2.model.list_resource_usages_response import ListResourceUsagesResponse
from huaweicloudsdkbss.v2.model.list_service_resources_request import ListServiceResourcesRequest
from huaweicloudsdkbss.v2.model.list_service_resources_response import ListServiceResourcesResponse
from huaweicloudsdkbss.v2.model.list_service_types_request import ListServiceTypesRequest
from huaweicloudsdkbss.v2.model.list_service_types_response import ListServiceTypesResponse
from huaweicloudsdkbss.v2.model.list_sku_inventories_request import ListSkuInventoriesRequest
from huaweicloudsdkbss.v2.model.list_sku_inventories_response import ListSkuInventoriesResponse
from huaweicloudsdkbss.v2.model.list_sub_customer_coupons_request import ListSubCustomerCouponsRequest
from huaweicloudsdkbss.v2.model.list_sub_customer_coupons_response import ListSubCustomerCouponsResponse
from huaweicloudsdkbss.v2.model.list_sub_customer_discounts_request import ListSubCustomerDiscountsRequest
from huaweicloudsdkbss.v2.model.list_sub_customer_discounts_response import ListSubCustomerDiscountsResponse
from huaweicloudsdkbss.v2.model.list_sub_customer_res_fee_records_request import ListSubCustomerResFeeRecordsRequest
from huaweicloudsdkbss.v2.model.list_sub_customer_res_fee_records_response import ListSubCustomerResFeeRecordsResponse
from huaweicloudsdkbss.v2.model.list_sub_customers_request import ListSubCustomersRequest
from huaweicloudsdkbss.v2.model.list_sub_customers_response import ListSubCustomersResponse
from huaweicloudsdkbss.v2.model.list_subcustomer_monthly_bills_request import ListSubcustomerMonthlyBillsRequest
from huaweicloudsdkbss.v2.model.list_subcustomer_monthly_bills_response import ListSubcustomerMonthlyBillsResponse
from huaweicloudsdkbss.v2.model.monthly_bill_record import MonthlyBillRecord
from huaweicloudsdkbss.v2.model.monthly_bill_res import MonthlyBillRes
from huaweicloudsdkbss.v2.model.new_customer_v2 import NewCustomerV2
from huaweicloudsdkbss.v2.model.official_website_rating_result import OfficialWebsiteRatingResult
from huaweicloudsdkbss.v2.model.optional_discount_rating_result import OptionalDiscountRatingResult
from huaweicloudsdkbss.v2.model.order_instance_v2 import OrderInstanceV2
from huaweicloudsdkbss.v2.model.order_line_item_entity_v2 import OrderLineItemEntityV2
from huaweicloudsdkbss.v2.model.order_refund_info_v2 import OrderRefundInfoV2
from huaweicloudsdkbss.v2.model.package_usage_info import PackageUsageInfo
from huaweicloudsdkbss.v2.model.pay_customer_order_req import PayCustomerOrderReq
from huaweicloudsdkbss.v2.model.pay_orders_request import PayOrdersRequest
from huaweicloudsdkbss.v2.model.pay_orders_response import PayOrdersResponse
from huaweicloudsdkbss.v2.model.period_product_info import PeriodProductInfo
from huaweicloudsdkbss.v2.model.period_product_official_rating_result import PeriodProductOfficialRatingResult
from huaweicloudsdkbss.v2.model.period_product_rating_result import PeriodProductRatingResult
from huaweicloudsdkbss.v2.model.province import Province
from huaweicloudsdkbss.v2.model.query_coupon_quotas_req_ext import QueryCouponQuotasReqExt
from huaweicloudsdkbss.v2.model.query_customer_on_demand_resources_req import QueryCustomerOnDemandResourcesReq
from huaweicloudsdkbss.v2.model.query_customers_balances_req import QueryCustomersBalancesReq
from huaweicloudsdkbss.v2.model.query_indirect_partners_req import QueryIndirectPartnersReq
from huaweicloudsdkbss.v2.model.query_res_records_detail_req import QueryResRecordsDetailReq
from huaweicloudsdkbss.v2.model.query_resources_req import QueryResourcesReq
from huaweicloudsdkbss.v2.model.query_sku_inventories_req import QuerySkuInventoriesReq
from huaweicloudsdkbss.v2.model.query_sub_customer_discount_v2 import QuerySubCustomerDiscountV2
from huaweicloudsdkbss.v2.model.query_sub_customer_list_req import QuerySubCustomerListReq
from huaweicloudsdkbss.v2.model.quota_limit_info import QuotaLimitInfo
from huaweicloudsdkbss.v2.model.quota_reclaim import QuotaReclaim
from huaweicloudsdkbss.v2.model.quota_record import QuotaRecord
from huaweicloudsdkbss.v2.model.quota_simple_info import QuotaSimpleInfo
from huaweicloudsdkbss.v2.model.rate_on_demand_req import RateOnDemandReq
from huaweicloudsdkbss.v2.model.rate_on_period_req import RateOnPeriodReq
from huaweicloudsdkbss.v2.model.reclaim_coupon_quotas_req import ReclaimCouponQuotasReq
from huaweicloudsdkbss.v2.model.reclaim_coupon_quotas_request import ReclaimCouponQuotasRequest
from huaweicloudsdkbss.v2.model.reclaim_coupon_quotas_response import ReclaimCouponQuotasResponse
from huaweicloudsdkbss.v2.model.reclaim_indirect_partner_account_req import ReclaimIndirectPartnerAccountReq
from huaweicloudsdkbss.v2.model.reclaim_indirect_partner_account_request import ReclaimIndirectPartnerAccountRequest
from huaweicloudsdkbss.v2.model.reclaim_indirect_partner_account_response import ReclaimIndirectPartnerAccountResponse
from huaweicloudsdkbss.v2.model.reclaim_partner_coupons_req import ReclaimPartnerCouponsReq
from huaweicloudsdkbss.v2.model.reclaim_partner_coupons_request import ReclaimPartnerCouponsRequest
from huaweicloudsdkbss.v2.model.reclaim_partner_coupons_response import ReclaimPartnerCouponsResponse
from huaweicloudsdkbss.v2.model.reclaim_sub_enterprise_amount_request import ReclaimSubEnterpriseAmountRequest
from huaweicloudsdkbss.v2.model.reclaim_sub_enterprise_amount_response import ReclaimSubEnterpriseAmountResponse
from huaweicloudsdkbss.v2.model.reclaim_to_partner_account_balances_req import ReclaimToPartnerAccountBalancesReq
from huaweicloudsdkbss.v2.model.reclaim_to_partner_account_request import ReclaimToPartnerAccountRequest
from huaweicloudsdkbss.v2.model.reclaim_to_partner_account_response import ReclaimToPartnerAccountResponse
from huaweicloudsdkbss.v2.model.renewal_resources_req import RenewalResourcesReq
from huaweicloudsdkbss.v2.model.renewal_resources_request import RenewalResourcesRequest
from huaweicloudsdkbss.v2.model.renewal_resources_response import RenewalResourcesResponse
from huaweicloudsdkbss.v2.model.res_fee_record_v2 import ResFeeRecordV2
from huaweicloudsdkbss.v2.model.resource_basic_info import ResourceBasicInfo
from huaweicloudsdkbss.v2.model.resource_type import ResourceType
from huaweicloudsdkbss.v2.model.retrieve_amount_info_v2 import RetrieveAmountInfoV2
from huaweicloudsdkbss.v2.model.retrieve_enterprise_multi_account_req import RetrieveEnterpriseMultiAccountReq
from huaweicloudsdkbss.v2.model.send_sm_verification_code_req import SendSmVerificationCodeReq
from huaweicloudsdkbss.v2.model.send_sms_verification_code_request import SendSmsVerificationCodeRequest
from huaweicloudsdkbss.v2.model.send_sms_verification_code_response import SendSmsVerificationCodeResponse
from huaweicloudsdkbss.v2.model.send_verification_code_v2_req import SendVerificationCodeV2Req
from huaweicloudsdkbss.v2.model.send_verification_message_code_request import SendVerificationMessageCodeRequest
from huaweicloudsdkbss.v2.model.send_verification_message_code_response import SendVerificationMessageCodeResponse
from huaweicloudsdkbss.v2.model.service_resource_info import ServiceResourceInfo
from huaweicloudsdkbss.v2.model.service_type import ServiceType
from huaweicloudsdkbss.v2.model.set_partner_discounts_req import SetPartnerDiscountsReq
from huaweicloudsdkbss.v2.model.set_sub_customer_discount_v2 import SetSubCustomerDiscountV2
from huaweicloudsdkbss.v2.model.show_cusotmer_account_balances_request import ShowCusotmerAccountBalancesRequest
from huaweicloudsdkbss.v2.model.show_cusotmer_account_balances_response import ShowCusotmerAccountBalancesResponse
from huaweicloudsdkbss.v2.model.show_customer_monthly_sum_request import ShowCustomerMonthlySumRequest
from huaweicloudsdkbss.v2.model.show_customer_monthly_sum_response import ShowCustomerMonthlySumResponse
from huaweicloudsdkbss.v2.model.show_customer_order_details_request import ShowCustomerOrderDetailsRequest
from huaweicloudsdkbss.v2.model.show_customer_order_details_response import ShowCustomerOrderDetailsResponse
from huaweicloudsdkbss.v2.model.show_multi_account_transfer_amount_request import ShowMultiAccountTransferAmountRequest
from huaweicloudsdkbss.v2.model.show_multi_account_transfer_amount_response import ShowMultiAccountTransferAmountResponse
from huaweicloudsdkbss.v2.model.show_realname_authentication_review_result_request import ShowRealnameAuthenticationReviewResultRequest
from huaweicloudsdkbss.v2.model.show_realname_authentication_review_result_response import ShowRealnameAuthenticationReviewResultResponse
from huaweicloudsdkbss.v2.model.show_refund_order_details_request import ShowRefundOrderDetailsRequest
from huaweicloudsdkbss.v2.model.show_refund_order_details_response import ShowRefundOrderDetailsResponse
from huaweicloudsdkbss.v2.model.sku_inventory import SkuInventory
from huaweicloudsdkbss.v2.model.sku_item import SkuItem
from huaweicloudsdkbss.v2.model.sub_customer_info_v2 import SubCustomerInfoV2
from huaweicloudsdkbss.v2.model.sub_customer_res_fee_record_v2 import SubCustomerResFeeRecordV2
from huaweicloudsdkbss.v2.model.template_args import TemplateArgs
from huaweicloudsdkbss.v2.model.transfer_amount_info_v2 import TransferAmountInfoV2
from huaweicloudsdkbss.v2.model.transfer_enterprise_multi_account_req import TransferEnterpriseMultiAccountReq
from huaweicloudsdkbss.v2.model.unsubscribe_resources_req import UnsubscribeResourcesReq
from huaweicloudsdkbss.v2.model.update_coupon_quotas_request import UpdateCouponQuotasRequest
from huaweicloudsdkbss.v2.model.update_coupon_quotas_response import UpdateCouponQuotasResponse
from huaweicloudsdkbss.v2.model.update_customer_account_amount_request import UpdateCustomerAccountAmountRequest
from huaweicloudsdkbss.v2.model.update_customer_account_amount_response import UpdateCustomerAccountAmountResponse
from huaweicloudsdkbss.v2.model.update_indirect_partner_account_request import UpdateIndirectPartnerAccountRequest
from huaweicloudsdkbss.v2.model.update_indirect_partner_account_response import UpdateIndirectPartnerAccountResponse
from huaweicloudsdkbss.v2.model.update_postal_req import UpdatePostalReq
from huaweicloudsdkbss.v2.model.update_postal_request import UpdatePostalRequest
from huaweicloudsdkbss.v2.model.update_postal_response import UpdatePostalResponse
from huaweicloudsdkbss.v2.model.update_sub_enterprise_amount_request import UpdateSubEnterpriseAmountRequest
from huaweicloudsdkbss.v2.model.update_sub_enterprise_amount_response import UpdateSubEnterpriseAmountResponse
