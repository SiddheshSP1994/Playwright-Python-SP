import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5461", "title": "Checkout scenario 5461", "data": {"sku": "SKU5461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5461@example.com", "threshold": 610}},
    {"id": "CHECKOUT-5462", "title": "Checkout scenario 5462", "data": {"sku": "SKU5462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5462@example.com", "threshold": 620}},
    {"id": "CHECKOUT-5463", "title": "Checkout scenario 5463", "data": {"sku": "SKU5463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5463@example.com", "threshold": 630}},
    {"id": "CHECKOUT-5464", "title": "Checkout scenario 5464", "data": {"sku": "SKU5464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5464@example.com", "threshold": 640}},
    {"id": "CHECKOUT-5465", "title": "Checkout scenario 5465", "data": {"sku": "SKU5465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5465@example.com", "threshold": 650}},
    {"id": "CHECKOUT-5466", "title": "Checkout scenario 5466", "data": {"sku": "SKU5466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5466@example.com", "threshold": 660}},
    {"id": "CHECKOUT-5467", "title": "Checkout scenario 5467", "data": {"sku": "SKU5467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5467@example.com", "threshold": 670}},
    {"id": "CHECKOUT-5468", "title": "Checkout scenario 5468", "data": {"sku": "SKU5468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5468@example.com", "threshold": 680}},
    {"id": "CHECKOUT-5469", "title": "Checkout scenario 5469", "data": {"sku": "SKU5469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5469@example.com", "threshold": 690}},
    {"id": "CHECKOUT-5470", "title": "Checkout scenario 5470", "data": {"sku": "SKU5470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5470@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
