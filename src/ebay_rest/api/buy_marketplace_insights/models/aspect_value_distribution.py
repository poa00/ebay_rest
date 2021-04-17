# coding: utf-8

"""
    Marketplace Insights API

    <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#Limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> The Marketplace Insights API provides the ability to search for sold items on eBay by keyword, GTIN, category, and product and returns the of sales history of those items.  # noqa: E501

    OpenAPI spec version: v1_beta.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AspectValueDistribution(object):
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
        'localized_aspect_value': 'str',
        'match_count': 'int',
        'refinement_href': 'str'
    }

    attribute_map = {
        'localized_aspect_value': 'localizedAspectValue',
        'match_count': 'matchCount',
        'refinement_href': 'refinementHref'
    }

    def __init__(self, localized_aspect_value=None, match_count=None, refinement_href=None):  # noqa: E501
        """AspectValueDistribution - a model defined in Swagger"""  # noqa: E501
        self._localized_aspect_value = None
        self._match_count = None
        self._refinement_href = None
        self.discriminator = None
        if localized_aspect_value is not None:
            self.localized_aspect_value = localized_aspect_value
        if match_count is not None:
            self.match_count = match_count
        if refinement_href is not None:
            self.refinement_href = refinement_href

    @property
    def localized_aspect_value(self):
        """Gets the localized_aspect_value of this AspectValueDistribution.  # noqa: E501

        The value of an aspect. For example, Red is a value for the aspect Color.  # noqa: E501

        :return: The localized_aspect_value of this AspectValueDistribution.  # noqa: E501
        :rtype: str
        """
        return self._localized_aspect_value

    @localized_aspect_value.setter
    def localized_aspect_value(self, localized_aspect_value):
        """Sets the localized_aspect_value of this AspectValueDistribution.

        The value of an aspect. For example, Red is a value for the aspect Color.  # noqa: E501

        :param localized_aspect_value: The localized_aspect_value of this AspectValueDistribution.  # noqa: E501
        :type: str
        """

        self._localized_aspect_value = localized_aspect_value

    @property
    def match_count(self):
        """Gets the match_count of this AspectValueDistribution.  # noqa: E501

        The number of items with this aspect.  # noqa: E501

        :return: The match_count of this AspectValueDistribution.  # noqa: E501
        :rtype: int
        """
        return self._match_count

    @match_count.setter
    def match_count(self, match_count):
        """Sets the match_count of this AspectValueDistribution.

        The number of items with this aspect.  # noqa: E501

        :param match_count: The match_count of this AspectValueDistribution.  # noqa: E501
        :type: int
        """

        self._match_count = match_count

    @property
    def refinement_href(self):
        """Gets the refinement_href of this AspectValueDistribution.  # noqa: E501

        A HATEOAS reference for this aspect.  # noqa: E501

        :return: The refinement_href of this AspectValueDistribution.  # noqa: E501
        :rtype: str
        """
        return self._refinement_href

    @refinement_href.setter
    def refinement_href(self, refinement_href):
        """Sets the refinement_href of this AspectValueDistribution.

        A HATEOAS reference for this aspect.  # noqa: E501

        :param refinement_href: The refinement_href of this AspectValueDistribution.  # noqa: E501
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
        if issubclass(AspectValueDistribution, dict):
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
        if not isinstance(other, AspectValueDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
