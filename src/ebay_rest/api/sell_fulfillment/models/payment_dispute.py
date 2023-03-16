# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentDispute(object):
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
        'amount': 'SimpleAmount',
        'available_choices': 'list[str]',
        'buyer_provided': 'InfoFromBuyer',
        'buyer_username': 'str',
        'closed_date': 'str',
        'evidence': 'list[DisputeEvidence]',
        'evidence_requests': 'list[EvidenceRequest]',
        'line_items': 'list[OrderLineItems]',
        'monetary_transactions': 'list[MonetaryTransaction]',
        'note': 'str',
        'open_date': 'str',
        'order_id': 'str',
        'payment_dispute_id': 'str',
        'payment_dispute_status': 'str',
        'reason': 'str',
        'resolution': 'PaymentDisputeOutcomeDetail',
        'respond_by_date': 'str',
        'return_address': 'ReturnAddress',
        'revision': 'int',
        'seller_response': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'available_choices': 'availableChoices',
        'buyer_provided': 'buyerProvided',
        'buyer_username': 'buyerUsername',
        'closed_date': 'closedDate',
        'evidence': 'evidence',
        'evidence_requests': 'evidenceRequests',
        'line_items': 'lineItems',
        'monetary_transactions': 'monetaryTransactions',
        'note': 'note',
        'open_date': 'openDate',
        'order_id': 'orderId',
        'payment_dispute_id': 'paymentDisputeId',
        'payment_dispute_status': 'paymentDisputeStatus',
        'reason': 'reason',
        'resolution': 'resolution',
        'respond_by_date': 'respondByDate',
        'return_address': 'returnAddress',
        'revision': 'revision',
        'seller_response': 'sellerResponse'
    }

    def __init__(self, amount=None, available_choices=None, buyer_provided=None, buyer_username=None, closed_date=None, evidence=None, evidence_requests=None, line_items=None, monetary_transactions=None, note=None, open_date=None, order_id=None, payment_dispute_id=None, payment_dispute_status=None, reason=None, resolution=None, respond_by_date=None, return_address=None, revision=None, seller_response=None):  # noqa: E501
        """PaymentDispute - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._available_choices = None
        self._buyer_provided = None
        self._buyer_username = None
        self._closed_date = None
        self._evidence = None
        self._evidence_requests = None
        self._line_items = None
        self._monetary_transactions = None
        self._note = None
        self._open_date = None
        self._order_id = None
        self._payment_dispute_id = None
        self._payment_dispute_status = None
        self._reason = None
        self._resolution = None
        self._respond_by_date = None
        self._return_address = None
        self._revision = None
        self._seller_response = None
        self.discriminator = None
        if amount is not None:
            self.amount = amount
        if available_choices is not None:
            self.available_choices = available_choices
        if buyer_provided is not None:
            self.buyer_provided = buyer_provided
        if buyer_username is not None:
            self.buyer_username = buyer_username
        if closed_date is not None:
            self.closed_date = closed_date
        if evidence is not None:
            self.evidence = evidence
        if evidence_requests is not None:
            self.evidence_requests = evidence_requests
        if line_items is not None:
            self.line_items = line_items
        if monetary_transactions is not None:
            self.monetary_transactions = monetary_transactions
        if note is not None:
            self.note = note
        if open_date is not None:
            self.open_date = open_date
        if order_id is not None:
            self.order_id = order_id
        if payment_dispute_id is not None:
            self.payment_dispute_id = payment_dispute_id
        if payment_dispute_status is not None:
            self.payment_dispute_status = payment_dispute_status
        if reason is not None:
            self.reason = reason
        if resolution is not None:
            self.resolution = resolution
        if respond_by_date is not None:
            self.respond_by_date = respond_by_date
        if return_address is not None:
            self.return_address = return_address
        if revision is not None:
            self.revision = revision
        if seller_response is not None:
            self.seller_response = seller_response

    @property
    def amount(self):
        """Gets the amount of this PaymentDispute.  # noqa: E501


        :return: The amount of this PaymentDispute.  # noqa: E501
        :rtype: SimpleAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentDispute.


        :param amount: The amount of this PaymentDispute.  # noqa: E501
        :type: SimpleAmount
        """

        self._amount = amount

    @property
    def available_choices(self):
        """Gets the available_choices of this PaymentDispute.  # noqa: E501

        The value(s) returned in this array indicate the choices that the seller has when responding to the payment dispute. Once the seller has responded to the payment dispute, this field will no longer be shown, and instead, the <strong>sellerResponse</strong> field will show the decision that the seller made.  # noqa: E501

        :return: The available_choices of this PaymentDispute.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_choices

    @available_choices.setter
    def available_choices(self, available_choices):
        """Sets the available_choices of this PaymentDispute.

        The value(s) returned in this array indicate the choices that the seller has when responding to the payment dispute. Once the seller has responded to the payment dispute, this field will no longer be shown, and instead, the <strong>sellerResponse</strong> field will show the decision that the seller made.  # noqa: E501

        :param available_choices: The available_choices of this PaymentDispute.  # noqa: E501
        :type: list[str]
        """

        self._available_choices = available_choices

    @property
    def buyer_provided(self):
        """Gets the buyer_provided of this PaymentDispute.  # noqa: E501


        :return: The buyer_provided of this PaymentDispute.  # noqa: E501
        :rtype: InfoFromBuyer
        """
        return self._buyer_provided

    @buyer_provided.setter
    def buyer_provided(self, buyer_provided):
        """Sets the buyer_provided of this PaymentDispute.


        :param buyer_provided: The buyer_provided of this PaymentDispute.  # noqa: E501
        :type: InfoFromBuyer
        """

        self._buyer_provided = buyer_provided

    @property
    def buyer_username(self):
        """Gets the buyer_username of this PaymentDispute.  # noqa: E501

        This is the eBay user ID of the buyer that initiated the payment dispute.  # noqa: E501

        :return: The buyer_username of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._buyer_username

    @buyer_username.setter
    def buyer_username(self, buyer_username):
        """Sets the buyer_username of this PaymentDispute.

        This is the eBay user ID of the buyer that initiated the payment dispute.  # noqa: E501

        :param buyer_username: The buyer_username of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._buyer_username = buyer_username

    @property
    def closed_date(self):
        """Gets the closed_date of this PaymentDispute.  # noqa: E501

        The timestamp in this field shows the date/time when the payment dispute was closed, so this field is only returned for payment disputes in the <code>CLOSED</code> state.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The closed_date of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._closed_date

    @closed_date.setter
    def closed_date(self, closed_date):
        """Sets the closed_date of this PaymentDispute.

        The timestamp in this field shows the date/time when the payment dispute was closed, so this field is only returned for payment disputes in the <code>CLOSED</code> state.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param closed_date: The closed_date of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._closed_date = closed_date

    @property
    def evidence(self):
        """Gets the evidence of this PaymentDispute.  # noqa: E501

        This container shows any evidence that has been provided by the seller to contest the payment dispute. Evidence may include shipment tracking information, proof of authentication documentation, image(s) to proof that an item is as described, or financial documentation/invoice.<br><br>This container is only returned if the seller has provided at least one document used as evidence against the payment dispute.  # noqa: E501

        :return: The evidence of this PaymentDispute.  # noqa: E501
        :rtype: list[DisputeEvidence]
        """
        return self._evidence

    @evidence.setter
    def evidence(self, evidence):
        """Sets the evidence of this PaymentDispute.

        This container shows any evidence that has been provided by the seller to contest the payment dispute. Evidence may include shipment tracking information, proof of authentication documentation, image(s) to proof that an item is as described, or financial documentation/invoice.<br><br>This container is only returned if the seller has provided at least one document used as evidence against the payment dispute.  # noqa: E501

        :param evidence: The evidence of this PaymentDispute.  # noqa: E501
        :type: list[DisputeEvidence]
        """

        self._evidence = evidence

    @property
    def evidence_requests(self):
        """Gets the evidence_requests of this PaymentDispute.  # noqa: E501

        This container is returned if one or more evidence documents are being requested from the seller.  # noqa: E501

        :return: The evidence_requests of this PaymentDispute.  # noqa: E501
        :rtype: list[EvidenceRequest]
        """
        return self._evidence_requests

    @evidence_requests.setter
    def evidence_requests(self, evidence_requests):
        """Sets the evidence_requests of this PaymentDispute.

        This container is returned if one or more evidence documents are being requested from the seller.  # noqa: E501

        :param evidence_requests: The evidence_requests of this PaymentDispute.  # noqa: E501
        :type: list[EvidenceRequest]
        """

        self._evidence_requests = evidence_requests

    @property
    def line_items(self):
        """Gets the line_items of this PaymentDispute.  # noqa: E501

        This array is used to identify one or more order line items associated with the payment dispute. There will always be at least one <b>itemId</b>/<b>lineItemId</b> pair returned in this array.  # noqa: E501

        :return: The line_items of this PaymentDispute.  # noqa: E501
        :rtype: list[OrderLineItems]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this PaymentDispute.

        This array is used to identify one or more order line items associated with the payment dispute. There will always be at least one <b>itemId</b>/<b>lineItemId</b> pair returned in this array.  # noqa: E501

        :param line_items: The line_items of this PaymentDispute.  # noqa: E501
        :type: list[OrderLineItems]
        """

        self._line_items = line_items

    @property
    def monetary_transactions(self):
        """Gets the monetary_transactions of this PaymentDispute.  # noqa: E501

        This array provide details about one or more monetary transactions that occur as part of a payment dispute. This array is only returned once one or more monetary transacations occur with a payment dispute.  # noqa: E501

        :return: The monetary_transactions of this PaymentDispute.  # noqa: E501
        :rtype: list[MonetaryTransaction]
        """
        return self._monetary_transactions

    @monetary_transactions.setter
    def monetary_transactions(self, monetary_transactions):
        """Sets the monetary_transactions of this PaymentDispute.

        This array provide details about one or more monetary transactions that occur as part of a payment dispute. This array is only returned once one or more monetary transacations occur with a payment dispute.  # noqa: E501

        :param monetary_transactions: The monetary_transactions of this PaymentDispute.  # noqa: E501
        :type: list[MonetaryTransaction]
        """

        self._monetary_transactions = monetary_transactions

    @property
    def note(self):
        """Gets the note of this PaymentDispute.  # noqa: E501

        This field shows information that the seller provides about the dispute, such as the basis for the dispute, any relevant evidence, tracking numbers, and so forth.<br><br>This field is limited to 1000 characters.  # noqa: E501

        :return: The note of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PaymentDispute.

        This field shows information that the seller provides about the dispute, such as the basis for the dispute, any relevant evidence, tracking numbers, and so forth.<br><br>This field is limited to 1000 characters.  # noqa: E501

        :param note: The note of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def open_date(self):
        """Gets the open_date of this PaymentDispute.  # noqa: E501

        The timestamp in this field shows the date/time when the payment dispute was opened. This field is returned for payment disputes in all states.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The open_date of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._open_date

    @open_date.setter
    def open_date(self, open_date):
        """Sets the open_date of this PaymentDispute.

        The timestamp in this field shows the date/time when the payment dispute was opened. This field is returned for payment disputes in all states.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param open_date: The open_date of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._open_date = open_date

    @property
    def order_id(self):
        """Gets the order_id of this PaymentDispute.  # noqa: E501

        This is the unique identifier of the order involved in the payment dispute.  # noqa: E501

        :return: The order_id of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this PaymentDispute.

        This is the unique identifier of the order involved in the payment dispute.  # noqa: E501

        :param order_id: The order_id of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def payment_dispute_id(self):
        """Gets the payment_dispute_id of this PaymentDispute.  # noqa: E501

        This is the unique identifier of the payment dispute. This is the same identifier that is passed in to the call URI. This identifier is automatically created by eBay once the payment dispute comes into the eBay system.  # noqa: E501

        :return: The payment_dispute_id of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._payment_dispute_id

    @payment_dispute_id.setter
    def payment_dispute_id(self, payment_dispute_id):
        """Sets the payment_dispute_id of this PaymentDispute.

        This is the unique identifier of the payment dispute. This is the same identifier that is passed in to the call URI. This identifier is automatically created by eBay once the payment dispute comes into the eBay system.  # noqa: E501

        :param payment_dispute_id: The payment_dispute_id of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._payment_dispute_id = payment_dispute_id

    @property
    def payment_dispute_status(self):
        """Gets the payment_dispute_status of this PaymentDispute.  # noqa: E501

        The enumeration value in this field gives the current status of the payment dispute. The status of a payment dispute partially determines other fields that are returned in the response. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:DisputeStateEnum'>eBay API documentation</a>  # noqa: E501

        :return: The payment_dispute_status of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._payment_dispute_status

    @payment_dispute_status.setter
    def payment_dispute_status(self, payment_dispute_status):
        """Sets the payment_dispute_status of this PaymentDispute.

        The enumeration value in this field gives the current status of the payment dispute. The status of a payment dispute partially determines other fields that are returned in the response. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:DisputeStateEnum'>eBay API documentation</a>  # noqa: E501

        :param payment_dispute_status: The payment_dispute_status of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._payment_dispute_status = payment_dispute_status

    @property
    def reason(self):
        """Gets the reason of this PaymentDispute.  # noqa: E501

        The enumeration value in this field gives the reason why the buyer initiated the payment dispute. See <strong>DisputeReasonEnum</strong> type for a description of the supported reasons that buyers can give for initiating a payment dispute. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:DisputeReasonEnum'>eBay API documentation</a>  # noqa: E501

        :return: The reason of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PaymentDispute.

        The enumeration value in this field gives the reason why the buyer initiated the payment dispute. See <strong>DisputeReasonEnum</strong> type for a description of the supported reasons that buyers can give for initiating a payment dispute. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:DisputeReasonEnum'>eBay API documentation</a>  # noqa: E501

        :param reason: The reason of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def resolution(self):
        """Gets the resolution of this PaymentDispute.  # noqa: E501


        :return: The resolution of this PaymentDispute.  # noqa: E501
        :rtype: PaymentDisputeOutcomeDetail
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this PaymentDispute.


        :param resolution: The resolution of this PaymentDispute.  # noqa: E501
        :type: PaymentDisputeOutcomeDetail
        """

        self._resolution = resolution

    @property
    def respond_by_date(self):
        """Gets the respond_by_date of this PaymentDispute.  # noqa: E501

        The timestamp in this field shows the date/time when the seller must response to a payment dispute, so this field is only returned for payment disputes in the <code>ACTION_NEEDED</code> state. For payment disputes that currently require action by the seller, that same seller should look at the <strong>availableChoices</strong> array to see the available actions.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :return: The respond_by_date of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._respond_by_date

    @respond_by_date.setter
    def respond_by_date(self, respond_by_date):
        """Sets the respond_by_date of this PaymentDispute.

        The timestamp in this field shows the date/time when the seller must response to a payment dispute, so this field is only returned for payment disputes in the <code>ACTION_NEEDED</code> state. For payment disputes that currently require action by the seller, that same seller should look at the <strong>availableChoices</strong> array to see the available actions.<br><br>The timestamps returned here use the ISO-8601 24-hour date and time format, and the time zone used is Universal Coordinated Time (UTC), also known as Greenwich Mean Time (GMT), or Zulu. The ISO-8601 format looks like this: <em>yyyy-MM-ddThh:mm.ss.sssZ</em>. An example would be <code>2019-08-04T19:09:02.768Z</code>.  # noqa: E501

        :param respond_by_date: The respond_by_date of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._respond_by_date = respond_by_date

    @property
    def return_address(self):
        """Gets the return_address of this PaymentDispute.  # noqa: E501


        :return: The return_address of this PaymentDispute.  # noqa: E501
        :rtype: ReturnAddress
        """
        return self._return_address

    @return_address.setter
    def return_address(self, return_address):
        """Sets the return_address of this PaymentDispute.


        :param return_address: The return_address of this PaymentDispute.  # noqa: E501
        :type: ReturnAddress
        """

        self._return_address = return_address

    @property
    def revision(self):
        """Gets the revision of this PaymentDispute.  # noqa: E501

        This integer value indicates the revision number of the payment dispute. Each time an action is taken against a payment dispute, this integer value increases by 1.  # noqa: E501

        :return: The revision of this PaymentDispute.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this PaymentDispute.

        This integer value indicates the revision number of the payment dispute. Each time an action is taken against a payment dispute, this integer value increases by 1.  # noqa: E501

        :param revision: The revision of this PaymentDispute.  # noqa: E501
        :type: int
        """

        self._revision = revision

    @property
    def seller_response(self):
        """Gets the seller_response of this PaymentDispute.  # noqa: E501

        The enumeration value returned in this field indicates how the seller has responded to the payment dispute. The seller has the option of accepting the payment dispute and agreeing to issue a refund, accepting the payment dispute and agreeing to issue a refund as long as the buyer returns the item, or contesting the payment dispute. This field is returned as soon as the seller makes an initial decision on the payment dispute. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:SellerResponseEnum'>eBay API documentation</a>  # noqa: E501

        :return: The seller_response of this PaymentDispute.  # noqa: E501
        :rtype: str
        """
        return self._seller_response

    @seller_response.setter
    def seller_response(self, seller_response):
        """Sets the seller_response of this PaymentDispute.

        The enumeration value returned in this field indicates how the seller has responded to the payment dispute. The seller has the option of accepting the payment dispute and agreeing to issue a refund, accepting the payment dispute and agreeing to issue a refund as long as the buyer returns the item, or contesting the payment dispute. This field is returned as soon as the seller makes an initial decision on the payment dispute. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/api:SellerResponseEnum'>eBay API documentation</a>  # noqa: E501

        :param seller_response: The seller_response of this PaymentDispute.  # noqa: E501
        :type: str
        """

        self._seller_response = seller_response

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
        if issubclass(PaymentDispute, dict):
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
        if not isinstance(other, PaymentDispute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
