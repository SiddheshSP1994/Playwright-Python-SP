import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4081", "title": "Checkout scenario 4081", "data": {"sku": "SKU4081", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4081@example.com", "threshold": 810}},
    {"id": "CHECKOUT-4082", "title": "Checkout scenario 4082", "data": {"sku": "SKU4082", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4082@example.com", "threshold": 820}},
    {"id": "CHECKOUT-4083", "title": "Checkout scenario 4083", "data": {"sku": "SKU4083", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4083@example.com", "threshold": 830}},
    {"id": "CHECKOUT-4084", "title": "Checkout scenario 4084", "data": {"sku": "SKU4084", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4084@example.com", "threshold": 840}},
    {"id": "CHECKOUT-4085", "title": "Checkout scenario 4085", "data": {"sku": "SKU4085", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4085@example.com", "threshold": 850}},
    {"id": "CHECKOUT-4086", "title": "Checkout scenario 4086", "data": {"sku": "SKU4086", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4086@example.com", "threshold": 860}},
    {"id": "CHECKOUT-4087", "title": "Checkout scenario 4087", "data": {"sku": "SKU4087", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4087@example.com", "threshold": 870}},
    {"id": "CHECKOUT-4088", "title": "Checkout scenario 4088", "data": {"sku": "SKU4088", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4088@example.com", "threshold": 880}},
    {"id": "CHECKOUT-4089", "title": "Checkout scenario 4089", "data": {"sku": "SKU4089", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4089@example.com", "threshold": 890}},
    {"id": "CHECKOUT-4090", "title": "Checkout scenario 4090", "data": {"sku": "SKU4090", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4090@example.com", "threshold": 900}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
