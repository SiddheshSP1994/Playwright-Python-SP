import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2401", "title": "Checkout scenario 2401", "data": {"sku": "SKU2401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2401@example.com", "threshold": 10}},
    {"id": "CHECKOUT-2402", "title": "Checkout scenario 2402", "data": {"sku": "SKU2402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2402@example.com", "threshold": 20}},
    {"id": "CHECKOUT-2403", "title": "Checkout scenario 2403", "data": {"sku": "SKU2403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2403@example.com", "threshold": 30}},
    {"id": "CHECKOUT-2404", "title": "Checkout scenario 2404", "data": {"sku": "SKU2404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2404@example.com", "threshold": 40}},
    {"id": "CHECKOUT-2405", "title": "Checkout scenario 2405", "data": {"sku": "SKU2405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2405@example.com", "threshold": 50}},
    {"id": "CHECKOUT-2406", "title": "Checkout scenario 2406", "data": {"sku": "SKU2406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2406@example.com", "threshold": 60}},
    {"id": "CHECKOUT-2407", "title": "Checkout scenario 2407", "data": {"sku": "SKU2407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2407@example.com", "threshold": 70}},
    {"id": "CHECKOUT-2408", "title": "Checkout scenario 2408", "data": {"sku": "SKU2408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2408@example.com", "threshold": 80}},
    {"id": "CHECKOUT-2409", "title": "Checkout scenario 2409", "data": {"sku": "SKU2409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2409@example.com", "threshold": 90}},
    {"id": "CHECKOUT-2410", "title": "Checkout scenario 2410", "data": {"sku": "SKU2410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2410@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
