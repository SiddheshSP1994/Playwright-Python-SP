import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6061", "title": "Checkout scenario 6061", "data": {"sku": "SKU6061", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6061@example.com", "threshold": 610}},
    {"id": "CHECKOUT-6062", "title": "Checkout scenario 6062", "data": {"sku": "SKU6062", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6062@example.com", "threshold": 620}},
    {"id": "CHECKOUT-6063", "title": "Checkout scenario 6063", "data": {"sku": "SKU6063", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6063@example.com", "threshold": 630}},
    {"id": "CHECKOUT-6064", "title": "Checkout scenario 6064", "data": {"sku": "SKU6064", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6064@example.com", "threshold": 640}},
    {"id": "CHECKOUT-6065", "title": "Checkout scenario 6065", "data": {"sku": "SKU6065", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6065@example.com", "threshold": 650}},
    {"id": "CHECKOUT-6066", "title": "Checkout scenario 6066", "data": {"sku": "SKU6066", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6066@example.com", "threshold": 660}},
    {"id": "CHECKOUT-6067", "title": "Checkout scenario 6067", "data": {"sku": "SKU6067", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6067@example.com", "threshold": 670}},
    {"id": "CHECKOUT-6068", "title": "Checkout scenario 6068", "data": {"sku": "SKU6068", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6068@example.com", "threshold": 680}},
    {"id": "CHECKOUT-6069", "title": "Checkout scenario 6069", "data": {"sku": "SKU6069", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6069@example.com", "threshold": 690}},
    {"id": "CHECKOUT-6070", "title": "Checkout scenario 6070", "data": {"sku": "SKU6070", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6070@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
