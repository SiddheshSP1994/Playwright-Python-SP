import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9121", "title": "Checkout scenario 9121", "data": {"sku": "SKU9121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9121@example.com", "threshold": 210}},
    {"id": "CHECKOUT-9122", "title": "Checkout scenario 9122", "data": {"sku": "SKU9122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9122@example.com", "threshold": 220}},
    {"id": "CHECKOUT-9123", "title": "Checkout scenario 9123", "data": {"sku": "SKU9123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9123@example.com", "threshold": 230}},
    {"id": "CHECKOUT-9124", "title": "Checkout scenario 9124", "data": {"sku": "SKU9124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9124@example.com", "threshold": 240}},
    {"id": "CHECKOUT-9125", "title": "Checkout scenario 9125", "data": {"sku": "SKU9125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9125@example.com", "threshold": 250}},
    {"id": "CHECKOUT-9126", "title": "Checkout scenario 9126", "data": {"sku": "SKU9126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9126@example.com", "threshold": 260}},
    {"id": "CHECKOUT-9127", "title": "Checkout scenario 9127", "data": {"sku": "SKU9127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9127@example.com", "threshold": 270}},
    {"id": "CHECKOUT-9128", "title": "Checkout scenario 9128", "data": {"sku": "SKU9128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9128@example.com", "threshold": 280}},
    {"id": "CHECKOUT-9129", "title": "Checkout scenario 9129", "data": {"sku": "SKU9129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9129@example.com", "threshold": 290}},
    {"id": "CHECKOUT-9130", "title": "Checkout scenario 9130", "data": {"sku": "SKU9130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9130@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
