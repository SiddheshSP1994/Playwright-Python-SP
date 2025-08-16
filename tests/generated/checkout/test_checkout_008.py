import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0421", "title": "Checkout scenario 421", "data": {"sku": "SKU421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user421@example.com", "threshold": 210}},
    {"id": "CHECKOUT-0422", "title": "Checkout scenario 422", "data": {"sku": "SKU422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user422@example.com", "threshold": 220}},
    {"id": "CHECKOUT-0423", "title": "Checkout scenario 423", "data": {"sku": "SKU423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user423@example.com", "threshold": 230}},
    {"id": "CHECKOUT-0424", "title": "Checkout scenario 424", "data": {"sku": "SKU424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user424@example.com", "threshold": 240}},
    {"id": "CHECKOUT-0425", "title": "Checkout scenario 425", "data": {"sku": "SKU425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user425@example.com", "threshold": 250}},
    {"id": "CHECKOUT-0426", "title": "Checkout scenario 426", "data": {"sku": "SKU426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user426@example.com", "threshold": 260}},
    {"id": "CHECKOUT-0427", "title": "Checkout scenario 427", "data": {"sku": "SKU427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user427@example.com", "threshold": 270}},
    {"id": "CHECKOUT-0428", "title": "Checkout scenario 428", "data": {"sku": "SKU428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user428@example.com", "threshold": 280}},
    {"id": "CHECKOUT-0429", "title": "Checkout scenario 429", "data": {"sku": "SKU429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user429@example.com", "threshold": 290}},
    {"id": "CHECKOUT-0430", "title": "Checkout scenario 430", "data": {"sku": "SKU430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user430@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
