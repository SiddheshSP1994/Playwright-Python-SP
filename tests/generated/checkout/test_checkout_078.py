import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4621", "title": "Checkout scenario 4621", "data": {"sku": "SKU4621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4621@example.com", "threshold": 210}},
    {"id": "CHECKOUT-4622", "title": "Checkout scenario 4622", "data": {"sku": "SKU4622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4622@example.com", "threshold": 220}},
    {"id": "CHECKOUT-4623", "title": "Checkout scenario 4623", "data": {"sku": "SKU4623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4623@example.com", "threshold": 230}},
    {"id": "CHECKOUT-4624", "title": "Checkout scenario 4624", "data": {"sku": "SKU4624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4624@example.com", "threshold": 240}},
    {"id": "CHECKOUT-4625", "title": "Checkout scenario 4625", "data": {"sku": "SKU4625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4625@example.com", "threshold": 250}},
    {"id": "CHECKOUT-4626", "title": "Checkout scenario 4626", "data": {"sku": "SKU4626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4626@example.com", "threshold": 260}},
    {"id": "CHECKOUT-4627", "title": "Checkout scenario 4627", "data": {"sku": "SKU4627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4627@example.com", "threshold": 270}},
    {"id": "CHECKOUT-4628", "title": "Checkout scenario 4628", "data": {"sku": "SKU4628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4628@example.com", "threshold": 280}},
    {"id": "CHECKOUT-4629", "title": "Checkout scenario 4629", "data": {"sku": "SKU4629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4629@example.com", "threshold": 290}},
    {"id": "CHECKOUT-4630", "title": "Checkout scenario 4630", "data": {"sku": "SKU4630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4630@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
