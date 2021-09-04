# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.4.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Error(object):
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
        'category': 'str',
        'domain': 'str',
        'error_id': 'int',
        'input_ref_ids': 'list[str]',
        'long_message': 'str',
        'message': 'str',
        'output_ref_ids': 'list[str]',
        'parameters': 'list[ErrorParameter]',
        'subdomain': 'str'
    }

    attribute_map = {
        'category': 'category',
        'domain': 'domain',
        'error_id': 'errorId',
        'input_ref_ids': 'inputRefIds',
        'long_message': 'longMessage',
        'message': 'message',
        'output_ref_ids': 'outputRefIds',
        'parameters': 'parameters',
        'subdomain': 'subdomain'
    }

    def __init__(self, category=None, domain=None, error_id=None, input_ref_ids=None, long_message=None, message=None, output_ref_ids=None, parameters=None, subdomain=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501
        self._category = None
        self._domain = None
        self._error_id = None
        self._input_ref_ids = None
        self._long_message = None
        self._message = None
        self._output_ref_ids = None
        self._parameters = None
        self._subdomain = None
        self.discriminator = None
        if category is not None:
            self.category = category
        if domain is not None:
            self.domain = domain
        if error_id is not None:
            self.error_id = error_id
        if input_ref_ids is not None:
            self.input_ref_ids = input_ref_ids
        if long_message is not None:
            self.long_message = long_message
        if message is not None:
            self.message = message
        if output_ref_ids is not None:
            self.output_ref_ids = output_ref_ids
        if parameters is not None:
            self.parameters = parameters
        if subdomain is not None:
            self.subdomain = subdomain

    @property
    def category(self):
        """Gets the category of this Error.  # noqa: E501

        The category type for this error or warning. It takes an ErrorCategory object which can have one of three values: Application: Indicates an exception or error occurred in the application code or at runtime. Examples include catching an exception in a service's business logic, system failures, or request errors from a dependency. Business: Used when your service or a dependent service refused to continue processing on the resource because of a business rule violation such as &quot;Seller does not ship item to Antarctica&quot; or &quot;Buyer ineligible to purchase an alcoholic item&quot;. Business errors are not syntactical input errors. Request: Used when there is anything wrong with the request, such as authentication, syntactical errors, rate limiting or missing headers, bad HTTP header values, and so on.  # noqa: E501

        :return: The category of this Error.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Error.

        The category type for this error or warning. It takes an ErrorCategory object which can have one of three values: Application: Indicates an exception or error occurred in the application code or at runtime. Examples include catching an exception in a service's business logic, system failures, or request errors from a dependency. Business: Used when your service or a dependent service refused to continue processing on the resource because of a business rule violation such as &quot;Seller does not ship item to Antarctica&quot; or &quot;Buyer ineligible to purchase an alcoholic item&quot;. Business errors are not syntactical input errors. Request: Used when there is anything wrong with the request, such as authentication, syntactical errors, rate limiting or missing headers, bad HTTP header values, and so on.  # noqa: E501

        :param category: The category of this Error.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def domain(self):
        """Gets the domain of this Error.  # noqa: E501

        Name of the domain containing the service or application.  # noqa: E501

        :return: The domain of this Error.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Error.

        Name of the domain containing the service or application.  # noqa: E501

        :param domain: The domain of this Error.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def error_id(self):
        """Gets the error_id of this Error.  # noqa: E501

        A positive integer that uniquely identifies the specific error condition that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.  # noqa: E501

        :return: The error_id of this Error.  # noqa: E501
        :rtype: int
        """
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        """Sets the error_id of this Error.

        A positive integer that uniquely identifies the specific error condition that occurred. Your application can use error codes as identifiers in your customized error-handling algorithms.  # noqa: E501

        :param error_id: The error_id of this Error.  # noqa: E501
        :type: int
        """

        self._error_id = error_id

    @property
    def input_ref_ids(self):
        """Gets the input_ref_ids of this Error.  # noqa: E501

        Identifies specific request elements associated with the error, if any. inputRefId's response is format specific. For JSON, use JSONPath notation.  # noqa: E501

        :return: The input_ref_ids of this Error.  # noqa: E501
        :rtype: list[str]
        """
        return self._input_ref_ids

    @input_ref_ids.setter
    def input_ref_ids(self, input_ref_ids):
        """Sets the input_ref_ids of this Error.

        Identifies specific request elements associated with the error, if any. inputRefId's response is format specific. For JSON, use JSONPath notation.  # noqa: E501

        :param input_ref_ids: The input_ref_ids of this Error.  # noqa: E501
        :type: list[str]
        """

        self._input_ref_ids = input_ref_ids

    @property
    def long_message(self):
        """Gets the long_message of this Error.  # noqa: E501

        An expanded version of message that should be around 100-200 characters long, but is not required to be such.  # noqa: E501

        :return: The long_message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._long_message

    @long_message.setter
    def long_message(self, long_message):
        """Sets the long_message of this Error.

        An expanded version of message that should be around 100-200 characters long, but is not required to be such.  # noqa: E501

        :param long_message: The long_message of this Error.  # noqa: E501
        :type: str
        """

        self._long_message = long_message

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501

        An end user and app developer friendly device agnostic message. It explains what the error or warning is, and how to fix it (in a general sense). Its value is at most 50 characters long. If applicable, the value is localized in the end user's requested locale.  # noqa: E501

        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.

        An end user and app developer friendly device agnostic message. It explains what the error or warning is, and how to fix it (in a general sense). Its value is at most 50 characters long. If applicable, the value is localized in the end user's requested locale.  # noqa: E501

        :param message: The message of this Error.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def output_ref_ids(self):
        """Gets the output_ref_ids of this Error.  # noqa: E501

        Identifies specific response elements associated with the error, if any. Path format is the same as inputRefId.  # noqa: E501

        :return: The output_ref_ids of this Error.  # noqa: E501
        :rtype: list[str]
        """
        return self._output_ref_ids

    @output_ref_ids.setter
    def output_ref_ids(self, output_ref_ids):
        """Sets the output_ref_ids of this Error.

        Identifies specific response elements associated with the error, if any. Path format is the same as inputRefId.  # noqa: E501

        :param output_ref_ids: The output_ref_ids of this Error.  # noqa: E501
        :type: list[str]
        """

        self._output_ref_ids = output_ref_ids

    @property
    def parameters(self):
        """Gets the parameters of this Error.  # noqa: E501

        This optional complex field type contains a list of one or more context-specific ErrorParameter objects, with each item in the list entry being a parameter (or input field name) that caused an error condition. Each ErrorParameter object consists of two fields, a name and a value.  # noqa: E501

        :return: The parameters of this Error.  # noqa: E501
        :rtype: list[ErrorParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Error.

        This optional complex field type contains a list of one or more context-specific ErrorParameter objects, with each item in the list entry being a parameter (or input field name) that caused an error condition. Each ErrorParameter object consists of two fields, a name and a value.  # noqa: E501

        :param parameters: The parameters of this Error.  # noqa: E501
        :type: list[ErrorParameter]
        """

        self._parameters = parameters

    @property
    def subdomain(self):
        """Gets the subdomain of this Error.  # noqa: E501

        Name of the domain's subsystem or subdivision. For example, checkout is a subdomain in the buying domain.  # noqa: E501

        :return: The subdomain of this Error.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this Error.

        Name of the domain's subsystem or subdivision. For example, checkout is a subdomain in the buying domain.  # noqa: E501

        :param subdomain: The subdomain of this Error.  # noqa: E501
        :type: str
        """

        self._subdomain = subdomain

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
        if issubclass(Error, dict):
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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
