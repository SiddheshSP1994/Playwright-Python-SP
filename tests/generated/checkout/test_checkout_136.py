import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8101", "title": "Checkout scenario 8101", "data": {"sku": "SKU8101", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8101@example.com", "threshold": 10}},
    {"id": "CHECKOUT-8102", "title": "Checkout scenario 8102", "data": {"sku": "SKU8102", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8102@example.com", "threshold": 20}},
    {"id": "CHECKOUT-8103", "title": "Checkout scenario 8103", "data": {"sku": "SKU8103", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8103@example.com", "threshold": 30}},
    {"id": "CHECKOUT-8104", "title": "Checkout scenario 8104", "data": {"sku": "SKU8104", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8104@example.com", "threshold": 40}},
    {"id": "CHECKOUT-8105", "title": "Checkout scenario 8105", "data": {"sku": "SKU8105", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8105@example.com", "threshold": 50}},
    {"id": "CHECKOUT-8106", "title": "Checkout scenario 8106", "data": {"sku": "SKU8106", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8106@example.com", "threshold": 60}},
    {"id": "CHECKOUT-8107", "title": "Checkout scenario 8107", "data": {"sku": "SKU8107", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8107@example.com", "threshold": 70}},
    {"id": "CHECKOUT-8108", "title": "Checkout scenario 8108", "data": {"sku": "SKU8108", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8108@example.com", "threshold": 80}},
    {"id": "CHECKOUT-8109", "title": "Checkout scenario 8109", "data": {"sku": "SKU8109", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8109@example.com", "threshold": 90}},
    {"id": "CHECKOUT-8110", "title": "Checkout scenario 8110", "data": {"sku": "SKU8110", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8110@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
