import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5581", "title": "Checkout scenario 5581", "data": {"sku": "SKU5581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5581@example.com", "threshold": 810}},
    {"id": "CHECKOUT-5582", "title": "Checkout scenario 5582", "data": {"sku": "SKU5582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5582@example.com", "threshold": 820}},
    {"id": "CHECKOUT-5583", "title": "Checkout scenario 5583", "data": {"sku": "SKU5583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5583@example.com", "threshold": 830}},
    {"id": "CHECKOUT-5584", "title": "Checkout scenario 5584", "data": {"sku": "SKU5584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5584@example.com", "threshold": 840}},
    {"id": "CHECKOUT-5585", "title": "Checkout scenario 5585", "data": {"sku": "SKU5585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5585@example.com", "threshold": 850}},
    {"id": "CHECKOUT-5586", "title": "Checkout scenario 5586", "data": {"sku": "SKU5586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5586@example.com", "threshold": 860}},
    {"id": "CHECKOUT-5587", "title": "Checkout scenario 5587", "data": {"sku": "SKU5587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5587@example.com", "threshold": 870}},
    {"id": "CHECKOUT-5588", "title": "Checkout scenario 5588", "data": {"sku": "SKU5588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5588@example.com", "threshold": 880}},
    {"id": "CHECKOUT-5589", "title": "Checkout scenario 5589", "data": {"sku": "SKU5589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5589@example.com", "threshold": 890}},
    {"id": "CHECKOUT-5590", "title": "Checkout scenario 5590", "data": {"sku": "SKU5590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5590@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
