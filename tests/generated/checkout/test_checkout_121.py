import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7201", "title": "Checkout scenario 7201", "data": {"sku": "SKU7201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7201@example.com", "threshold": 10}},
    {"id": "CHECKOUT-7202", "title": "Checkout scenario 7202", "data": {"sku": "SKU7202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7202@example.com", "threshold": 20}},
    {"id": "CHECKOUT-7203", "title": "Checkout scenario 7203", "data": {"sku": "SKU7203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7203@example.com", "threshold": 30}},
    {"id": "CHECKOUT-7204", "title": "Checkout scenario 7204", "data": {"sku": "SKU7204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7204@example.com", "threshold": 40}},
    {"id": "CHECKOUT-7205", "title": "Checkout scenario 7205", "data": {"sku": "SKU7205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7205@example.com", "threshold": 50}},
    {"id": "CHECKOUT-7206", "title": "Checkout scenario 7206", "data": {"sku": "SKU7206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7206@example.com", "threshold": 60}},
    {"id": "CHECKOUT-7207", "title": "Checkout scenario 7207", "data": {"sku": "SKU7207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7207@example.com", "threshold": 70}},
    {"id": "CHECKOUT-7208", "title": "Checkout scenario 7208", "data": {"sku": "SKU7208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7208@example.com", "threshold": 80}},
    {"id": "CHECKOUT-7209", "title": "Checkout scenario 7209", "data": {"sku": "SKU7209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7209@example.com", "threshold": 90}},
    {"id": "CHECKOUT-7210", "title": "Checkout scenario 7210", "data": {"sku": "SKU7210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7210@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
