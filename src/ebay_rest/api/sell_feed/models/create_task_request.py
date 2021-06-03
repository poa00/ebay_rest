# coding: utf-8

"""
    Feed API

    <p>The <strong>Feed API</strong> lets sellers upload input files, download reports and files including their status, filter reports using URI parameters, and retrieve customer service metrics task details.</p>  # noqa: E501

    OpenAPI spec version: v1.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateTaskRequest(object):
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
        'feed_type': 'str',
        'schema_version': 'str'
    }

    attribute_map = {
        'feed_type': 'feedType',
        'schema_version': 'schemaVersion'
    }

    def __init__(self, feed_type=None, schema_version=None):  # noqa: E501
        """CreateTaskRequest - a model defined in Swagger"""  # noqa: E501
        self._feed_type = None
        self._schema_version = None
        self.discriminator = None
        if feed_type is not None:
            self.feed_type = feed_type
        if schema_version is not None:
            self.schema_version = schema_version

    @property
    def feed_type(self):
        """Gets the feed_type of this CreateTaskRequest.  # noqa: E501

        The feed type associated with the task. Only use a feedType that is available for your API. Available feed types: LMS FeedTypes: All LMS feed types except LMS_ORDER_REPORT and LMS_ACTIVE_INVENTORY_REPORT File Exchange FeedTypes  # noqa: E501

        :return: The feed_type of this CreateTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._feed_type

    @feed_type.setter
    def feed_type(self, feed_type):
        """Sets the feed_type of this CreateTaskRequest.

        The feed type associated with the task. Only use a feedType that is available for your API. Available feed types: LMS FeedTypes: All LMS feed types except LMS_ORDER_REPORT and LMS_ACTIVE_INVENTORY_REPORT File Exchange FeedTypes  # noqa: E501

        :param feed_type: The feed_type of this CreateTaskRequest.  # noqa: E501
        :type: str
        """

        self._feed_type = feed_type

    @property
    def schema_version(self):
        """Gets the schema_version of this CreateTaskRequest.  # noqa: E501

        The schemaVersion/version number of the file format (use the schema version of the API to which you are programming): LMS Version Details / Schema Version File Exchange Schema Version  # noqa: E501

        :return: The schema_version of this CreateTaskRequest.  # noqa: E501
        :rtype: str
        """
        return self._schema_version

    @schema_version.setter
    def schema_version(self, schema_version):
        """Sets the schema_version of this CreateTaskRequest.

        The schemaVersion/version number of the file format (use the schema version of the API to which you are programming): LMS Version Details / Schema Version File Exchange Schema Version  # noqa: E501

        :param schema_version: The schema_version of this CreateTaskRequest.  # noqa: E501
        :type: str
        """

        self._schema_version = schema_version

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
        if issubclass(CreateTaskRequest, dict):
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
        if not isinstance(other, CreateTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
