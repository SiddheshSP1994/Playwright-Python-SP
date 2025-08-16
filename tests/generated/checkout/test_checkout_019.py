import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1081", "title": "Checkout scenario 1081", "data": {"sku": "SKU1081", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1081@example.com", "threshold": 810}},
    {"id": "CHECKOUT-1082", "title": "Checkout scenario 1082", "data": {"sku": "SKU1082", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1082@example.com", "threshold": 820}},
    {"id": "CHECKOUT-1083", "title": "Checkout scenario 1083", "data": {"sku": "SKU1083", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1083@example.com", "threshold": 830}},
    {"id": "CHECKOUT-1084", "title": "Checkout scenario 1084", "data": {"sku": "SKU1084", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1084@example.com", "threshold": 840}},
    {"id": "CHECKOUT-1085", "title": "Checkout scenario 1085", "data": {"sku": "SKU1085", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1085@example.com", "threshold": 850}},
    {"id": "CHECKOUT-1086", "title": "Checkout scenario 1086", "data": {"sku": "SKU1086", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1086@example.com", "threshold": 860}},
    {"id": "CHECKOUT-1087", "title": "Checkout scenario 1087", "data": {"sku": "SKU1087", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1087@example.com", "threshold": 870}},
    {"id": "CHECKOUT-1088", "title": "Checkout scenario 1088", "data": {"sku": "SKU1088", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1088@example.com", "threshold": 880}},
    {"id": "CHECKOUT-1089", "title": "Checkout scenario 1089", "data": {"sku": "SKU1089", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1089@example.com", "threshold": 890}},
    {"id": "CHECKOUT-1090", "title": "Checkout scenario 1090", "data": {"sku": "SKU1090", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1090@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
