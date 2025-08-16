import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2161", "title": "Checkout scenario 2161", "data": {"sku": "SKU2161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2161@example.com", "threshold": 610}},
    {"id": "CHECKOUT-2162", "title": "Checkout scenario 2162", "data": {"sku": "SKU2162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2162@example.com", "threshold": 620}},
    {"id": "CHECKOUT-2163", "title": "Checkout scenario 2163", "data": {"sku": "SKU2163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2163@example.com", "threshold": 630}},
    {"id": "CHECKOUT-2164", "title": "Checkout scenario 2164", "data": {"sku": "SKU2164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2164@example.com", "threshold": 640}},
    {"id": "CHECKOUT-2165", "title": "Checkout scenario 2165", "data": {"sku": "SKU2165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2165@example.com", "threshold": 650}},
    {"id": "CHECKOUT-2166", "title": "Checkout scenario 2166", "data": {"sku": "SKU2166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2166@example.com", "threshold": 660}},
    {"id": "CHECKOUT-2167", "title": "Checkout scenario 2167", "data": {"sku": "SKU2167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2167@example.com", "threshold": 670}},
    {"id": "CHECKOUT-2168", "title": "Checkout scenario 2168", "data": {"sku": "SKU2168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2168@example.com", "threshold": 680}},
    {"id": "CHECKOUT-2169", "title": "Checkout scenario 2169", "data": {"sku": "SKU2169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2169@example.com", "threshold": 690}},
    {"id": "CHECKOUT-2170", "title": "Checkout scenario 2170", "data": {"sku": "SKU2170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2170@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
