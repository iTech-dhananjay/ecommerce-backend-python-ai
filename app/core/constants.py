class Messages:
    EMAIL_EXISTS = "Email already registered."
    USER_NOT_FOUND = "User not found."
    PRODUCT_NOT_FOUND = "Product not available."
    ORDER_FAILED = "Unable to place order."
    PAYMENT_ERROR = "Payment could not be processed."
    LOGIN_FAILED = "Incorrect email or password."
    UNAUTHORIZED = "Unauthorized access."
    TOKEN_EXPIRED = "Token has expired."
    FORBIDDEN = "Access forbidden."

class Roles:
    SUPERADMIN = "superadmin"
    ADMIN = "admin"
    USER = "user"
    ALL = [SUPERADMIN, ADMIN, USER]


class Status:
    ORDER_PENDING = "pending"
    ORDER_PAID = "paid"
    ORDER_FAILED = "failed"