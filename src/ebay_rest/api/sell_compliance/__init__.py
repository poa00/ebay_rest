# coding: utf-8

# flake8: noqa

"""
    Compliance API

    Service for providing information to sellers about their listings being non-compliant, or at risk for becoming non-compliant, against eBay listing policies.  # noqa: E501

    OpenAPI spec version: 1.4.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from ..sell_compliance.api.listing_violation_api import ListingViolationApi
from ..sell_compliance.api.listing_violation_summary_api import ListingViolationSummaryApi
# import ApiClient
from ..sell_compliance.api_client import ApiClient
from ..sell_compliance.configuration import Configuration
# import models into sdk package
from ..sell_compliance.models.aspect_recommendations import AspectRecommendations
from ..sell_compliance.models.compliance_detail import ComplianceDetail
from ..sell_compliance.models.compliance_summary import ComplianceSummary
from ..sell_compliance.models.compliance_summary_info import ComplianceSummaryInfo
from ..sell_compliance.models.compliance_violation import ComplianceViolation
from ..sell_compliance.models.corrective_recommendations import CorrectiveRecommendations
from ..sell_compliance.models.error import Error
from ..sell_compliance.models.error_parameter import ErrorParameter
from ..sell_compliance.models.name_value_list import NameValueList
from ..sell_compliance.models.paged_compliance_violation_collection import PagedComplianceViolationCollection
from ..sell_compliance.models.product_recommendation import ProductRecommendation
from ..sell_compliance.models.variation_details import VariationDetails
