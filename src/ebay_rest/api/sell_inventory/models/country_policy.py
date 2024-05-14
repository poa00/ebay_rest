# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.17.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CountryPolicy(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'country': 'str',
        'policy_ids': 'list[str]'
    }

    attribute_map = {
        'country': 'country',
        'policy_ids': 'policyIds'
    }

    def __init__(self, country=None, policy_ids=None):  # noqa: E501
        """CountryPolicy - a model defined in Swagger"""  # noqa: E501
        self._country = None
        self._policy_ids = None
        self.discriminator = None
        if country is not None:
            self.country = country
        if policy_ids is not None:
            self.policy_ids = policy_ids

    @property
    def country(self):
        """Gets the country of this CountryPolicy.  # noqa: E501

        The two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" target=\"_blank\">ISO 3166-1</a> country code identifying the country to which the policy or policies specified in the corresponding policyIds array will apply. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The country of this CountryPolicy.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CountryPolicy.

        The two-letter <a href=\"https://www.iso.org/iso-3166-country-codes.html \" target=\"_blank\">ISO 3166-1</a> country code identifying the country to which the policy or policies specified in the corresponding policyIds array will apply. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/ba:CountryCodeEnum'>eBay API documentation</a>  # noqa: E501

        :param country: The country of this CountryPolicy.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def policy_ids(self):
        """Gets the policy_ids of this CountryPolicy.  # noqa: E501

        An array of custom policy identifiers that apply to the country specified by <a href=\"#request.listingPolicies.regionalProductCompliancePolicies.countryPolicies.country\">listingPolicies.regionalTakeBackPolicies.countryPolicies.country</a>.<br><br>Product compliance and take-back policy information may be returned using the following methods:<ul><li><a href=\"/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicies \" target=\"_blank\">getCustomPolicies</a><br><br>Set <code>policy_types</code> to:<ul><li><code>PRODUCT_COMPLIANCE</code> for product compliance policies</li><li><code>TAKE_BACK</code> for takeback policies</li></ul><br>This returns the list of specified policies and corresponding <b>customPolicyId</b> values a seller has created.</li><li><a href=\"/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicy \" target=\"_blank\">getCustomPolicy</a> with <code>custom_policy_id = customPolicyId</code><br><br>Returns the details of the the policy specified by <b>customPolicyId</b></li></ul>For information about creating and managing custom policies, refer to the <a href=\"/api-docs/sell/account/resources/methods#h2-custom_policy \" target=\"_blank\">custom_policy</a> resource in the <b>Sell Account</b> API.  # noqa: E501

        :return: The policy_ids of this CountryPolicy.  # noqa: E501
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        """Sets the policy_ids of this CountryPolicy.

        An array of custom policy identifiers that apply to the country specified by <a href=\"#request.listingPolicies.regionalProductCompliancePolicies.countryPolicies.country\">listingPolicies.regionalTakeBackPolicies.countryPolicies.country</a>.<br><br>Product compliance and take-back policy information may be returned using the following methods:<ul><li><a href=\"/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicies \" target=\"_blank\">getCustomPolicies</a><br><br>Set <code>policy_types</code> to:<ul><li><code>PRODUCT_COMPLIANCE</code> for product compliance policies</li><li><code>TAKE_BACK</code> for takeback policies</li></ul><br>This returns the list of specified policies and corresponding <b>customPolicyId</b> values a seller has created.</li><li><a href=\"/api-docs/sell/account/resources/custom_policy/methods/getCustomPolicy \" target=\"_blank\">getCustomPolicy</a> with <code>custom_policy_id = customPolicyId</code><br><br>Returns the details of the the policy specified by <b>customPolicyId</b></li></ul>For information about creating and managing custom policies, refer to the <a href=\"/api-docs/sell/account/resources/methods#h2-custom_policy \" target=\"_blank\">custom_policy</a> resource in the <b>Sell Account</b> API.  # noqa: E501

        :param policy_ids: The policy_ids of this CountryPolicy.  # noqa: E501
        :type: list[str]
        """

        self._policy_ids = policy_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CountryPolicy, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CountryPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
