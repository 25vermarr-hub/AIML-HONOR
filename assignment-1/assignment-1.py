from abc import ABC, abstractmethod

class paymentmehod(ABC):

    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class razorpaycardpayment(paymentmehod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Razorpay Card: {self.card_number}"

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Razorpay Card.")
        return True

class razorpayupipayment(paymentmehod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return f"Razorpay UPI: {self.upi_id}"

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Razorpay UPI.")
        return True

class stripecardpayment(paymentmehod):

    def __init__(self, card_number):
        self.card_number = card_number

    def get_details(self):
        return f"Stripe Card: {self.card_number}"

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Stripe Card.")
        return True

class stripeupipayment(paymentmehod):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def get_details(self):
        return f"Stripe UPI: {self.upi_id}"

    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Stripe UPI.")
        return True

class Factorypaymentmehod(ABC):

    factory = {}

    @classmethod
    def get_payment_object(cls, method_type, **kwargs):

        if method_type not in cls.factory:
            raise ValueError("Invalid payment method")

        return cls.factory[method_type](**kwargs)

class stripefactory(Factorypaymentmehod):

    factory = {
        "card": stripecardpayment,
        "upi": stripeupipayment
    }

class razorpayfactory(Factorypaymentmehod):

    factory = {
        "card": razorpaycardpayment,
        "upi": razorpayupipayment
    }

class Aggregator(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def call_get_payment_object(self, method_type, amount, **kwargs):
        pass

class stripeaggregator(Aggregator):

    def __init__(self):
        super().__init__("Stripe")
        self.processing_fee = 2.9

    def call_get_payment_object(self, method_type, amount, **kwargs):

        payment = stripefactory.get_payment_object(
            method_type,
            **kwargs
        )

        fee = amount * self.processing_fee / 100
        final_amount = amount + fee

        print(f"Processing fee: ₹{fee}")

        return payment.pay(final_amount)

class razorpayaggregator(Aggregator):

    def __init__(self):
        super().__init__("Razorpay")
        self.processing_fee = 2.0

    def call_get_payment_object(self, method_type, amount, **kwargs):

        payment = razorpayfactory.get_payment_object(
            method_type,
            **kwargs
        )

        fee = amount * self.processing_fee / 100
        final_amount = amount + fee

        print(f"Processing fee: ₹{fee}")

        return payment.pay(final_amount)

class aggregatorfactory:

    factory = {
        "stripe": stripeaggregator,
        "razorpay": razorpayaggregator
    }

    @classmethod
    def get_aggregator_object(cls, aggregator_name):

        if aggregator_name not in cls.factory:
            raise ValueError("Invalid aggregator")

        return cls.factory[aggregator_name]()

while True:

    print(" Payment Processing System")
    print("1. Stripe")
    print("2. Razorpay")
    print("3. Exit")

    choice = input("Choose aggregator: ")

    if choice == "3":
        print("Exiting...")
        break

    if choice == "1":
        aggregator_name = "stripe"

    elif choice == "2":
        aggregator_name = "razorpay"

    else:
        print("Invalid choice.")
        continue

    method = input("Enter payment method (card/upi): ").lower()

    try:
        amount = float(input("Enter amount: "))

        aggregator = aggregatorfactory.get_aggregator_object(
            aggregator_name
        )

        if method == "card":

            card_number = input("Enter card number: ")

            aggregator.call_get_payment_object(
                "card",
                amount,
                card_number=card_number
            )

        elif method == "upi":

            upi_id = input("Enter UPI ID: ")

            aggregator.call_get_payment_object(
                "upi",
                amount,
                upi_id=upi_id
            )

        else:
            print("Invalid payment method.")

    except ValueError as e:
        print("Error:", e)
