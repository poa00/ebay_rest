# coding: utf-8

"""
    Deal API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units. For information on how to obtain access to this API in production, see the <a href=\"/../api-docs/buy/static/buy-requirements.html\" target=\"_blank\">Buy APIs Requirements</a>.</span><br /><br />This API allows third-party developers to search for and retrieve details about eBay deals and events, as well as the items associated with those deals and events.  # noqa: E501

    OpenAPI spec version: v1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Terms(object):
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
        'full_text': 'str',
        'summary': 'str'
    }

    attribute_map = {
        'full_text': 'fullText',
        'summary': 'summary'
    }

    def __init__(self, full_text=None, summary=None):  # noqa: E501
        """Terms - a model defined in Swagger"""  # noqa: E501
        self._full_text = None
        self._summary = None
        self.discriminator = None
        if full_text is not None:
            self.full_text = full_text
        if summary is not None:
            self.summary = summary

    @property
    def full_text(self):
        """Gets the full_text of this Terms.  # noqa: E501

        A full-text description of the terms.  # noqa: E501

        :return: The full_text of this Terms.  # noqa: E501
        :rtype: str
        """
        return self._full_text

    @full_text.setter
    def full_text(self, full_text):
        """Sets the full_text of this Terms.

        A full-text description of the terms.  # noqa: E501

        :param full_text: The full_text of this Terms.  # noqa: E501
        :type: str
        """

        self._full_text = full_text

    @property
    def summary(self):
        """Gets the summary of this Terms.  # noqa: E501

        A summarized description of the terms.  # noqa: E501

        :return: The summary of this Terms.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Terms.

        A summarized description of the terms.  # noqa: E501

        :param summary: The summary of this Terms.  # noqa: E501
        :type: str
        """

        self._summary = summary

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
        if issubclass(Terms, dict):
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
        if not isinstance(other, Terms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
