import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3061", "title": "Checkout scenario 3061", "data": {"sku": "SKU3061", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3061@example.com", "threshold": 610}},
    {"id": "CHECKOUT-3062", "title": "Checkout scenario 3062", "data": {"sku": "SKU3062", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3062@example.com", "threshold": 620}},
    {"id": "CHECKOUT-3063", "title": "Checkout scenario 3063", "data": {"sku": "SKU3063", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3063@example.com", "threshold": 630}},
    {"id": "CHECKOUT-3064", "title": "Checkout scenario 3064", "data": {"sku": "SKU3064", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3064@example.com", "threshold": 640}},
    {"id": "CHECKOUT-3065", "title": "Checkout scenario 3065", "data": {"sku": "SKU3065", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3065@example.com", "threshold": 650}},
    {"id": "CHECKOUT-3066", "title": "Checkout scenario 3066", "data": {"sku": "SKU3066", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3066@example.com", "threshold": 660}},
    {"id": "CHECKOUT-3067", "title": "Checkout scenario 3067", "data": {"sku": "SKU3067", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3067@example.com", "threshold": 670}},
    {"id": "CHECKOUT-3068", "title": "Checkout scenario 3068", "data": {"sku": "SKU3068", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3068@example.com", "threshold": 680}},
    {"id": "CHECKOUT-3069", "title": "Checkout scenario 3069", "data": {"sku": "SKU3069", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3069@example.com", "threshold": 690}},
    {"id": "CHECKOUT-3070", "title": "Checkout scenario 3070", "data": {"sku": "SKU3070", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3070@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
