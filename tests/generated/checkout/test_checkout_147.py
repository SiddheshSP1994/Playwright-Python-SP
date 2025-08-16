import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8761", "title": "Checkout scenario 8761", "data": {"sku": "SKU8761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8761@example.com", "threshold": 610}},
    {"id": "CHECKOUT-8762", "title": "Checkout scenario 8762", "data": {"sku": "SKU8762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8762@example.com", "threshold": 620}},
    {"id": "CHECKOUT-8763", "title": "Checkout scenario 8763", "data": {"sku": "SKU8763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8763@example.com", "threshold": 630}},
    {"id": "CHECKOUT-8764", "title": "Checkout scenario 8764", "data": {"sku": "SKU8764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8764@example.com", "threshold": 640}},
    {"id": "CHECKOUT-8765", "title": "Checkout scenario 8765", "data": {"sku": "SKU8765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8765@example.com", "threshold": 650}},
    {"id": "CHECKOUT-8766", "title": "Checkout scenario 8766", "data": {"sku": "SKU8766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8766@example.com", "threshold": 660}},
    {"id": "CHECKOUT-8767", "title": "Checkout scenario 8767", "data": {"sku": "SKU8767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8767@example.com", "threshold": 670}},
    {"id": "CHECKOUT-8768", "title": "Checkout scenario 8768", "data": {"sku": "SKU8768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8768@example.com", "threshold": 680}},
    {"id": "CHECKOUT-8769", "title": "Checkout scenario 8769", "data": {"sku": "SKU8769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8769@example.com", "threshold": 690}},
    {"id": "CHECKOUT-8770", "title": "Checkout scenario 8770", "data": {"sku": "SKU8770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8770@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
