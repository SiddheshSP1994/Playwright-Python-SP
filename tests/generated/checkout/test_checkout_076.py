import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4501", "title": "Checkout scenario 4501", "data": {"sku": "SKU4501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4501@example.com", "threshold": 10}},
    {"id": "CHECKOUT-4502", "title": "Checkout scenario 4502", "data": {"sku": "SKU4502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4502@example.com", "threshold": 20}},
    {"id": "CHECKOUT-4503", "title": "Checkout scenario 4503", "data": {"sku": "SKU4503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4503@example.com", "threshold": 30}},
    {"id": "CHECKOUT-4504", "title": "Checkout scenario 4504", "data": {"sku": "SKU4504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4504@example.com", "threshold": 40}},
    {"id": "CHECKOUT-4505", "title": "Checkout scenario 4505", "data": {"sku": "SKU4505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4505@example.com", "threshold": 50}},
    {"id": "CHECKOUT-4506", "title": "Checkout scenario 4506", "data": {"sku": "SKU4506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4506@example.com", "threshold": 60}},
    {"id": "CHECKOUT-4507", "title": "Checkout scenario 4507", "data": {"sku": "SKU4507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4507@example.com", "threshold": 70}},
    {"id": "CHECKOUT-4508", "title": "Checkout scenario 4508", "data": {"sku": "SKU4508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4508@example.com", "threshold": 80}},
    {"id": "CHECKOUT-4509", "title": "Checkout scenario 4509", "data": {"sku": "SKU4509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4509@example.com", "threshold": 90}},
    {"id": "CHECKOUT-4510", "title": "Checkout scenario 4510", "data": {"sku": "SKU4510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4510@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
