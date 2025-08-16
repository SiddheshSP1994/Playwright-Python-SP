import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4141", "title": "Checkout scenario 4141", "data": {"sku": "SKU4141", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4141@example.com", "threshold": 410}},
    {"id": "CHECKOUT-4142", "title": "Checkout scenario 4142", "data": {"sku": "SKU4142", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4142@example.com", "threshold": 420}},
    {"id": "CHECKOUT-4143", "title": "Checkout scenario 4143", "data": {"sku": "SKU4143", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4143@example.com", "threshold": 430}},
    {"id": "CHECKOUT-4144", "title": "Checkout scenario 4144", "data": {"sku": "SKU4144", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4144@example.com", "threshold": 440}},
    {"id": "CHECKOUT-4145", "title": "Checkout scenario 4145", "data": {"sku": "SKU4145", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4145@example.com", "threshold": 450}},
    {"id": "CHECKOUT-4146", "title": "Checkout scenario 4146", "data": {"sku": "SKU4146", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4146@example.com", "threshold": 460}},
    {"id": "CHECKOUT-4147", "title": "Checkout scenario 4147", "data": {"sku": "SKU4147", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4147@example.com", "threshold": 470}},
    {"id": "CHECKOUT-4148", "title": "Checkout scenario 4148", "data": {"sku": "SKU4148", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4148@example.com", "threshold": 480}},
    {"id": "CHECKOUT-4149", "title": "Checkout scenario 4149", "data": {"sku": "SKU4149", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4149@example.com", "threshold": 490}},
    {"id": "CHECKOUT-4150", "title": "Checkout scenario 4150", "data": {"sku": "SKU4150", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4150@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
