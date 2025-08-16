import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5401", "title": "Checkout scenario 5401", "data": {"sku": "SKU5401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5401@example.com", "threshold": 10}},
    {"id": "CHECKOUT-5402", "title": "Checkout scenario 5402", "data": {"sku": "SKU5402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5402@example.com", "threshold": 20}},
    {"id": "CHECKOUT-5403", "title": "Checkout scenario 5403", "data": {"sku": "SKU5403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5403@example.com", "threshold": 30}},
    {"id": "CHECKOUT-5404", "title": "Checkout scenario 5404", "data": {"sku": "SKU5404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5404@example.com", "threshold": 40}},
    {"id": "CHECKOUT-5405", "title": "Checkout scenario 5405", "data": {"sku": "SKU5405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5405@example.com", "threshold": 50}},
    {"id": "CHECKOUT-5406", "title": "Checkout scenario 5406", "data": {"sku": "SKU5406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5406@example.com", "threshold": 60}},
    {"id": "CHECKOUT-5407", "title": "Checkout scenario 5407", "data": {"sku": "SKU5407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5407@example.com", "threshold": 70}},
    {"id": "CHECKOUT-5408", "title": "Checkout scenario 5408", "data": {"sku": "SKU5408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5408@example.com", "threshold": 80}},
    {"id": "CHECKOUT-5409", "title": "Checkout scenario 5409", "data": {"sku": "SKU5409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5409@example.com", "threshold": 90}},
    {"id": "CHECKOUT-5410", "title": "Checkout scenario 5410", "data": {"sku": "SKU5410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5410@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
