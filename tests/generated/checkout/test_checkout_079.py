import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4681", "title": "Checkout scenario 4681", "data": {"sku": "SKU4681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4681@example.com", "threshold": 810}},
    {"id": "CHECKOUT-4682", "title": "Checkout scenario 4682", "data": {"sku": "SKU4682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4682@example.com", "threshold": 820}},
    {"id": "CHECKOUT-4683", "title": "Checkout scenario 4683", "data": {"sku": "SKU4683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4683@example.com", "threshold": 830}},
    {"id": "CHECKOUT-4684", "title": "Checkout scenario 4684", "data": {"sku": "SKU4684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4684@example.com", "threshold": 840}},
    {"id": "CHECKOUT-4685", "title": "Checkout scenario 4685", "data": {"sku": "SKU4685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4685@example.com", "threshold": 850}},
    {"id": "CHECKOUT-4686", "title": "Checkout scenario 4686", "data": {"sku": "SKU4686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4686@example.com", "threshold": 860}},
    {"id": "CHECKOUT-4687", "title": "Checkout scenario 4687", "data": {"sku": "SKU4687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4687@example.com", "threshold": 870}},
    {"id": "CHECKOUT-4688", "title": "Checkout scenario 4688", "data": {"sku": "SKU4688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4688@example.com", "threshold": 880}},
    {"id": "CHECKOUT-4689", "title": "Checkout scenario 4689", "data": {"sku": "SKU4689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4689@example.com", "threshold": 890}},
    {"id": "CHECKOUT-4690", "title": "Checkout scenario 4690", "data": {"sku": "SKU4690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4690@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
