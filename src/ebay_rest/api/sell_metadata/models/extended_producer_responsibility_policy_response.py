# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExtendedProducerResponsibilityPolicyResponse(object):
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
        'extended_producer_responsibilities': 'list[ExtendedProducerResponsibilityPolicy]',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'extended_producer_responsibilities': 'extendedProducerResponsibilities',
        'warnings': 'warnings'
    }

    def __init__(self, extended_producer_responsibilities=None, warnings=None):  # noqa: E501
        """ExtendedProducerResponsibilityPolicyResponse - a model defined in Swagger"""  # noqa: E501
        self._extended_producer_responsibilities = None
        self._warnings = None
        self.discriminator = None
        if extended_producer_responsibilities is not None:
            self.extended_producer_responsibilities = extended_producer_responsibilities
        if warnings is not None:
            self.warnings = warnings

    @property
    def extended_producer_responsibilities(self):
        """Gets the extended_producer_responsibilities of this ExtendedProducerResponsibilityPolicyResponse.  # noqa: E501

        An array of response fields detailing the Extended Producer Responsibility policies supported for the specified marketplace.  # noqa: E501

        :return: The extended_producer_responsibilities of this ExtendedProducerResponsibilityPolicyResponse.  # noqa: E501
        :rtype: list[ExtendedProducerResponsibilityPolicy]
        """
        return self._extended_producer_responsibilities

    @extended_producer_responsibilities.setter
    def extended_producer_responsibilities(self, extended_producer_responsibilities):
        """Sets the extended_producer_responsibilities of this ExtendedProducerResponsibilityPolicyResponse.

        An array of response fields detailing the Extended Producer Responsibility policies supported for the specified marketplace.  # noqa: E501

        :param extended_producer_responsibilities: The extended_producer_responsibilities of this ExtendedProducerResponsibilityPolicyResponse.  # noqa: E501
        :type: list[ExtendedProducerResponsibilityPolicy]
        """

        self._extended_producer_responsibilities = extended_producer_responsibilities

    @property
    def warnings(self):
        """Gets the warnings of this ExtendedProducerResponsibilityPolicyResponse.  # noqa: E501

        A collection of warnings generated for the request.  # noqa: E501

        :return: The warnings of this ExtendedProducerResponsibilityPolicyResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this ExtendedProducerResponsibilityPolicyResponse.

        A collection of warnings generated for the request.  # noqa: E501

        :param warnings: The warnings of this ExtendedProducerResponsibilityPolicyResponse.  # noqa: E501
        :type: list[Error]
        """

        self._warnings = warnings

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
        if issubclass(ExtendedProducerResponsibilityPolicyResponse, dict):
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
        if not isinstance(other, ExtendedProducerResponsibilityPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
