import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4201", "title": "Checkout scenario 4201", "data": {"sku": "SKU4201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4201@example.com", "threshold": 10}},
    {"id": "CHECKOUT-4202", "title": "Checkout scenario 4202", "data": {"sku": "SKU4202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4202@example.com", "threshold": 20}},
    {"id": "CHECKOUT-4203", "title": "Checkout scenario 4203", "data": {"sku": "SKU4203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4203@example.com", "threshold": 30}},
    {"id": "CHECKOUT-4204", "title": "Checkout scenario 4204", "data": {"sku": "SKU4204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4204@example.com", "threshold": 40}},
    {"id": "CHECKOUT-4205", "title": "Checkout scenario 4205", "data": {"sku": "SKU4205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4205@example.com", "threshold": 50}},
    {"id": "CHECKOUT-4206", "title": "Checkout scenario 4206", "data": {"sku": "SKU4206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4206@example.com", "threshold": 60}},
    {"id": "CHECKOUT-4207", "title": "Checkout scenario 4207", "data": {"sku": "SKU4207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4207@example.com", "threshold": 70}},
    {"id": "CHECKOUT-4208", "title": "Checkout scenario 4208", "data": {"sku": "SKU4208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4208@example.com", "threshold": 80}},
    {"id": "CHECKOUT-4209", "title": "Checkout scenario 4209", "data": {"sku": "SKU4209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4209@example.com", "threshold": 90}},
    {"id": "CHECKOUT-4210", "title": "Checkout scenario 4210", "data": {"sku": "SKU4210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4210@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
