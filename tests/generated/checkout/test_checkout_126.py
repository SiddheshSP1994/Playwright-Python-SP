import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7501", "title": "Checkout scenario 7501", "data": {"sku": "SKU7501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7501@example.com", "threshold": 10}},
    {"id": "CHECKOUT-7502", "title": "Checkout scenario 7502", "data": {"sku": "SKU7502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7502@example.com", "threshold": 20}},
    {"id": "CHECKOUT-7503", "title": "Checkout scenario 7503", "data": {"sku": "SKU7503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7503@example.com", "threshold": 30}},
    {"id": "CHECKOUT-7504", "title": "Checkout scenario 7504", "data": {"sku": "SKU7504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7504@example.com", "threshold": 40}},
    {"id": "CHECKOUT-7505", "title": "Checkout scenario 7505", "data": {"sku": "SKU7505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7505@example.com", "threshold": 50}},
    {"id": "CHECKOUT-7506", "title": "Checkout scenario 7506", "data": {"sku": "SKU7506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7506@example.com", "threshold": 60}},
    {"id": "CHECKOUT-7507", "title": "Checkout scenario 7507", "data": {"sku": "SKU7507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7507@example.com", "threshold": 70}},
    {"id": "CHECKOUT-7508", "title": "Checkout scenario 7508", "data": {"sku": "SKU7508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7508@example.com", "threshold": 80}},
    {"id": "CHECKOUT-7509", "title": "Checkout scenario 7509", "data": {"sku": "SKU7509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7509@example.com", "threshold": 90}},
    {"id": "CHECKOUT-7510", "title": "Checkout scenario 7510", "data": {"sku": "SKU7510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7510@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
