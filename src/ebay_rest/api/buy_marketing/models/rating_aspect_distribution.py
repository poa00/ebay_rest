# coding: utf-8

"""
    Buy Marketing API

    The Marketing API retrieves eBay products based on a metric, such as Best Selling, as well as products that were also bought and also viewed.  # noqa: E501

    OpenAPI spec version: v1_beta.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RatingAspectDistribution(object):
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
        'count': 'int',
        'percentage': 'str',
        'value': 'str'
    }

    attribute_map = {
        'count': 'count',
        'percentage': 'percentage',
        'value': 'value'
    }

    def __init__(self, count=None, percentage=None, value=None):  # noqa: E501
        """RatingAspectDistribution - a model defined in Swagger"""  # noqa: E501
        self._count = None
        self._percentage = None
        self._value = None
        self.discriminator = None
        if count is not None:
            self.count = count
        if percentage is not None:
            self.percentage = percentage
        if value is not None:
            self.value = value

    @property
    def count(self):
        """Gets the count of this RatingAspectDistribution.  # noqa: E501

        The number of eBay users that choose this rating aspect value.  # noqa: E501

        :return: The count of this RatingAspectDistribution.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this RatingAspectDistribution.

        The number of eBay users that choose this rating aspect value.  # noqa: E501

        :param count: The count of this RatingAspectDistribution.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def percentage(self):
        """Gets the percentage of this RatingAspectDistribution.  # noqa: E501

        The percentage of the aspect rating value. <br /><br /> <b> ratingAspectDistributions.percentage</b> =  <b> ratingAspectDistributions.count</b> /  <b>ratingAspects.count</b>  # noqa: E501

        :return: The percentage of this RatingAspectDistribution.  # noqa: E501
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this RatingAspectDistribution.

        The percentage of the aspect rating value. <br /><br /> <b> ratingAspectDistributions.percentage</b> =  <b> ratingAspectDistributions.count</b> /  <b>ratingAspects.count</b>  # noqa: E501

        :param percentage: The percentage of this RatingAspectDistribution.  # noqa: E501
        :type: str
        """

        self._percentage = percentage

    @property
    def value(self):
        """Gets the value of this RatingAspectDistribution.  # noqa: E501

        The rating aspect. For example: TRUE or FALSE  # noqa: E501

        :return: The value of this RatingAspectDistribution.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RatingAspectDistribution.

        The rating aspect. For example: TRUE or FALSE  # noqa: E501

        :param value: The value of this RatingAspectDistribution.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(RatingAspectDistribution, dict):
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
        if not isinstance(other, RatingAspectDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
