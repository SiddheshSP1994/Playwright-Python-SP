import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5101", "title": "Checkout scenario 5101", "data": {"sku": "SKU5101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5101@example.com", "threshold": 10}},
    {"id": "CHECKOUT-5102", "title": "Checkout scenario 5102", "data": {"sku": "SKU5102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5102@example.com", "threshold": 20}},
    {"id": "CHECKOUT-5103", "title": "Checkout scenario 5103", "data": {"sku": "SKU5103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5103@example.com", "threshold": 30}},
    {"id": "CHECKOUT-5104", "title": "Checkout scenario 5104", "data": {"sku": "SKU5104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5104@example.com", "threshold": 40}},
    {"id": "CHECKOUT-5105", "title": "Checkout scenario 5105", "data": {"sku": "SKU5105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5105@example.com", "threshold": 50}},
    {"id": "CHECKOUT-5106", "title": "Checkout scenario 5106", "data": {"sku": "SKU5106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5106@example.com", "threshold": 60}},
    {"id": "CHECKOUT-5107", "title": "Checkout scenario 5107", "data": {"sku": "SKU5107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5107@example.com", "threshold": 70}},
    {"id": "CHECKOUT-5108", "title": "Checkout scenario 5108", "data": {"sku": "SKU5108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5108@example.com", "threshold": 80}},
    {"id": "CHECKOUT-5109", "title": "Checkout scenario 5109", "data": {"sku": "SKU5109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5109@example.com", "threshold": 90}},
    {"id": "CHECKOUT-5110", "title": "Checkout scenario 5110", "data": {"sku": "SKU5110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5110@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
