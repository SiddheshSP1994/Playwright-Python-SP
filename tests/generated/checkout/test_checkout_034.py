import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1981", "title": "Checkout scenario 1981", "data": {"sku": "SKU1981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1981@example.com", "threshold": 810}},
    {"id": "CHECKOUT-1982", "title": "Checkout scenario 1982", "data": {"sku": "SKU1982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1982@example.com", "threshold": 820}},
    {"id": "CHECKOUT-1983", "title": "Checkout scenario 1983", "data": {"sku": "SKU1983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1983@example.com", "threshold": 830}},
    {"id": "CHECKOUT-1984", "title": "Checkout scenario 1984", "data": {"sku": "SKU1984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1984@example.com", "threshold": 840}},
    {"id": "CHECKOUT-1985", "title": "Checkout scenario 1985", "data": {"sku": "SKU1985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1985@example.com", "threshold": 850}},
    {"id": "CHECKOUT-1986", "title": "Checkout scenario 1986", "data": {"sku": "SKU1986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1986@example.com", "threshold": 860}},
    {"id": "CHECKOUT-1987", "title": "Checkout scenario 1987", "data": {"sku": "SKU1987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1987@example.com", "threshold": 870}},
    {"id": "CHECKOUT-1988", "title": "Checkout scenario 1988", "data": {"sku": "SKU1988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1988@example.com", "threshold": 880}},
    {"id": "CHECKOUT-1989", "title": "Checkout scenario 1989", "data": {"sku": "SKU1989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1989@example.com", "threshold": 890}},
    {"id": "CHECKOUT-1990", "title": "Checkout scenario 1990", "data": {"sku": "SKU1990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1990@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
