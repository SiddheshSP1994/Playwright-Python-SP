import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8581", "title": "Checkout scenario 8581", "data": {"sku": "SKU8581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8581@example.com", "threshold": 810}},
    {"id": "CHECKOUT-8582", "title": "Checkout scenario 8582", "data": {"sku": "SKU8582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8582@example.com", "threshold": 820}},
    {"id": "CHECKOUT-8583", "title": "Checkout scenario 8583", "data": {"sku": "SKU8583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8583@example.com", "threshold": 830}},
    {"id": "CHECKOUT-8584", "title": "Checkout scenario 8584", "data": {"sku": "SKU8584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8584@example.com", "threshold": 840}},
    {"id": "CHECKOUT-8585", "title": "Checkout scenario 8585", "data": {"sku": "SKU8585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8585@example.com", "threshold": 850}},
    {"id": "CHECKOUT-8586", "title": "Checkout scenario 8586", "data": {"sku": "SKU8586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8586@example.com", "threshold": 860}},
    {"id": "CHECKOUT-8587", "title": "Checkout scenario 8587", "data": {"sku": "SKU8587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8587@example.com", "threshold": 870}},
    {"id": "CHECKOUT-8588", "title": "Checkout scenario 8588", "data": {"sku": "SKU8588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8588@example.com", "threshold": 880}},
    {"id": "CHECKOUT-8589", "title": "Checkout scenario 8589", "data": {"sku": "SKU8589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8589@example.com", "threshold": 890}},
    {"id": "CHECKOUT-8590", "title": "Checkout scenario 8590", "data": {"sku": "SKU8590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8590@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
