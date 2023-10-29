# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.20.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DisputeEvidence(object):
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
        'files': 'list[FileInfo]',
        'line_items': 'list[OrderLineItems]',
        'provided_date': 'str',
        'request_date': 'str',
        'respond_by_date': 'str',
        'shipment_tracking': 'list[TrackingInfo]'
    }

    attribute_map = {
        'evidence_id': 'evidenceId',
        'evidence_type': 'evidenceType',
        'files': 'files',
        'line_items': 'lineItems',
        'provided_date': 'providedDate',
        'request_date': 'requestDate',
        'respond_by_date': 'respondByDate',
        'shipment_tracking': 'shipmentTracking'
    }

    def __init__(self, evidence_id=None, evidence_type=None, files=None, line_items=None, provided_date=None, request_date=None, respond_by_date=None, shipment_tracking=None):  # noqa: E501
        """DisputeEvidence - a model defined in Swagger"""  # noqa: E501
        self._evidence_id = None
        self._evidence_type = None
        self._files = None
        self._line_items = None
        self._provided_date = None
        self._request_date = None
        self._respond_by_date = None
        self._shipment_tracking = None
        self.discriminator = None
        if evidence_id is not None:
            self.evidence_id = evidence_id
        if evidence_type is not None:
            self.evidence_type = evidence_type
        if files is not None:
            self.files = files
        if line_items is not None:
            self.line_items = line_items
        if provided_date is not None:
            self.provided_date = provided_date
        if request_date is not None:
            self.request_date = request_date
        if respond_by_date is not None:
            self.respond_by_date = respond_by_date
        if shipment_tracking is not None:
            self.shipment_tracking = shipment_tracking

    @property
    def evidence_id(self):
        """Gets the evidence_id of this DisputeEvidence.  # noqa: E501

        Unique identifier of the evidential file set. Potentially, each evidential file set can have more than one file, that is why there is this file set identifier, and then an identifier for each file within this file set.  # noqa: E501

        :return: The evidence_id of this DisputeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._evidence_id

    @evidence_id.setter
    def evidence_id(self, evidence_id):
        """Sets the evidence_id of this DisputeEvidence.

        Unique identifier of the evidential file set. Potentially, each evidential file set can have more than one file, that is why there is this file set identifier, and then an identifier for each file within this file set.  # noqa: E501

        :param evidence_id: The evidence_id of this DisputeEvidence.  # noqa: E501
        :type: str
        """

        self._evidence_id = evidence_id

    @property
    def evidence_type(self):
        """Gets the evidence_type of this DisputeEvidence.  # noqa: E501

        This enumeration value shows the type of evidential file provided. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:EvidenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The evidence_type of this DisputeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._evidence_type

    @evidence_type.setter
    def evidence_type(self, evidence_type):
        """Sets the evidence_type of this DisputeEvidence.

        This enumeration value shows the type of evidential file provided. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:EvidenceTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param evidence_type: The evidence_type of this DisputeEvidence.  # noqa: E501
        :type: str
        """

        self._evidence_type = evidence_type

    @property
    def files(self):
        """Gets the files of this DisputeEvidence.  # noqa: E501

        This array shows the name, ID, file type, and upload date for each provided file.  # noqa: E501

        :return: The files of this DisputeEvidence.  # noqa: E501
        :rtype: list[FileInfo]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this DisputeEvidence.

        This array shows the name, ID, file type, and upload date for each provided file.  # noqa: E501

        :param files: The files of this DisputeEvidence.  # noqa: E501
        :type: list[FileInfo]
        """

        self._files = files

    @property
    def line_items(self):
        """Gets the line_items of this DisputeEvidence.  # noqa: E501

        This array shows one or more order line items associated with the evidential document that has been provided.  # noqa: E501

        :return: The line_items of this DisputeEvidence.  # noqa: E501
        :rtype: list[OrderLineItems]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this DisputeEvidence.

        This array shows one or more order line items associated with the evidential document that has been provided.  # noqa: E501

        :param line_items: The line_items of this DisputeEvidence.  # noqa: E501
        :type: list[OrderLineItems]
        """

        self._line_items = line_items

    @property
    def provided_date(self):
        """Gets the provided_date of this DisputeEvidence.  # noqa: E501

        The timestamp in this field shows the date/time when the seller provided a requested evidential document to eBay. <br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The provided_date of this DisputeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._provided_date

    @provided_date.setter
    def provided_date(self, provided_date):
        """Sets the provided_date of this DisputeEvidence.

        The timestamp in this field shows the date/time when the seller provided a requested evidential document to eBay. <br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param provided_date: The provided_date of this DisputeEvidence.  # noqa: E501
        :type: str
        """

        self._provided_date = provided_date

    @property
    def request_date(self):
        """Gets the request_date of this DisputeEvidence.  # noqa: E501

        The timestamp in this field shows the date/time when eBay requested the evidential document from the seller in response to a payment dispute. <br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The request_date of this DisputeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._request_date

    @request_date.setter
    def request_date(self, request_date):
        """Sets the request_date of this DisputeEvidence.

        The timestamp in this field shows the date/time when eBay requested the evidential document from the seller in response to a payment dispute. <br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param request_date: The request_date of this DisputeEvidence.  # noqa: E501
        :type: str
        """

        self._request_date = request_date

    @property
    def respond_by_date(self):
        """Gets the respond_by_date of this DisputeEvidence.  # noqa: E501

        The timestamp in this field shows the date/time when the seller was expected to provide a requested evidential document to eBay.  <br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The respond_by_date of this DisputeEvidence.  # noqa: E501
        :rtype: str
        """
        return self._respond_by_date

    @respond_by_date.setter
    def respond_by_date(self, respond_by_date):
        """Sets the respond_by_date of this DisputeEvidence.

        The timestamp in this field shows the date/time when the seller was expected to provide a requested evidential document to eBay.  <br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param respond_by_date: The respond_by_date of this DisputeEvidence.  # noqa: E501
        :type: str
        """

        self._respond_by_date = respond_by_date

    @property
    def shipment_tracking(self):
        """Gets the shipment_tracking of this DisputeEvidence.  # noqa: E501

        This array shows the shipping carrier and shipment tracking number associated with each shipment package of the order. This array is returned under the <strong>evidence</strong> container if the seller has provided shipment tracking information as evidence to support <code>PROOF_OF_DELIVERY</code> for an INR-related payment dispute.  # noqa: E501

        :return: The shipment_tracking of this DisputeEvidence.  # noqa: E501
        :rtype: list[TrackingInfo]
        """
        return self._shipment_tracking

    @shipment_tracking.setter
    def shipment_tracking(self, shipment_tracking):
        """Sets the shipment_tracking of this DisputeEvidence.

        This array shows the shipping carrier and shipment tracking number associated with each shipment package of the order. This array is returned under the <strong>evidence</strong> container if the seller has provided shipment tracking information as evidence to support <code>PROOF_OF_DELIVERY</code> for an INR-related payment dispute.  # noqa: E501

        :param shipment_tracking: The shipment_tracking of this DisputeEvidence.  # noqa: E501
        :type: list[TrackingInfo]
        """

        self._shipment_tracking = shipment_tracking

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
        if issubclass(DisputeEvidence, dict):
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
        if not isinstance(other, DisputeEvidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
