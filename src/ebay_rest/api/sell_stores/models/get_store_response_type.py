# coding: utf-8

"""
    Store API

    <p>This API provides stores-related resources for third-party developers. These resources let you retrieve basic store information such as store name, description, store url, return store category hierarchy, add,rename,move,delete a single user's eBay store category, and retrieve the processing status of these tasks.</p> <p>The stores resource methods require an access token created with the <a href=\"/api-docs/static/oauth-authorization-code-grant.html\">authorization code grant</a> flow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application)</p>  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetStoreResponseType(object):
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
        'last_opened_time': 'str',
        'logo': 'StoreLogoType',
        'name': 'str',
        'url': 'str',
        'url_path': 'str'
    }

    attribute_map = {
        'description': 'description',
        'last_opened_time': 'lastOpenedTime',
        'logo': 'logo',
        'name': 'name',
        'url': 'url',
        'url_path': 'urlPath'
    }

    def __init__(self, description=None, last_opened_time=None, logo=None, name=None, url=None, url_path=None):  # noqa: E501
        """GetStoreResponseType - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._last_opened_time = None
        self._logo = None
        self._name = None
        self._url = None
        self._url_path = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if last_opened_time is not None:
            self.last_opened_time = last_opened_time
        if logo is not None:
            self.logo = logo
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if url_path is not None:
            self.url_path = url_path

    @property
    def description(self):
        """Gets the description of this GetStoreResponseType.  # noqa: E501

        The seller-provided description of the eBay Store.<br><br> <b>Max length: </b>300  # noqa: E501

        :return: The description of this GetStoreResponseType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetStoreResponseType.

        The seller-provided description of the eBay Store.<br><br> <b>Max length: </b>300  # noqa: E501

        :param description: The description of this GetStoreResponseType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def last_opened_time(self):
        """Gets the last_opened_time of this GetStoreResponseType.  # noqa: E501

        Indicates the time the store was last opened or reopened.  # noqa: E501

        :return: The last_opened_time of this GetStoreResponseType.  # noqa: E501
        :rtype: str
        """
        return self._last_opened_time

    @last_opened_time.setter
    def last_opened_time(self, last_opened_time):
        """Sets the last_opened_time of this GetStoreResponseType.

        Indicates the time the store was last opened or reopened.  # noqa: E501

        :param last_opened_time: The last_opened_time of this GetStoreResponseType.  # noqa: E501
        :type: str
        """

        self._last_opened_time = last_opened_time

    @property
    def logo(self):
        """Gets the logo of this GetStoreResponseType.  # noqa: E501


        :return: The logo of this GetStoreResponseType.  # noqa: E501
        :rtype: StoreLogoType
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this GetStoreResponseType.


        :param logo: The logo of this GetStoreResponseType.  # noqa: E501
        :type: StoreLogoType
        """

        self._logo = logo

    @property
    def name(self):
        """Gets the name of this GetStoreResponseType.  # noqa: E501

        The name of the eBay Store. The name is shown at the top of the Store page.<br><br> <b>Max length: </b>35  # noqa: E501

        :return: The name of this GetStoreResponseType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetStoreResponseType.

        The name of the eBay Store. The name is shown at the top of the Store page.<br><br> <b>Max length: </b>35  # noqa: E501

        :param name: The name of this GetStoreResponseType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this GetStoreResponseType.  # noqa: E501

        The complete URL of the user's store.  # noqa: E501

        :return: The url of this GetStoreResponseType.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GetStoreResponseType.

        The complete URL of the user's store.  # noqa: E501

        :param url: The url of this GetStoreResponseType.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def url_path(self):
        """Gets the url_path of this GetStoreResponseType.  # noqa: E501

        The relative URL path of the Store.<br><br> <b>Max length: </b>58  # noqa: E501

        :return: The url_path of this GetStoreResponseType.  # noqa: E501
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this GetStoreResponseType.

        The relative URL path of the Store.<br><br> <b>Max length: </b>58  # noqa: E501

        :param url_path: The url_path of this GetStoreResponseType.  # noqa: E501
        :type: str
        """

        self._url_path = url_path

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
        if issubclass(GetStoreResponseType, dict):
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
        if not isinstance(other, GetStoreResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
