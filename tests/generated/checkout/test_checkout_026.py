import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1501", "title": "Checkout scenario 1501", "data": {"sku": "SKU1501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1501@example.com", "threshold": 10}},
    {"id": "CHECKOUT-1502", "title": "Checkout scenario 1502", "data": {"sku": "SKU1502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1502@example.com", "threshold": 20}},
    {"id": "CHECKOUT-1503", "title": "Checkout scenario 1503", "data": {"sku": "SKU1503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1503@example.com", "threshold": 30}},
    {"id": "CHECKOUT-1504", "title": "Checkout scenario 1504", "data": {"sku": "SKU1504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1504@example.com", "threshold": 40}},
    {"id": "CHECKOUT-1505", "title": "Checkout scenario 1505", "data": {"sku": "SKU1505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1505@example.com", "threshold": 50}},
    {"id": "CHECKOUT-1506", "title": "Checkout scenario 1506", "data": {"sku": "SKU1506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1506@example.com", "threshold": 60}},
    {"id": "CHECKOUT-1507", "title": "Checkout scenario 1507", "data": {"sku": "SKU1507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1507@example.com", "threshold": 70}},
    {"id": "CHECKOUT-1508", "title": "Checkout scenario 1508", "data": {"sku": "SKU1508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1508@example.com", "threshold": 80}},
    {"id": "CHECKOUT-1509", "title": "Checkout scenario 1509", "data": {"sku": "SKU1509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1509@example.com", "threshold": 90}},
    {"id": "CHECKOUT-1510", "title": "Checkout scenario 1510", "data": {"sku": "SKU1510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1510@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
