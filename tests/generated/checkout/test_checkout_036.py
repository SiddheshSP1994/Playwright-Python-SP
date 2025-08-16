import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2101", "title": "Checkout scenario 2101", "data": {"sku": "SKU2101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2101@example.com", "threshold": 10}},
    {"id": "CHECKOUT-2102", "title": "Checkout scenario 2102", "data": {"sku": "SKU2102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2102@example.com", "threshold": 20}},
    {"id": "CHECKOUT-2103", "title": "Checkout scenario 2103", "data": {"sku": "SKU2103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2103@example.com", "threshold": 30}},
    {"id": "CHECKOUT-2104", "title": "Checkout scenario 2104", "data": {"sku": "SKU2104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2104@example.com", "threshold": 40}},
    {"id": "CHECKOUT-2105", "title": "Checkout scenario 2105", "data": {"sku": "SKU2105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2105@example.com", "threshold": 50}},
    {"id": "CHECKOUT-2106", "title": "Checkout scenario 2106", "data": {"sku": "SKU2106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2106@example.com", "threshold": 60}},
    {"id": "CHECKOUT-2107", "title": "Checkout scenario 2107", "data": {"sku": "SKU2107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2107@example.com", "threshold": 70}},
    {"id": "CHECKOUT-2108", "title": "Checkout scenario 2108", "data": {"sku": "SKU2108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2108@example.com", "threshold": 80}},
    {"id": "CHECKOUT-2109", "title": "Checkout scenario 2109", "data": {"sku": "SKU2109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2109@example.com", "threshold": 90}},
    {"id": "CHECKOUT-2110", "title": "Checkout scenario 2110", "data": {"sku": "SKU2110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2110@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
