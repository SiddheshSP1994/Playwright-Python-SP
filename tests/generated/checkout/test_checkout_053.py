import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3121", "title": "Checkout scenario 3121", "data": {"sku": "SKU3121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3121@example.com", "threshold": 210}},
    {"id": "CHECKOUT-3122", "title": "Checkout scenario 3122", "data": {"sku": "SKU3122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3122@example.com", "threshold": 220}},
    {"id": "CHECKOUT-3123", "title": "Checkout scenario 3123", "data": {"sku": "SKU3123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3123@example.com", "threshold": 230}},
    {"id": "CHECKOUT-3124", "title": "Checkout scenario 3124", "data": {"sku": "SKU3124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3124@example.com", "threshold": 240}},
    {"id": "CHECKOUT-3125", "title": "Checkout scenario 3125", "data": {"sku": "SKU3125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3125@example.com", "threshold": 250}},
    {"id": "CHECKOUT-3126", "title": "Checkout scenario 3126", "data": {"sku": "SKU3126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3126@example.com", "threshold": 260}},
    {"id": "CHECKOUT-3127", "title": "Checkout scenario 3127", "data": {"sku": "SKU3127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3127@example.com", "threshold": 270}},
    {"id": "CHECKOUT-3128", "title": "Checkout scenario 3128", "data": {"sku": "SKU3128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3128@example.com", "threshold": 280}},
    {"id": "CHECKOUT-3129", "title": "Checkout scenario 3129", "data": {"sku": "SKU3129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3129@example.com", "threshold": 290}},
    {"id": "CHECKOUT-3130", "title": "Checkout scenario 3130", "data": {"sku": "SKU3130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3130@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
