# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.17.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OfferSkuResponse(object):
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
        'errors': 'list[Error]',
        'format': 'str',
        'marketplace_id': 'str',
        'offer_id': 'str',
        'sku': 'str',
        'status_code': 'int',
        'warnings': 'list[Error]'
    }

    attribute_map = {
        'errors': 'errors',
        'format': 'format',
        'marketplace_id': 'marketplaceId',
        'offer_id': 'offerId',
        'sku': 'sku',
        'status_code': 'statusCode',
        'warnings': 'warnings'
    }

    def __init__(self, errors=None, format=None, marketplace_id=None, offer_id=None, sku=None, status_code=None, warnings=None):  # noqa: E501
        """OfferSkuResponse - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._format = None
        self._marketplace_id = None
        self._offer_id = None
        self._sku = None
        self._status_code = None
        self._warnings = None
        self.discriminator = None
        if errors is not None:
            self.errors = errors
        if format is not None:
            self.format = format
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if offer_id is not None:
            self.offer_id = offer_id
        if sku is not None:
            self.sku = sku
        if status_code is not None:
            self.status_code = status_code
        if warnings is not None:
            self.warnings = warnings

    @property
    def errors(self):
        """Gets the errors of this OfferSkuResponse.  # noqa: E501

        This container will be returned at the offer level, and will contain one or more errors if any occurred with the attempted creation of the corresponding offer.  # noqa: E501

        :return: The errors of this OfferSkuResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this OfferSkuResponse.

        This container will be returned at the offer level, and will contain one or more errors if any occurred with the attempted creation of the corresponding offer.  # noqa: E501

        :param errors: The errors of this OfferSkuResponse.  # noqa: E501
        :type: list[Error]
        """

        self._errors = errors

    @property
    def format(self):
        """Gets the format of this OfferSkuResponse.  # noqa: E501

        This enumeration value indicates the listing format of the offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:FormatTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The format of this OfferSkuResponse.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this OfferSkuResponse.

        This enumeration value indicates the listing format of the offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:FormatTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param format: The format of this OfferSkuResponse.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this OfferSkuResponse.  # noqa: E501

        This enumeration value is the unique identifier of the eBay marketplace for which the offer will be made available. This enumeration value should be the same for all offers since the <strong>bulkCreateOffer</strong> method can only be used to create offers for one eBay marketplace at a time. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:MarketplaceEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this OfferSkuResponse.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this OfferSkuResponse.

        This enumeration value is the unique identifier of the eBay marketplace for which the offer will be made available. This enumeration value should be the same for all offers since the <strong>bulkCreateOffer</strong> method can only be used to create offers for one eBay marketplace at a time. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:MarketplaceEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this OfferSkuResponse.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def offer_id(self):
        """Gets the offer_id of this OfferSkuResponse.  # noqa: E501

        The unique identifier of the newly-created offer. This identifier should be automatically created by eBay if the creation of the offer was successful. It is not returned if the creation of the offer was not successful. In which case, the user may want to scan the corresponding <strong>errors</strong> and/or <strong>warnings</strong> container to see what the issue may be.  # noqa: E501

        :return: The offer_id of this OfferSkuResponse.  # noqa: E501
        :rtype: str
        """
        return self._offer_id

    @offer_id.setter
    def offer_id(self, offer_id):
        """Sets the offer_id of this OfferSkuResponse.

        The unique identifier of the newly-created offer. This identifier should be automatically created by eBay if the creation of the offer was successful. It is not returned if the creation of the offer was not successful. In which case, the user may want to scan the corresponding <strong>errors</strong> and/or <strong>warnings</strong> container to see what the issue may be.  # noqa: E501

        :param offer_id: The offer_id of this OfferSkuResponse.  # noqa: E501
        :type: str
        """

        self._offer_id = offer_id

    @property
    def sku(self):
        """Gets the sku of this OfferSkuResponse.  # noqa: E501

        The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The <strong>sku</strong> value is required for each product offer that the seller is trying to create, and it is always returned to identified the product that is associated with the offer.  # noqa: E501

        :return: The sku of this OfferSkuResponse.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this OfferSkuResponse.

        The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The <strong>sku</strong> value is required for each product offer that the seller is trying to create, and it is always returned to identified the product that is associated with the offer.  # noqa: E501

        :param sku: The sku of this OfferSkuResponse.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def status_code(self):
        """Gets the status_code of this OfferSkuResponse.  # noqa: E501

        The integer value returned in this field is the http status code. If an offer is created successfully, the value returned in this field should be <code>200</code>. A user can view the <strong>HTTP status codes</strong> section for information on other status codes that may be returned with the <strong>bulkCreateOffer</strong> method.  # noqa: E501

        :return: The status_code of this OfferSkuResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this OfferSkuResponse.

        The integer value returned in this field is the http status code. If an offer is created successfully, the value returned in this field should be <code>200</code>. A user can view the <strong>HTTP status codes</strong> section for information on other status codes that may be returned with the <strong>bulkCreateOffer</strong> method.  # noqa: E501

        :param status_code: The status_code of this OfferSkuResponse.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def warnings(self):
        """Gets the warnings of this OfferSkuResponse.  # noqa: E501

        This container will be returned at the offer level, and will contain one or more warnings if any occurred with the attempted creation of the corresponding offer. Note that it is possible that an offer can be created successfully even if one or more warnings are triggered.  # noqa: E501

        :return: The warnings of this OfferSkuResponse.  # noqa: E501
        :rtype: list[Error]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this OfferSkuResponse.

        This container will be returned at the offer level, and will contain one or more warnings if any occurred with the attempted creation of the corresponding offer. Note that it is possible that an offer can be created successfully even if one or more warnings are triggered.  # noqa: E501

        :param warnings: The warnings of this OfferSkuResponse.  # noqa: E501
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
        if issubclass(OfferSkuResponse, dict):
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
        if not isinstance(other, OfferSkuResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
