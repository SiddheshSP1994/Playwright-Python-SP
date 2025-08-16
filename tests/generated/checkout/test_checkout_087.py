import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5161", "title": "Checkout scenario 5161", "data": {"sku": "SKU5161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5161@example.com", "threshold": 610}},
    {"id": "CHECKOUT-5162", "title": "Checkout scenario 5162", "data": {"sku": "SKU5162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5162@example.com", "threshold": 620}},
    {"id": "CHECKOUT-5163", "title": "Checkout scenario 5163", "data": {"sku": "SKU5163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5163@example.com", "threshold": 630}},
    {"id": "CHECKOUT-5164", "title": "Checkout scenario 5164", "data": {"sku": "SKU5164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5164@example.com", "threshold": 640}},
    {"id": "CHECKOUT-5165", "title": "Checkout scenario 5165", "data": {"sku": "SKU5165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5165@example.com", "threshold": 650}},
    {"id": "CHECKOUT-5166", "title": "Checkout scenario 5166", "data": {"sku": "SKU5166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5166@example.com", "threshold": 660}},
    {"id": "CHECKOUT-5167", "title": "Checkout scenario 5167", "data": {"sku": "SKU5167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5167@example.com", "threshold": 670}},
    {"id": "CHECKOUT-5168", "title": "Checkout scenario 5168", "data": {"sku": "SKU5168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5168@example.com", "threshold": 680}},
    {"id": "CHECKOUT-5169", "title": "Checkout scenario 5169", "data": {"sku": "SKU5169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5169@example.com", "threshold": 690}},
    {"id": "CHECKOUT-5170", "title": "Checkout scenario 5170", "data": {"sku": "SKU5170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5170@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
