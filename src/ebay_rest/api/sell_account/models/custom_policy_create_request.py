# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (seller-defined custom policies and eBay business policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CustomPolicyCreateRequest(object):
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
        'description': 'str',
        'label': 'str',
        'name': 'str',
        'policy_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'label': 'label',
        'name': 'name',
        'policy_type': 'policyType'
    }

    def __init__(self, description=None, label=None, name=None, policy_type=None):  # noqa: E501
        """CustomPolicyCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._label = None
        self._name = None
        self._policy_type = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if policy_type is not None:
            self.policy_type = policy_type

    @property
    def description(self):
        """Gets the description of this CustomPolicyCreateRequest.  # noqa: E501

        Details of the seller's specific policy and terms for this policy.<br><br><b>Max length:</b> 15,000  # noqa: E501

        :return: The description of this CustomPolicyCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomPolicyCreateRequest.

        Details of the seller's specific policy and terms for this policy.<br><br><b>Max length:</b> 15,000  # noqa: E501

        :param description: The description of this CustomPolicyCreateRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def label(self):
        """Gets the label of this CustomPolicyCreateRequest.  # noqa: E501

        Customer-facing label shown on View Item pages for items to which the policy applies. This seller-defined string is displayed as a system-generated hyperlink pointing to detailed policy information.<br><br><b>Max length:</b> 65  # noqa: E501

        :return: The label of this CustomPolicyCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CustomPolicyCreateRequest.

        Customer-facing label shown on View Item pages for items to which the policy applies. This seller-defined string is displayed as a system-generated hyperlink pointing to detailed policy information.<br><br><b>Max length:</b> 65  # noqa: E501

        :param label: The label of this CustomPolicyCreateRequest.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this CustomPolicyCreateRequest.  # noqa: E501

        The seller-defined name for the custom policy. Names must be unique for policies assigned to the same seller, policy type, and eBay marketplace.<br /><span class=\"tablenote\"><strong>Note:</strong> This field is visible only to the seller. </span><br/><br/><b>Max length:</b> 65  # noqa: E501

        :return: The name of this CustomPolicyCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomPolicyCreateRequest.

        The seller-defined name for the custom policy. Names must be unique for policies assigned to the same seller, policy type, and eBay marketplace.<br /><span class=\"tablenote\"><strong>Note:</strong> This field is visible only to the seller. </span><br/><br/><b>Max length:</b> 65  # noqa: E501

        :param name: The name of this CustomPolicyCreateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def policy_type(self):
        """Gets the policy_type of this CustomPolicyCreateRequest.  # noqa: E501

        Specifies the type of custom policy being created. <br/><br/>Two Custom Policy types are supported: <ul><li>Product Compliance (PRODUCT_COMPLIANCE)</li> <li>Takeback (TAKE_BACK)</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:CustomPolicyTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The policy_type of this CustomPolicyCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this CustomPolicyCreateRequest.

        Specifies the type of custom policy being created. <br/><br/>Two Custom Policy types are supported: <ul><li>Product Compliance (PRODUCT_COMPLIANCE)</li> <li>Takeback (TAKE_BACK)</li></ul> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:CustomPolicyTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param policy_type: The policy_type of this CustomPolicyCreateRequest.  # noqa: E501
        :type: str
        """

        self._policy_type = policy_type

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
        if issubclass(CustomPolicyCreateRequest, dict):
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
        if not isinstance(other, CustomPolicyCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
