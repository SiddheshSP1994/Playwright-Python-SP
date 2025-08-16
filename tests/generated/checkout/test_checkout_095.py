import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5641", "title": "Checkout scenario 5641", "data": {"sku": "SKU5641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5641@example.com", "threshold": 410}},
    {"id": "CHECKOUT-5642", "title": "Checkout scenario 5642", "data": {"sku": "SKU5642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5642@example.com", "threshold": 420}},
    {"id": "CHECKOUT-5643", "title": "Checkout scenario 5643", "data": {"sku": "SKU5643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5643@example.com", "threshold": 430}},
    {"id": "CHECKOUT-5644", "title": "Checkout scenario 5644", "data": {"sku": "SKU5644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5644@example.com", "threshold": 440}},
    {"id": "CHECKOUT-5645", "title": "Checkout scenario 5645", "data": {"sku": "SKU5645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5645@example.com", "threshold": 450}},
    {"id": "CHECKOUT-5646", "title": "Checkout scenario 5646", "data": {"sku": "SKU5646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5646@example.com", "threshold": 460}},
    {"id": "CHECKOUT-5647", "title": "Checkout scenario 5647", "data": {"sku": "SKU5647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5647@example.com", "threshold": 470}},
    {"id": "CHECKOUT-5648", "title": "Checkout scenario 5648", "data": {"sku": "SKU5648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5648@example.com", "threshold": 480}},
    {"id": "CHECKOUT-5649", "title": "Checkout scenario 5649", "data": {"sku": "SKU5649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5649@example.com", "threshold": 490}},
    {"id": "CHECKOUT-5650", "title": "Checkout scenario 5650", "data": {"sku": "SKU5650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5650@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
