import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3421", "title": "Checkout scenario 3421", "data": {"sku": "SKU3421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3421@example.com", "threshold": 210}},
    {"id": "CHECKOUT-3422", "title": "Checkout scenario 3422", "data": {"sku": "SKU3422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3422@example.com", "threshold": 220}},
    {"id": "CHECKOUT-3423", "title": "Checkout scenario 3423", "data": {"sku": "SKU3423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3423@example.com", "threshold": 230}},
    {"id": "CHECKOUT-3424", "title": "Checkout scenario 3424", "data": {"sku": "SKU3424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3424@example.com", "threshold": 240}},
    {"id": "CHECKOUT-3425", "title": "Checkout scenario 3425", "data": {"sku": "SKU3425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3425@example.com", "threshold": 250}},
    {"id": "CHECKOUT-3426", "title": "Checkout scenario 3426", "data": {"sku": "SKU3426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3426@example.com", "threshold": 260}},
    {"id": "CHECKOUT-3427", "title": "Checkout scenario 3427", "data": {"sku": "SKU3427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3427@example.com", "threshold": 270}},
    {"id": "CHECKOUT-3428", "title": "Checkout scenario 3428", "data": {"sku": "SKU3428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3428@example.com", "threshold": 280}},
    {"id": "CHECKOUT-3429", "title": "Checkout scenario 3429", "data": {"sku": "SKU3429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3429@example.com", "threshold": 290}},
    {"id": "CHECKOUT-3430", "title": "Checkout scenario 3430", "data": {"sku": "SKU3430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3430@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
