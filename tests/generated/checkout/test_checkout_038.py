import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2221", "title": "Checkout scenario 2221", "data": {"sku": "SKU2221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2221@example.com", "threshold": 210}},
    {"id": "CHECKOUT-2222", "title": "Checkout scenario 2222", "data": {"sku": "SKU2222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2222@example.com", "threshold": 220}},
    {"id": "CHECKOUT-2223", "title": "Checkout scenario 2223", "data": {"sku": "SKU2223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2223@example.com", "threshold": 230}},
    {"id": "CHECKOUT-2224", "title": "Checkout scenario 2224", "data": {"sku": "SKU2224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2224@example.com", "threshold": 240}},
    {"id": "CHECKOUT-2225", "title": "Checkout scenario 2225", "data": {"sku": "SKU2225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2225@example.com", "threshold": 250}},
    {"id": "CHECKOUT-2226", "title": "Checkout scenario 2226", "data": {"sku": "SKU2226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2226@example.com", "threshold": 260}},
    {"id": "CHECKOUT-2227", "title": "Checkout scenario 2227", "data": {"sku": "SKU2227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2227@example.com", "threshold": 270}},
    {"id": "CHECKOUT-2228", "title": "Checkout scenario 2228", "data": {"sku": "SKU2228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2228@example.com", "threshold": 280}},
    {"id": "CHECKOUT-2229", "title": "Checkout scenario 2229", "data": {"sku": "SKU2229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2229@example.com", "threshold": 290}},
    {"id": "CHECKOUT-2230", "title": "Checkout scenario 2230", "data": {"sku": "SKU2230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2230@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
