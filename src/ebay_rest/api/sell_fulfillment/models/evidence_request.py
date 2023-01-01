# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EvidenceRequest(object):
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
        'evidence_id': 'str',
        'evidence_type': 'str',
        'line_items': 'list[OrderLineItems]',
        'request_date': 'str',
        'respond_by_date': 'str'
    }

    attribute_map = {
        'evidence_id': 'evidenceId',
        'evidence_type': 'evidenceType',
        'line_items': 'lineItems',
        'request_date': 'requestDate',
        'respond_by_date': 'respondByDate'
    }

    def __init__(self, evidence_id=None, evidence_type=None, line_items=None, request_date=None, respond_by_date=None):  # noqa: E501
        """EvidenceRequest - a model defined in Swagger"""  # noqa: E501
        self._evidence_id = None
        self._evidence_type = None
        self._line_items = None
        self._request_date = None
        self._respond_by_date = None
        self.discriminator = None
        if evidence_id is not None:
            self.evidence_id = evidence_id
        if evidence_type is not None:
            self.evidence_type = evidence_type
        if line_items is not None:
            self.line_items = line_items
        if request_date is not None:
            self.request_date = request_date
        if respond_by_date is not None:
            self.respond_by_date = respond_by_date

    @property
    def evidence_id(self):
        """Gets the evidence_id of this EvidenceRequest.  # noqa: E501

        Unique identifier of the evidential file set. Potentially, each evidential file set can have more than one file, that is why there is this file set identifier, and then an identifier for each file within this file set.  # noqa: E501

        :return: The evidence_id of this EvidenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._evidence_id

    @evidence_id.setter
    def evidence_id(self, evidence_id):
        """Sets the evidence_id of this EvidenceRequest.

        Unique identifier of the evidential file set. Potentially, each evidential file set can have more than one file, that is why there is this file set identifier, and then an identifier for each file within this file set.  # noqa: E501

        :param evidence_id: The evidence_id of this EvidenceRequest.  # noqa: E501
        :type: str
        """

        self._evidence_id = evidence_id

    @property
    def evidence_type(self):
        """Gets the evidence_type of this EvidenceRequest.  # noqa: E501

        This enumeration value shows the type of evidential document provided. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:EvidenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The evidence_type of this EvidenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._evidence_type

    @evidence_type.setter
    def evidence_type(self, evidence_type):
        """Sets the evidence_type of this EvidenceRequest.

        This enumeration value shows the type of evidential document provided. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:EvidenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param evidence_type: The evidence_type of this EvidenceRequest.  # noqa: E501
        :type: str
        """

        self._evidence_type = evidence_type

    @property
    def line_items(self):
        """Gets the line_items of this EvidenceRequest.  # noqa: E501

        This array shows one or more order line items associated with the evidential document that has been provided.  # noqa: E501

        :return: The line_items of this EvidenceRequest.  # noqa: E501
        :rtype: list[OrderLineItems]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this EvidenceRequest.

        This array shows one or more order line items associated with the evidential document that has been provided.  # noqa: E501

        :param line_items: The line_items of this EvidenceRequest.  # noqa: E501
        :type: list[OrderLineItems]
        """

        self._line_items = line_items

    @property
    def request_date(self):
        """Gets the request_date of this EvidenceRequest.  # noqa: E501

        The timestamp in this field shows the date/time when eBay requested the evidential document from the seller in response to a payment dispute. <br/><br/>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The request_date of this EvidenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_date

    @request_date.setter
    def request_date(self, request_date):
        """Sets the request_date of this EvidenceRequest.

        The timestamp in this field shows the date/time when eBay requested the evidential document from the seller in response to a payment dispute. <br/><br/>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param request_date: The request_date of this EvidenceRequest.  # noqa: E501
        :type: str
        """

        self._request_date = request_date

    @property
    def respond_by_date(self):
        """Gets the respond_by_date of this EvidenceRequest.  # noqa: E501

        The timestamp in this field shows the date/time when the seller is expected to provide a requested evidential document to eBay.  <br/><br/>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The respond_by_date of this EvidenceRequest.  # noqa: E501
        :rtype: str
        """
        return self._respond_by_date

    @respond_by_date.setter
    def respond_by_date(self, respond_by_date):
        """Sets the respond_by_date of this EvidenceRequest.

        The timestamp in this field shows the date/time when the seller is expected to provide a requested evidential document to eBay.  <br/><br/>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param respond_by_date: The respond_by_date of this EvidenceRequest.  # noqa: E501
        :type: str
        """

        self._respond_by_date = respond_by_date

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
        if issubclass(EvidenceRequest, dict):
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
        if not isinstance(other, EvidenceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
