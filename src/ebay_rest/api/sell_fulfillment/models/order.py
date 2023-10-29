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

class Order(object):
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
        'buyer': 'Buyer',
        'buyer_checkout_notes': 'str',
        'cancel_status': 'CancelStatus',
        'creation_date': 'str',
        'ebay_collect_and_remit_tax': 'bool',
        'fulfillment_hrefs': 'list[str]',
        'fulfillment_start_instructions': 'list[FulfillmentStartInstruction]',
        'last_modified_date': 'str',
        'legacy_order_id': 'str',
        'line_items': 'list[LineItem]',
        'order_fulfillment_status': 'str',
        'order_id': 'str',
        'order_payment_status': 'str',
        'payment_summary': 'PaymentSummary',
        'pricing_summary': 'PricingSummary',
        'program': 'Program',
        'sales_record_reference': 'str',
        'seller_id': 'str',
        'total_fee_basis_amount': 'Amount',
        'total_marketplace_fee': 'Amount'
    }

    attribute_map = {
        'buyer': 'buyer',
        'buyer_checkout_notes': 'buyerCheckoutNotes',
        'cancel_status': 'cancelStatus',
        'creation_date': 'creationDate',
        'ebay_collect_and_remit_tax': 'ebayCollectAndRemitTax',
        'fulfillment_hrefs': 'fulfillmentHrefs',
        'fulfillment_start_instructions': 'fulfillmentStartInstructions',
        'last_modified_date': 'lastModifiedDate',
        'legacy_order_id': 'legacyOrderId',
        'line_items': 'lineItems',
        'order_fulfillment_status': 'orderFulfillmentStatus',
        'order_id': 'orderId',
        'order_payment_status': 'orderPaymentStatus',
        'payment_summary': 'paymentSummary',
        'pricing_summary': 'pricingSummary',
        'program': 'program',
        'sales_record_reference': 'salesRecordReference',
        'seller_id': 'sellerId',
        'total_fee_basis_amount': 'totalFeeBasisAmount',
        'total_marketplace_fee': 'totalMarketplaceFee'
    }

    def __init__(self, buyer=None, buyer_checkout_notes=None, cancel_status=None, creation_date=None, ebay_collect_and_remit_tax=None, fulfillment_hrefs=None, fulfillment_start_instructions=None, last_modified_date=None, legacy_order_id=None, line_items=None, order_fulfillment_status=None, order_id=None, order_payment_status=None, payment_summary=None, pricing_summary=None, program=None, sales_record_reference=None, seller_id=None, total_fee_basis_amount=None, total_marketplace_fee=None):  # noqa: E501
        """Order - a model defined in Swagger"""  # noqa: E501
        self._buyer = None
        self._buyer_checkout_notes = None
        self._cancel_status = None
        self._creation_date = None
        self._ebay_collect_and_remit_tax = None
        self._fulfillment_hrefs = None
        self._fulfillment_start_instructions = None
        self._last_modified_date = None
        self._legacy_order_id = None
        self._line_items = None
        self._order_fulfillment_status = None
        self._order_id = None
        self._order_payment_status = None
        self._payment_summary = None
        self._pricing_summary = None
        self._program = None
        self._sales_record_reference = None
        self._seller_id = None
        self._total_fee_basis_amount = None
        self._total_marketplace_fee = None
        self.discriminator = None
        if buyer is not None:
            self.buyer = buyer
        if buyer_checkout_notes is not None:
            self.buyer_checkout_notes = buyer_checkout_notes
        if cancel_status is not None:
            self.cancel_status = cancel_status
        if creation_date is not None:
            self.creation_date = creation_date
        if ebay_collect_and_remit_tax is not None:
            self.ebay_collect_and_remit_tax = ebay_collect_and_remit_tax
        if fulfillment_hrefs is not None:
            self.fulfillment_hrefs = fulfillment_hrefs
        if fulfillment_start_instructions is not None:
            self.fulfillment_start_instructions = fulfillment_start_instructions
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if legacy_order_id is not None:
            self.legacy_order_id = legacy_order_id
        if line_items is not None:
            self.line_items = line_items
        if order_fulfillment_status is not None:
            self.order_fulfillment_status = order_fulfillment_status
        if order_id is not None:
            self.order_id = order_id
        if order_payment_status is not None:
            self.order_payment_status = order_payment_status
        if payment_summary is not None:
            self.payment_summary = payment_summary
        if pricing_summary is not None:
            self.pricing_summary = pricing_summary
        if program is not None:
            self.program = program
        if sales_record_reference is not None:
            self.sales_record_reference = sales_record_reference
        if seller_id is not None:
            self.seller_id = seller_id
        if total_fee_basis_amount is not None:
            self.total_fee_basis_amount = total_fee_basis_amount
        if total_marketplace_fee is not None:
            self.total_marketplace_fee = total_marketplace_fee

    @property
    def buyer(self):
        """Gets the buyer of this Order.  # noqa: E501


        :return: The buyer of this Order.  # noqa: E501
        :rtype: Buyer
        """
        return self._buyer

    @buyer.setter
    def buyer(self, buyer):
        """Sets the buyer of this Order.


        :param buyer: The buyer of this Order.  # noqa: E501
        :type: Buyer
        """

        self._buyer = buyer

    @property
    def buyer_checkout_notes(self):
        """Gets the buyer_checkout_notes of this Order.  # noqa: E501

        This field contains any comments that the buyer left for the seller about the order during checkout process. This field is only returned if a buyer left comments at checkout time.   # noqa: E501

        :return: The buyer_checkout_notes of this Order.  # noqa: E501
        :rtype: str
        """
        return self._buyer_checkout_notes

    @buyer_checkout_notes.setter
    def buyer_checkout_notes(self, buyer_checkout_notes):
        """Sets the buyer_checkout_notes of this Order.

        This field contains any comments that the buyer left for the seller about the order during checkout process. This field is only returned if a buyer left comments at checkout time.   # noqa: E501

        :param buyer_checkout_notes: The buyer_checkout_notes of this Order.  # noqa: E501
        :type: str
        """

        self._buyer_checkout_notes = buyer_checkout_notes

    @property
    def cancel_status(self):
        """Gets the cancel_status of this Order.  # noqa: E501


        :return: The cancel_status of this Order.  # noqa: E501
        :rtype: CancelStatus
        """
        return self._cancel_status

    @cancel_status.setter
    def cancel_status(self, cancel_status):
        """Sets the cancel_status of this Order.


        :param cancel_status: The cancel_status of this Order.  # noqa: E501
        :type: CancelStatus
        """

        self._cancel_status = cancel_status

    @property
    def creation_date(self):
        """Gets the creation_date of this Order.  # noqa: E501

        The date and time that the order was created. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :return: The creation_date of this Order.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Order.

        The date and time that the order was created. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :param creation_date: The creation_date of this Order.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def ebay_collect_and_remit_tax(self):
        """Gets the ebay_collect_and_remit_tax of this Order.  # noqa: E501

        This field is only returned if <code>true</code>, and indicates that eBay will collect tax (US state-mandated sales tax, Federal and Provincial Sales Tax in Canada, 'Goods and Services' tax in Canada, Australia, and New Zealand, and VAT collected for UK and EU countries,) for at least one line item in the order, and remit the tax to the taxing authority of the buyer's residence. If this field is returned, the seller should search for one or more <strong>ebayCollectAndRemitTaxes</strong> containers at the line item level to get more information about the type of tax and the amount.  # noqa: E501

        :return: The ebay_collect_and_remit_tax of this Order.  # noqa: E501
        :rtype: bool
        """
        return self._ebay_collect_and_remit_tax

    @ebay_collect_and_remit_tax.setter
    def ebay_collect_and_remit_tax(self, ebay_collect_and_remit_tax):
        """Sets the ebay_collect_and_remit_tax of this Order.

        This field is only returned if <code>true</code>, and indicates that eBay will collect tax (US state-mandated sales tax, Federal and Provincial Sales Tax in Canada, 'Goods and Services' tax in Canada, Australia, and New Zealand, and VAT collected for UK and EU countries,) for at least one line item in the order, and remit the tax to the taxing authority of the buyer's residence. If this field is returned, the seller should search for one or more <strong>ebayCollectAndRemitTaxes</strong> containers at the line item level to get more information about the type of tax and the amount.  # noqa: E501

        :param ebay_collect_and_remit_tax: The ebay_collect_and_remit_tax of this Order.  # noqa: E501
        :type: bool
        """

        self._ebay_collect_and_remit_tax = ebay_collect_and_remit_tax

    @property
    def fulfillment_hrefs(self):
        """Gets the fulfillment_hrefs of this Order.  # noqa: E501

        This array contains a list of one or more <strong>getShippingFulfillment</strong> call URIs that can be used to retrieve shipping fulfillments that have been set up for the order.  # noqa: E501

        :return: The fulfillment_hrefs of this Order.  # noqa: E501
        :rtype: list[str]
        """
        return self._fulfillment_hrefs

    @fulfillment_hrefs.setter
    def fulfillment_hrefs(self, fulfillment_hrefs):
        """Sets the fulfillment_hrefs of this Order.

        This array contains a list of one or more <strong>getShippingFulfillment</strong> call URIs that can be used to retrieve shipping fulfillments that have been set up for the order.  # noqa: E501

        :param fulfillment_hrefs: The fulfillment_hrefs of this Order.  # noqa: E501
        :type: list[str]
        """

        self._fulfillment_hrefs = fulfillment_hrefs

    @property
    def fulfillment_start_instructions(self):
        """Gets the fulfillment_start_instructions of this Order.  # noqa: E501

        This container consists of a set of specifications for fulfilling the order, including the type of fulfillment, shipping carrier and service, shipping address, and estimated delivery window. These instructions are derived from the buyer's and seller's eBay account preferences, the listing parameters, and the buyer's checkout selections. The seller can use them as a starting point for packaging, addressing, and shipping the order.<br><br><span class=\"tablenote\"><strong>Note:</strong> Although this container is presented as an array, it currently returns only one set of fulfillment specifications. Additional array members will be supported in future functionality.</span>  # noqa: E501

        :return: The fulfillment_start_instructions of this Order.  # noqa: E501
        :rtype: list[FulfillmentStartInstruction]
        """
        return self._fulfillment_start_instructions

    @fulfillment_start_instructions.setter
    def fulfillment_start_instructions(self, fulfillment_start_instructions):
        """Sets the fulfillment_start_instructions of this Order.

        This container consists of a set of specifications for fulfilling the order, including the type of fulfillment, shipping carrier and service, shipping address, and estimated delivery window. These instructions are derived from the buyer's and seller's eBay account preferences, the listing parameters, and the buyer's checkout selections. The seller can use them as a starting point for packaging, addressing, and shipping the order.<br><br><span class=\"tablenote\"><strong>Note:</strong> Although this container is presented as an array, it currently returns only one set of fulfillment specifications. Additional array members will be supported in future functionality.</span>  # noqa: E501

        :param fulfillment_start_instructions: The fulfillment_start_instructions of this Order.  # noqa: E501
        :type: list[FulfillmentStartInstruction]
        """

        self._fulfillment_start_instructions = fulfillment_start_instructions

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this Order.  # noqa: E501

        The date and time that the order was last modified. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :return: The last_modified_date of this Order.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this Order.

        The date and time that the order was last modified. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :param last_modified_date: The last_modified_date of this Order.  # noqa: E501
        :type: str
        """

        self._last_modified_date = last_modified_date

    @property
    def legacy_order_id(self):
        """Gets the legacy_order_id of this Order.  # noqa: E501

        The unique identifier of the order in legacy format, as traditionally used by the Trading API (and other legacy APIs). Both the <b>orderId</b> field and this field are always returned.  # noqa: E501

        :return: The legacy_order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._legacy_order_id

    @legacy_order_id.setter
    def legacy_order_id(self, legacy_order_id):
        """Sets the legacy_order_id of this Order.

        The unique identifier of the order in legacy format, as traditionally used by the Trading API (and other legacy APIs). Both the <b>orderId</b> field and this field are always returned.  # noqa: E501

        :param legacy_order_id: The legacy_order_id of this Order.  # noqa: E501
        :type: str
        """

        self._legacy_order_id = legacy_order_id

    @property
    def line_items(self):
        """Gets the line_items of this Order.  # noqa: E501

        This array contains the details for all line items that comprise the order.  # noqa: E501

        :return: The line_items of this Order.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Order.

        This array contains the details for all line items that comprise the order.  # noqa: E501

        :param line_items: The line_items of this Order.  # noqa: E501
        :type: list[LineItem]
        """

        self._line_items = line_items

    @property
    def order_fulfillment_status(self):
        """Gets the order_fulfillment_status of this Order.  # noqa: E501

        The degree to which fulfillment of the order is complete. See the <strong>OrderFulfillmentStatus</strong> type definition for more information about each possible fulfillment state. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:OrderFulfillmentStatus'>eBay API documentation</a>  # noqa: E501

        :return: The order_fulfillment_status of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_fulfillment_status

    @order_fulfillment_status.setter
    def order_fulfillment_status(self, order_fulfillment_status):
        """Sets the order_fulfillment_status of this Order.

        The degree to which fulfillment of the order is complete. See the <strong>OrderFulfillmentStatus</strong> type definition for more information about each possible fulfillment state. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:OrderFulfillmentStatus'>eBay API documentation</a>  # noqa: E501

        :param order_fulfillment_status: The order_fulfillment_status of this Order.  # noqa: E501
        :type: str
        """

        self._order_fulfillment_status = order_fulfillment_status

    @property
    def order_id(self):
        """Gets the order_id of this Order.  # noqa: E501

        The unique identifier of the order. Both the <b>legacyOrderId</b> field (traditionally used by Trading and other legacy APIS) and this field are always returned.  # noqa: E501

        :return: The order_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order.

        The unique identifier of the order. Both the <b>legacyOrderId</b> field (traditionally used by Trading and other legacy APIS) and this field are always returned.  # noqa: E501

        :param order_id: The order_id of this Order.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def order_payment_status(self):
        """Gets the order_payment_status of this Order.  # noqa: E501

        The enumeration value returned in this field indicates the current payment status of an order, or in case of a refund request, the current status of the refund. See the <strong>OrderPaymentStatusEnum</strong> type definition for more information about each possible payment/refund state. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:OrderPaymentStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The order_payment_status of this Order.  # noqa: E501
        :rtype: str
        """
        return self._order_payment_status

    @order_payment_status.setter
    def order_payment_status(self, order_payment_status):
        """Sets the order_payment_status of this Order.

        The enumeration value returned in this field indicates the current payment status of an order, or in case of a refund request, the current status of the refund. See the <strong>OrderPaymentStatusEnum</strong> type definition for more information about each possible payment/refund state. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:OrderPaymentStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param order_payment_status: The order_payment_status of this Order.  # noqa: E501
        :type: str
        """

        self._order_payment_status = order_payment_status

    @property
    def payment_summary(self):
        """Gets the payment_summary of this Order.  # noqa: E501


        :return: The payment_summary of this Order.  # noqa: E501
        :rtype: PaymentSummary
        """
        return self._payment_summary

    @payment_summary.setter
    def payment_summary(self, payment_summary):
        """Sets the payment_summary of this Order.


        :param payment_summary: The payment_summary of this Order.  # noqa: E501
        :type: PaymentSummary
        """

        self._payment_summary = payment_summary

    @property
    def pricing_summary(self):
        """Gets the pricing_summary of this Order.  # noqa: E501


        :return: The pricing_summary of this Order.  # noqa: E501
        :rtype: PricingSummary
        """
        return self._pricing_summary

    @pricing_summary.setter
    def pricing_summary(self, pricing_summary):
        """Sets the pricing_summary of this Order.


        :param pricing_summary: The pricing_summary of this Order.  # noqa: E501
        :type: PricingSummary
        """

        self._pricing_summary = pricing_summary

    @property
    def program(self):
        """Gets the program of this Order.  # noqa: E501


        :return: The program of this Order.  # noqa: E501
        :rtype: Program
        """
        return self._program

    @program.setter
    def program(self, program):
        """Sets the program of this Order.


        :param program: The program of this Order.  # noqa: E501
        :type: Program
        """

        self._program = program

    @property
    def sales_record_reference(self):
        """Gets the sales_record_reference of this Order.  # noqa: E501

        An eBay-generated identifier that is used to identify and manage orders through the Selling Manager and Selling Manager Pro tools. This order identifier can also be found on the Orders grid page and in the Sales Record pages in Seller Hub. A <strong>salesRecordReference</strong> number is only generated and returned at the order level, and not at the order line item level.<br><br> In cases where the seller does not have a Selling Manager or Selling Manager Pro subscription nor access to Seller Hub, this field may not be returned.  # noqa: E501

        :return: The sales_record_reference of this Order.  # noqa: E501
        :rtype: str
        """
        return self._sales_record_reference

    @sales_record_reference.setter
    def sales_record_reference(self, sales_record_reference):
        """Sets the sales_record_reference of this Order.

        An eBay-generated identifier that is used to identify and manage orders through the Selling Manager and Selling Manager Pro tools. This order identifier can also be found on the Orders grid page and in the Sales Record pages in Seller Hub. A <strong>salesRecordReference</strong> number is only generated and returned at the order level, and not at the order line item level.<br><br> In cases where the seller does not have a Selling Manager or Selling Manager Pro subscription nor access to Seller Hub, this field may not be returned.  # noqa: E501

        :param sales_record_reference: The sales_record_reference of this Order.  # noqa: E501
        :type: str
        """

        self._sales_record_reference = sales_record_reference

    @property
    def seller_id(self):
        """Gets the seller_id of this Order.  # noqa: E501

        The unique eBay user ID of the seller who sold the order.  # noqa: E501

        :return: The seller_id of this Order.  # noqa: E501
        :rtype: str
        """
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        """Sets the seller_id of this Order.

        The unique eBay user ID of the seller who sold the order.  # noqa: E501

        :param seller_id: The seller_id of this Order.  # noqa: E501
        :type: str
        """

        self._seller_id = seller_id

    @property
    def total_fee_basis_amount(self):
        """Gets the total_fee_basis_amount of this Order.  # noqa: E501


        :return: The total_fee_basis_amount of this Order.  # noqa: E501
        :rtype: Amount
        """
        return self._total_fee_basis_amount

    @total_fee_basis_amount.setter
    def total_fee_basis_amount(self, total_fee_basis_amount):
        """Sets the total_fee_basis_amount of this Order.


        :param total_fee_basis_amount: The total_fee_basis_amount of this Order.  # noqa: E501
        :type: Amount
        """

        self._total_fee_basis_amount = total_fee_basis_amount

    @property
    def total_marketplace_fee(self):
        """Gets the total_marketplace_fee of this Order.  # noqa: E501


        :return: The total_marketplace_fee of this Order.  # noqa: E501
        :rtype: Amount
        """
        return self._total_marketplace_fee

    @total_marketplace_fee.setter
    def total_marketplace_fee(self, total_marketplace_fee):
        """Sets the total_marketplace_fee of this Order.


        :param total_marketplace_fee: The total_marketplace_fee of this Order.  # noqa: E501
        :type: Amount
        """

        self._total_marketplace_fee = total_marketplace_fee

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
