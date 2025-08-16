import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2461", "title": "Checkout scenario 2461", "data": {"sku": "SKU2461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2461@example.com", "threshold": 610}},
    {"id": "CHECKOUT-2462", "title": "Checkout scenario 2462", "data": {"sku": "SKU2462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2462@example.com", "threshold": 620}},
    {"id": "CHECKOUT-2463", "title": "Checkout scenario 2463", "data": {"sku": "SKU2463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2463@example.com", "threshold": 630}},
    {"id": "CHECKOUT-2464", "title": "Checkout scenario 2464", "data": {"sku": "SKU2464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2464@example.com", "threshold": 640}},
    {"id": "CHECKOUT-2465", "title": "Checkout scenario 2465", "data": {"sku": "SKU2465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2465@example.com", "threshold": 650}},
    {"id": "CHECKOUT-2466", "title": "Checkout scenario 2466", "data": {"sku": "SKU2466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2466@example.com", "threshold": 660}},
    {"id": "CHECKOUT-2467", "title": "Checkout scenario 2467", "data": {"sku": "SKU2467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2467@example.com", "threshold": 670}},
    {"id": "CHECKOUT-2468", "title": "Checkout scenario 2468", "data": {"sku": "SKU2468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2468@example.com", "threshold": 680}},
    {"id": "CHECKOUT-2469", "title": "Checkout scenario 2469", "data": {"sku": "SKU2469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2469@example.com", "threshold": 690}},
    {"id": "CHECKOUT-2470", "title": "Checkout scenario 2470", "data": {"sku": "SKU2470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2470@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
