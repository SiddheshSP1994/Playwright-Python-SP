import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1201", "title": "Checkout scenario 1201", "data": {"sku": "SKU1201", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1201@example.com", "threshold": 10}},
    {"id": "CHECKOUT-1202", "title": "Checkout scenario 1202", "data": {"sku": "SKU1202", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1202@example.com", "threshold": 20}},
    {"id": "CHECKOUT-1203", "title": "Checkout scenario 1203", "data": {"sku": "SKU1203", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1203@example.com", "threshold": 30}},
    {"id": "CHECKOUT-1204", "title": "Checkout scenario 1204", "data": {"sku": "SKU1204", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1204@example.com", "threshold": 40}},
    {"id": "CHECKOUT-1205", "title": "Checkout scenario 1205", "data": {"sku": "SKU1205", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1205@example.com", "threshold": 50}},
    {"id": "CHECKOUT-1206", "title": "Checkout scenario 1206", "data": {"sku": "SKU1206", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1206@example.com", "threshold": 60}},
    {"id": "CHECKOUT-1207", "title": "Checkout scenario 1207", "data": {"sku": "SKU1207", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1207@example.com", "threshold": 70}},
    {"id": "CHECKOUT-1208", "title": "Checkout scenario 1208", "data": {"sku": "SKU1208", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1208@example.com", "threshold": 80}},
    {"id": "CHECKOUT-1209", "title": "Checkout scenario 1209", "data": {"sku": "SKU1209", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1209@example.com", "threshold": 90}},
    {"id": "CHECKOUT-1210", "title": "Checkout scenario 1210", "data": {"sku": "SKU1210", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1210@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
