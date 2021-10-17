# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DiscountRule(object):
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
        'discount_benefit': 'DiscountBenefit',
        'discount_specification': 'DiscountSpecification',
        'max_discount_amount': 'Amount',
        'rule_order': 'int'
    }

    attribute_map = {
        'discount_benefit': 'discountBenefit',
        'discount_specification': 'discountSpecification',
        'max_discount_amount': 'maxDiscountAmount',
        'rule_order': 'ruleOrder'
    }

    def __init__(self, discount_benefit=None, discount_specification=None, max_discount_amount=None, rule_order=None):  # noqa: E501
        """DiscountRule - a model defined in Swagger"""  # noqa: E501
        self._discount_benefit = None
        self._discount_specification = None
        self._max_discount_amount = None
        self._rule_order = None
        self.discriminator = None
        if discount_benefit is not None:
            self.discount_benefit = discount_benefit
        if discount_specification is not None:
            self.discount_specification = discount_specification
        if max_discount_amount is not None:
            self.max_discount_amount = max_discount_amount
        if rule_order is not None:
            self.rule_order = rule_order

    @property
    def discount_benefit(self):
        """Gets the discount_benefit of this DiscountRule.  # noqa: E501


        :return: The discount_benefit of this DiscountRule.  # noqa: E501
        :rtype: DiscountBenefit
        """
        return self._discount_benefit

    @discount_benefit.setter
    def discount_benefit(self, discount_benefit):
        """Sets the discount_benefit of this DiscountRule.


        :param discount_benefit: The discount_benefit of this DiscountRule.  # noqa: E501
        :type: DiscountBenefit
        """

        self._discount_benefit = discount_benefit

    @property
    def discount_specification(self):
        """Gets the discount_specification of this DiscountRule.  # noqa: E501


        :return: The discount_specification of this DiscountRule.  # noqa: E501
        :rtype: DiscountSpecification
        """
        return self._discount_specification

    @discount_specification.setter
    def discount_specification(self, discount_specification):
        """Sets the discount_specification of this DiscountRule.


        :param discount_specification: The discount_specification of this DiscountRule.  # noqa: E501
        :type: DiscountSpecification
        """

        self._discount_specification = discount_specification

    @property
    def max_discount_amount(self):
        """Gets the max_discount_amount of this DiscountRule.  # noqa: E501


        :return: The max_discount_amount of this DiscountRule.  # noqa: E501
        :rtype: Amount
        """
        return self._max_discount_amount

    @max_discount_amount.setter
    def max_discount_amount(self, max_discount_amount):
        """Sets the max_discount_amount of this DiscountRule.


        :param max_discount_amount: The max_discount_amount of this DiscountRule.  # noqa: E501
        :type: Amount
        """

        self._max_discount_amount = max_discount_amount

    @property
    def rule_order(self):
        """Gets the rule_order of this DiscountRule.  # noqa: E501

        This field indicates the order in which the <b>discountRules</b> are presented. The value specified for this field must equal the associated <b>minQuantity</b> value. <br><br><i>Required if </i> you are creating a volume pricing promotion.  # noqa: E501

        :return: The rule_order of this DiscountRule.  # noqa: E501
        :rtype: int
        """
        return self._rule_order

    @rule_order.setter
    def rule_order(self, rule_order):
        """Sets the rule_order of this DiscountRule.

        This field indicates the order in which the <b>discountRules</b> are presented. The value specified for this field must equal the associated <b>minQuantity</b> value. <br><br><i>Required if </i> you are creating a volume pricing promotion.  # noqa: E501

        :param rule_order: The rule_order of this DiscountRule.  # noqa: E501
        :type: int
        """

        self._rule_order = rule_order

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
        if issubclass(DiscountRule, dict):
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
        if not isinstance(other, DiscountRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
