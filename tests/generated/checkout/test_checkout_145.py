import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8641", "title": "Checkout scenario 8641", "data": {"sku": "SKU8641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8641@example.com", "threshold": 410}},
    {"id": "CHECKOUT-8642", "title": "Checkout scenario 8642", "data": {"sku": "SKU8642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8642@example.com", "threshold": 420}},
    {"id": "CHECKOUT-8643", "title": "Checkout scenario 8643", "data": {"sku": "SKU8643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8643@example.com", "threshold": 430}},
    {"id": "CHECKOUT-8644", "title": "Checkout scenario 8644", "data": {"sku": "SKU8644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8644@example.com", "threshold": 440}},
    {"id": "CHECKOUT-8645", "title": "Checkout scenario 8645", "data": {"sku": "SKU8645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8645@example.com", "threshold": 450}},
    {"id": "CHECKOUT-8646", "title": "Checkout scenario 8646", "data": {"sku": "SKU8646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8646@example.com", "threshold": 460}},
    {"id": "CHECKOUT-8647", "title": "Checkout scenario 8647", "data": {"sku": "SKU8647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8647@example.com", "threshold": 470}},
    {"id": "CHECKOUT-8648", "title": "Checkout scenario 8648", "data": {"sku": "SKU8648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8648@example.com", "threshold": 480}},
    {"id": "CHECKOUT-8649", "title": "Checkout scenario 8649", "data": {"sku": "SKU8649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8649@example.com", "threshold": 490}},
    {"id": "CHECKOUT-8650", "title": "Checkout scenario 8650", "data": {"sku": "SKU8650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8650@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
