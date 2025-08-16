import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1681", "title": "Checkout scenario 1681", "data": {"sku": "SKU1681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1681@example.com", "threshold": 810}},
    {"id": "CHECKOUT-1682", "title": "Checkout scenario 1682", "data": {"sku": "SKU1682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1682@example.com", "threshold": 820}},
    {"id": "CHECKOUT-1683", "title": "Checkout scenario 1683", "data": {"sku": "SKU1683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1683@example.com", "threshold": 830}},
    {"id": "CHECKOUT-1684", "title": "Checkout scenario 1684", "data": {"sku": "SKU1684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1684@example.com", "threshold": 840}},
    {"id": "CHECKOUT-1685", "title": "Checkout scenario 1685", "data": {"sku": "SKU1685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1685@example.com", "threshold": 850}},
    {"id": "CHECKOUT-1686", "title": "Checkout scenario 1686", "data": {"sku": "SKU1686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1686@example.com", "threshold": 860}},
    {"id": "CHECKOUT-1687", "title": "Checkout scenario 1687", "data": {"sku": "SKU1687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1687@example.com", "threshold": 870}},
    {"id": "CHECKOUT-1688", "title": "Checkout scenario 1688", "data": {"sku": "SKU1688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1688@example.com", "threshold": 880}},
    {"id": "CHECKOUT-1689", "title": "Checkout scenario 1689", "data": {"sku": "SKU1689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1689@example.com", "threshold": 890}},
    {"id": "CHECKOUT-1690", "title": "Checkout scenario 1690", "data": {"sku": "SKU1690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1690@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
