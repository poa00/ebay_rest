# coding: utf-8

"""
     Seller Service Metrics API 

    The <i>Analytics API</i> provides data and information about a seller and their eBay business.  <br><br>The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating.  <br><br>The three resources in the Analytics API provide the following data and information: <ul><li><b>Customer Service Metric</b> &ndash; Returns benchmark data and a metric rating pertaining to a seller's customer service performance as compared to other seller's in the same peer group.</li> <li><b>Traffic Report</b> &ndash; Returns data and information that shows how buyers are engaging with a seller's listings.</li> <li><b>Seller Standards Profile</b> &ndash; Returns information pertaining to a seller's profile rating.</li></ul> Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers.  <br><br>For details on using this API, see <a href=\"/api-docs/sell/static/performance/analyzing-performance.html\" title=\"Selling Integration Guide\">Analyzing seller performance</a>.  # noqa: E501

    OpenAPI spec version: 1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MetricDistribution(object):
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
        'basis': 'str',
        'data': 'list[Distribution]'
    }

    attribute_map = {
        'basis': 'basis',
        'data': 'data'
    }

    def __init__(self, basis=None, data=None):  # noqa: E501
        """MetricDistribution - a model defined in Swagger"""  # noqa: E501
        self._basis = None
        self._data = None
        self.discriminator = None
        if basis is not None:
            self.basis = basis
        if data is not None:
            self.data = data

    @property
    def basis(self):
        """Gets the basis of this MetricDistribution.  # noqa: E501

        This field returns the basis, or the method, by which the metric rating is calculated.  # noqa: E501

        :return: The basis of this MetricDistribution.  # noqa: E501
        :rtype: str
        """
        return self._basis

    @basis.setter
    def basis(self, basis):
        """Sets the basis of this MetricDistribution.

        This field returns the basis, or the method, by which the metric rating is calculated.  # noqa: E501

        :param basis: The basis of this MetricDistribution.  # noqa: E501
        :type: str
        """

        self._basis = basis

    @property
    def data(self):
        """Gets the data of this MetricDistribution.  # noqa: E501

        This field returns a list of name/value pairs, where the <b>name</b> indicates the distribution being rated and the <b>value</b> indicates the count of seller transactions that meet the distribution criteria.  # noqa: E501

        :return: The data of this MetricDistribution.  # noqa: E501
        :rtype: list[Distribution]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MetricDistribution.

        This field returns a list of name/value pairs, where the <b>name</b> indicates the distribution being rated and the <b>value</b> indicates the count of seller transactions that meet the distribution criteria.  # noqa: E501

        :param data: The data of this MetricDistribution.  # noqa: E501
        :type: list[Distribution]
        """

        self._data = data

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
        if issubclass(MetricDistribution, dict):
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
        if not isinstance(other, MetricDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
