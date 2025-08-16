import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7681", "title": "Checkout scenario 7681", "data": {"sku": "SKU7681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7681@example.com", "threshold": 810}},
    {"id": "CHECKOUT-7682", "title": "Checkout scenario 7682", "data": {"sku": "SKU7682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7682@example.com", "threshold": 820}},
    {"id": "CHECKOUT-7683", "title": "Checkout scenario 7683", "data": {"sku": "SKU7683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7683@example.com", "threshold": 830}},
    {"id": "CHECKOUT-7684", "title": "Checkout scenario 7684", "data": {"sku": "SKU7684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7684@example.com", "threshold": 840}},
    {"id": "CHECKOUT-7685", "title": "Checkout scenario 7685", "data": {"sku": "SKU7685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7685@example.com", "threshold": 850}},
    {"id": "CHECKOUT-7686", "title": "Checkout scenario 7686", "data": {"sku": "SKU7686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7686@example.com", "threshold": 860}},
    {"id": "CHECKOUT-7687", "title": "Checkout scenario 7687", "data": {"sku": "SKU7687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7687@example.com", "threshold": 870}},
    {"id": "CHECKOUT-7688", "title": "Checkout scenario 7688", "data": {"sku": "SKU7688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7688@example.com", "threshold": 880}},
    {"id": "CHECKOUT-7689", "title": "Checkout scenario 7689", "data": {"sku": "SKU7689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7689@example.com", "threshold": 890}},
    {"id": "CHECKOUT-7690", "title": "Checkout scenario 7690", "data": {"sku": "SKU7690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7690@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
