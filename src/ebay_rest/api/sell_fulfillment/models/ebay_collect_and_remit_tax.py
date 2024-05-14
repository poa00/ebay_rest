# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.20.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EbayCollectAndRemitTax(object):
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
        'amount': 'Amount',
        'ebay_reference': 'EbayTaxReference',
        'tax_type': 'str',
        'collection_method': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'ebay_reference': 'ebayReference',
        'tax_type': 'taxType',
        'collection_method': 'collectionMethod'
    }

    def __init__(self, amount=None, ebay_reference=None, tax_type=None, collection_method=None):  # noqa: E501
        """EbayCollectAndRemitTax - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._ebay_reference = None
        self._tax_type = None
        self._collection_method = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if ebay_reference is not None:
            self.ebay_reference = ebay_reference
        if tax_type is not None:
            self.tax_type = tax_type
        if collection_method is not None:
            self.collection_method = collection_method

    @property
    def amount(self):
        """Gets the amount of this EbayCollectAndRemitTax.  # noqa: E501


        :return: The amount of this EbayCollectAndRemitTax.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EbayCollectAndRemitTax.


        :param amount: The amount of this EbayCollectAndRemitTax.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def ebay_reference(self):
        """Gets the ebay_reference of this EbayCollectAndRemitTax.  # noqa: E501


        :return: The ebay_reference of this EbayCollectAndRemitTax.  # noqa: E501
        :rtype: EbayTaxReference
        """
        return self._ebay_reference

    @ebay_reference.setter
    def ebay_reference(self, ebay_reference):
        """Sets the ebay_reference of this EbayCollectAndRemitTax.


        :param ebay_reference: The ebay_reference of this EbayCollectAndRemitTax.  # noqa: E501
        :type: EbayTaxReference
        """

        self._ebay_reference = ebay_reference

    @property
    def tax_type(self):
        """Gets the tax_type of this EbayCollectAndRemitTax.  # noqa: E501

        The type of tax and fees that eBay will collect and remit to the taxing or fee authority. See the <strong>TaxTypeEnum</strong> type definition for more information about each tax or fee type. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:TaxTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The tax_type of this EbayCollectAndRemitTax.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this EbayCollectAndRemitTax.

        The type of tax and fees that eBay will collect and remit to the taxing or fee authority. See the <strong>TaxTypeEnum</strong> type definition for more information about each tax or fee type. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:TaxTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param tax_type: The tax_type of this EbayCollectAndRemitTax.  # noqa: E501
        :type: str
        """

        self._tax_type = tax_type

    @property
    def collection_method(self):
        """Gets the collection_method of this EbayCollectAndRemitTax.  # noqa: E501

        This field indicates the collection method used to collect the 'Collect and Remit' tax for the order. This field is always returned for orders subject to 'Collect and Remit' tax, and its value is always <code>NET</code>.<br><br><span class=\"tablenote\"><strong>Note:</strong> Although the <strong>collectionMethod</strong> field is returned for all orders subject to 'Collect and Remit' tax, the <strong>collectionMethod</strong> field and the <strong>CollectionMethodEnum</strong> type are not currently of any practical use, although this field may have use in the future. If and when the logic of this field is changed, this note will be updated and a note will also be added to the Release Notes.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:CollectionMethodEnum'>eBay API documentation</a>  # noqa: E501

        :return: The collection_method of this EbayCollectAndRemitTax.  # noqa: E501
        :rtype: str
        """
        return self._collection_method

    @collection_method.setter
    def collection_method(self, collection_method):
        """Sets the collection_method of this EbayCollectAndRemitTax.

        This field indicates the collection method used to collect the 'Collect and Remit' tax for the order. This field is always returned for orders subject to 'Collect and Remit' tax, and its value is always <code>NET</code>.<br><br><span class=\"tablenote\"><strong>Note:</strong> Although the <strong>collectionMethod</strong> field is returned for all orders subject to 'Collect and Remit' tax, the <strong>collectionMethod</strong> field and the <strong>CollectionMethodEnum</strong> type are not currently of any practical use, although this field may have use in the future. If and when the logic of this field is changed, this note will be updated and a note will also be added to the Release Notes.</span> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:CollectionMethodEnum'>eBay API documentation</a>  # noqa: E501

        :param collection_method: The collection_method of this EbayCollectAndRemitTax.  # noqa: E501
        :type: str
        """

        self._collection_method = collection_method

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
        if issubclass(EbayCollectAndRemitTax, dict):
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
        if not isinstance(other, EbayCollectAndRemitTax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
