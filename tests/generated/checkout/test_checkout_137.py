import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8161", "title": "Checkout scenario 8161", "data": {"sku": "SKU8161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8161@example.com", "threshold": 610}},
    {"id": "CHECKOUT-8162", "title": "Checkout scenario 8162", "data": {"sku": "SKU8162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8162@example.com", "threshold": 620}},
    {"id": "CHECKOUT-8163", "title": "Checkout scenario 8163", "data": {"sku": "SKU8163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8163@example.com", "threshold": 630}},
    {"id": "CHECKOUT-8164", "title": "Checkout scenario 8164", "data": {"sku": "SKU8164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8164@example.com", "threshold": 640}},
    {"id": "CHECKOUT-8165", "title": "Checkout scenario 8165", "data": {"sku": "SKU8165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8165@example.com", "threshold": 650}},
    {"id": "CHECKOUT-8166", "title": "Checkout scenario 8166", "data": {"sku": "SKU8166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8166@example.com", "threshold": 660}},
    {"id": "CHECKOUT-8167", "title": "Checkout scenario 8167", "data": {"sku": "SKU8167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8167@example.com", "threshold": 670}},
    {"id": "CHECKOUT-8168", "title": "Checkout scenario 8168", "data": {"sku": "SKU8168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8168@example.com", "threshold": 680}},
    {"id": "CHECKOUT-8169", "title": "Checkout scenario 8169", "data": {"sku": "SKU8169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8169@example.com", "threshold": 690}},
    {"id": "CHECKOUT-8170", "title": "Checkout scenario 8170", "data": {"sku": "SKU8170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8170@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
