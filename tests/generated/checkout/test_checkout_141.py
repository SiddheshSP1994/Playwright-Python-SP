import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8401", "title": "Checkout scenario 8401", "data": {"sku": "SKU8401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8401@example.com", "threshold": 10}},
    {"id": "CHECKOUT-8402", "title": "Checkout scenario 8402", "data": {"sku": "SKU8402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8402@example.com", "threshold": 20}},
    {"id": "CHECKOUT-8403", "title": "Checkout scenario 8403", "data": {"sku": "SKU8403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8403@example.com", "threshold": 30}},
    {"id": "CHECKOUT-8404", "title": "Checkout scenario 8404", "data": {"sku": "SKU8404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8404@example.com", "threshold": 40}},
    {"id": "CHECKOUT-8405", "title": "Checkout scenario 8405", "data": {"sku": "SKU8405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8405@example.com", "threshold": 50}},
    {"id": "CHECKOUT-8406", "title": "Checkout scenario 8406", "data": {"sku": "SKU8406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8406@example.com", "threshold": 60}},
    {"id": "CHECKOUT-8407", "title": "Checkout scenario 8407", "data": {"sku": "SKU8407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8407@example.com", "threshold": 70}},
    {"id": "CHECKOUT-8408", "title": "Checkout scenario 8408", "data": {"sku": "SKU8408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8408@example.com", "threshold": 80}},
    {"id": "CHECKOUT-8409", "title": "Checkout scenario 8409", "data": {"sku": "SKU8409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8409@example.com", "threshold": 90}},
    {"id": "CHECKOUT-8410", "title": "Checkout scenario 8410", "data": {"sku": "SKU8410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8410@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
