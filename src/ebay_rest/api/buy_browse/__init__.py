# coding: utf-8

# flake8: noqa

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values.</li>  <li><b> search_by_image: </b><a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  <li> <b> shopping_cart: </b> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#experimental\" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Release\" title=\"Experimental Release\" />&nbsp;(Experimental)</a> <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&nbsp;&nbsp;<b> Note: </b> This resource is not available in the eBay API Explorer.</li></ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>. The <b> shopping_cart</b> resource calls require a <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">User access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from ..buy_browse.api.item_api import ItemApi
from ..buy_browse.api.item_summary_api import ItemSummaryApi
from ..buy_browse.api.search_by_image_api import SearchByImageApi
from ..buy_browse.api.shopping_cart_api import ShoppingCartApi
# import ApiClient
from ..buy_browse.api_client import ApiClient
from ..buy_browse.configuration import Configuration
# import models into sdk package
from ..buy_browse.models.add_cart_item_input import AddCartItemInput
from ..buy_browse.models.additional_product_identity import AdditionalProductIdentity
from ..buy_browse.models.address import Address
from ..buy_browse.models.amount import Amount
from ..buy_browse.models.aspect import Aspect
from ..buy_browse.models.aspect_distribution import AspectDistribution
from ..buy_browse.models.aspect_group import AspectGroup
from ..buy_browse.models.aspect_value_distribution import AspectValueDistribution
from ..buy_browse.models.attribute_name_value import AttributeNameValue
from ..buy_browse.models.authenticity_guarantee_program import AuthenticityGuaranteeProgram
from ..buy_browse.models.authenticity_verification_program import AuthenticityVerificationProgram
from ..buy_browse.models.auto_corrections import AutoCorrections
from ..buy_browse.models.available_coupon import AvailableCoupon
from ..buy_browse.models.buying_option_distribution import BuyingOptionDistribution
from ..buy_browse.models.cart_item import CartItem
from ..buy_browse.models.category import Category
from ..buy_browse.models.category_distribution import CategoryDistribution
from ..buy_browse.models.common_descriptions import CommonDescriptions
from ..buy_browse.models.compatibility_payload import CompatibilityPayload
from ..buy_browse.models.compatibility_property import CompatibilityProperty
from ..buy_browse.models.compatibility_response import CompatibilityResponse
from ..buy_browse.models.condition_distribution import ConditionDistribution
from ..buy_browse.models.converted_amount import ConvertedAmount
from ..buy_browse.models.core_item import CoreItem
from ..buy_browse.models.coupon_constraint import CouponConstraint
from ..buy_browse.models.error import Error
from ..buy_browse.models.error_parameter import ErrorParameter
from ..buy_browse.models.estimated_availability import EstimatedAvailability
from ..buy_browse.models.image import Image
from ..buy_browse.models.item import Item
from ..buy_browse.models.item_group import ItemGroup
from ..buy_browse.models.item_group_summary import ItemGroupSummary
from ..buy_browse.models.item_location_impl import ItemLocationImpl
from ..buy_browse.models.item_return_terms import ItemReturnTerms
from ..buy_browse.models.item_summary import ItemSummary
from ..buy_browse.models.items import Items
from ..buy_browse.models.legal_address import LegalAddress
from ..buy_browse.models.marketing_price import MarketingPrice
from ..buy_browse.models.payment_method import PaymentMethod
from ..buy_browse.models.payment_method_brand import PaymentMethodBrand
from ..buy_browse.models.pickup_option_summary import PickupOptionSummary
from ..buy_browse.models.price import Price
from ..buy_browse.models.product import Product
from ..buy_browse.models.product_identity import ProductIdentity
from ..buy_browse.models.rating_histogram import RatingHistogram
from ..buy_browse.models.refinement import Refinement
from ..buy_browse.models.region import Region
from ..buy_browse.models.remote_shopcart_response import RemoteShopcartResponse
from ..buy_browse.models.remove_cart_item_input import RemoveCartItemInput
from ..buy_browse.models.review_rating import ReviewRating
from ..buy_browse.models.search_by_image_request import SearchByImageRequest
from ..buy_browse.models.search_paged_collection import SearchPagedCollection
from ..buy_browse.models.seller import Seller
from ..buy_browse.models.seller_custom_policy import SellerCustomPolicy
from ..buy_browse.models.seller_detail import SellerDetail
from ..buy_browse.models.seller_legal_info import SellerLegalInfo
from ..buy_browse.models.ship_to_location import ShipToLocation
from ..buy_browse.models.ship_to_locations import ShipToLocations
from ..buy_browse.models.ship_to_region import ShipToRegion
from ..buy_browse.models.shipping_option import ShippingOption
from ..buy_browse.models.shipping_option_summary import ShippingOptionSummary
from ..buy_browse.models.target_location import TargetLocation
from ..buy_browse.models.tax_jurisdiction import TaxJurisdiction
from ..buy_browse.models.taxes import Taxes
from ..buy_browse.models.time_duration import TimeDuration
from ..buy_browse.models.typed_name_value import TypedNameValue
from ..buy_browse.models.update_cart_item_input import UpdateCartItemInput
from ..buy_browse.models.vat_detail import VatDetail
