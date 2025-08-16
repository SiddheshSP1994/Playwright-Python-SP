import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9061", "title": "Checkout scenario 9061", "data": {"sku": "SKU9061", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9061@example.com", "threshold": 610}},
    {"id": "CHECKOUT-9062", "title": "Checkout scenario 9062", "data": {"sku": "SKU9062", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9062@example.com", "threshold": 620}},
    {"id": "CHECKOUT-9063", "title": "Checkout scenario 9063", "data": {"sku": "SKU9063", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9063@example.com", "threshold": 630}},
    {"id": "CHECKOUT-9064", "title": "Checkout scenario 9064", "data": {"sku": "SKU9064", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9064@example.com", "threshold": 640}},
    {"id": "CHECKOUT-9065", "title": "Checkout scenario 9065", "data": {"sku": "SKU9065", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9065@example.com", "threshold": 650}},
    {"id": "CHECKOUT-9066", "title": "Checkout scenario 9066", "data": {"sku": "SKU9066", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9066@example.com", "threshold": 660}},
    {"id": "CHECKOUT-9067", "title": "Checkout scenario 9067", "data": {"sku": "SKU9067", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9067@example.com", "threshold": 670}},
    {"id": "CHECKOUT-9068", "title": "Checkout scenario 9068", "data": {"sku": "SKU9068", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9068@example.com", "threshold": 680}},
    {"id": "CHECKOUT-9069", "title": "Checkout scenario 9069", "data": {"sku": "SKU9069", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9069@example.com", "threshold": 690}},
    {"id": "CHECKOUT-9070", "title": "Checkout scenario 9070", "data": {"sku": "SKU9070", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9070@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
