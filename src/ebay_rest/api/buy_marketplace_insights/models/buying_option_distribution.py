# coding: utf-8

"""
    Marketplace Insights API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"/api-docs/static/versioning.html#limited \" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units. For information on how to obtain access to this API in production, see the <a href=\"/../api-docs/buy/static/buy-requirements.html\" target=\"_blank\">Buy APIs Requirements</a>.</span>  <p>The Marketplace Insights API provides the ability to search for sold items on eBay by keyword, GTIN, category, and product and returns the of sales history of those items.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BuyingOptionDistribution(object):
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
        'buying_option': 'str',
        'match_count': 'int',
        'refinement_href': 'str'
    }

    attribute_map = {
        'buying_option': 'buyingOption',
        'match_count': 'matchCount',
        'refinement_href': 'refinementHref'
    }

    def __init__(self, buying_option=None, match_count=None, refinement_href=None):  # noqa: E501
        """BuyingOptionDistribution - a model defined in Swagger"""  # noqa: E501
        self._buying_option = None
        self._match_count = None
        self._refinement_href = None
        self.discriminator = None
        if buying_option is not None:
            self.buying_option = buying_option
        if match_count is not None:
            self.match_count = match_count
        if refinement_href is not None:
            self.refinement_href = refinement_href

    @property
    def buying_option(self):
        """Gets the buying_option of this BuyingOptionDistribution.  # noqa: E501


        :return: The buying_option of this BuyingOptionDistribution.  # noqa: E501
        :rtype: str
        """
        return self._buying_option

    @buying_option.setter
    def buying_option(self, buying_option):
        """Sets the buying_option of this BuyingOptionDistribution.


        :param buying_option: The buying_option of this BuyingOptionDistribution.  # noqa: E501
        :type: str
        """

        self._buying_option = buying_option

    @property
    def match_count(self):
        """Gets the match_count of this BuyingOptionDistribution.  # noqa: E501

        The number of items having this buying option.  # noqa: E501

        :return: The match_count of this BuyingOptionDistribution.  # noqa: E501
        :rtype: int
        """
        return self._match_count

    @match_count.setter
    def match_count(self, match_count):
        """Sets the match_count of this BuyingOptionDistribution.

        The number of items having this buying option.  # noqa: E501

        :param match_count: The match_count of this BuyingOptionDistribution.  # noqa: E501
        :type: int
        """

        self._match_count = match_count

    @property
    def refinement_href(self):
        """Gets the refinement_href of this BuyingOptionDistribution.  # noqa: E501

        The HATEOAS reference for this buying option.  # noqa: E501

        :return: The refinement_href of this BuyingOptionDistribution.  # noqa: E501
        :rtype: str
        """
        return self._refinement_href

    @refinement_href.setter
    def refinement_href(self, refinement_href):
        """Sets the refinement_href of this BuyingOptionDistribution.

        The HATEOAS reference for this buying option.  # noqa: E501

        :param refinement_href: The refinement_href of this BuyingOptionDistribution.  # noqa: E501
        :type: str
        """

        self._refinement_href = refinement_href

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
        if issubclass(BuyingOptionDistribution, dict):
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
        if not isinstance(other, BuyingOptionDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
