import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2341", "title": "Checkout scenario 2341", "data": {"sku": "SKU2341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2341@example.com", "threshold": 410}},
    {"id": "CHECKOUT-2342", "title": "Checkout scenario 2342", "data": {"sku": "SKU2342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2342@example.com", "threshold": 420}},
    {"id": "CHECKOUT-2343", "title": "Checkout scenario 2343", "data": {"sku": "SKU2343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2343@example.com", "threshold": 430}},
    {"id": "CHECKOUT-2344", "title": "Checkout scenario 2344", "data": {"sku": "SKU2344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2344@example.com", "threshold": 440}},
    {"id": "CHECKOUT-2345", "title": "Checkout scenario 2345", "data": {"sku": "SKU2345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2345@example.com", "threshold": 450}},
    {"id": "CHECKOUT-2346", "title": "Checkout scenario 2346", "data": {"sku": "SKU2346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2346@example.com", "threshold": 460}},
    {"id": "CHECKOUT-2347", "title": "Checkout scenario 2347", "data": {"sku": "SKU2347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2347@example.com", "threshold": 470}},
    {"id": "CHECKOUT-2348", "title": "Checkout scenario 2348", "data": {"sku": "SKU2348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2348@example.com", "threshold": 480}},
    {"id": "CHECKOUT-2349", "title": "Checkout scenario 2349", "data": {"sku": "SKU2349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2349@example.com", "threshold": 490}},
    {"id": "CHECKOUT-2350", "title": "Checkout scenario 2350", "data": {"sku": "SKU2350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2350@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
