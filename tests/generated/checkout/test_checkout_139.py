import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8281", "title": "Checkout scenario 8281", "data": {"sku": "SKU8281", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8281@example.com", "threshold": 810}},
    {"id": "CHECKOUT-8282", "title": "Checkout scenario 8282", "data": {"sku": "SKU8282", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8282@example.com", "threshold": 820}},
    {"id": "CHECKOUT-8283", "title": "Checkout scenario 8283", "data": {"sku": "SKU8283", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8283@example.com", "threshold": 830}},
    {"id": "CHECKOUT-8284", "title": "Checkout scenario 8284", "data": {"sku": "SKU8284", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8284@example.com", "threshold": 840}},
    {"id": "CHECKOUT-8285", "title": "Checkout scenario 8285", "data": {"sku": "SKU8285", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8285@example.com", "threshold": 850}},
    {"id": "CHECKOUT-8286", "title": "Checkout scenario 8286", "data": {"sku": "SKU8286", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8286@example.com", "threshold": 860}},
    {"id": "CHECKOUT-8287", "title": "Checkout scenario 8287", "data": {"sku": "SKU8287", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8287@example.com", "threshold": 870}},
    {"id": "CHECKOUT-8288", "title": "Checkout scenario 8288", "data": {"sku": "SKU8288", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8288@example.com", "threshold": 880}},
    {"id": "CHECKOUT-8289", "title": "Checkout scenario 8289", "data": {"sku": "SKU8289", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8289@example.com", "threshold": 890}},
    {"id": "CHECKOUT-8290", "title": "Checkout scenario 8290", "data": {"sku": "SKU8290", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8290@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
