import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5341", "title": "Checkout scenario 5341", "data": {"sku": "SKU5341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5341@example.com", "threshold": 410}},
    {"id": "CHECKOUT-5342", "title": "Checkout scenario 5342", "data": {"sku": "SKU5342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5342@example.com", "threshold": 420}},
    {"id": "CHECKOUT-5343", "title": "Checkout scenario 5343", "data": {"sku": "SKU5343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5343@example.com", "threshold": 430}},
    {"id": "CHECKOUT-5344", "title": "Checkout scenario 5344", "data": {"sku": "SKU5344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5344@example.com", "threshold": 440}},
    {"id": "CHECKOUT-5345", "title": "Checkout scenario 5345", "data": {"sku": "SKU5345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5345@example.com", "threshold": 450}},
    {"id": "CHECKOUT-5346", "title": "Checkout scenario 5346", "data": {"sku": "SKU5346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5346@example.com", "threshold": 460}},
    {"id": "CHECKOUT-5347", "title": "Checkout scenario 5347", "data": {"sku": "SKU5347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5347@example.com", "threshold": 470}},
    {"id": "CHECKOUT-5348", "title": "Checkout scenario 5348", "data": {"sku": "SKU5348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5348@example.com", "threshold": 480}},
    {"id": "CHECKOUT-5349", "title": "Checkout scenario 5349", "data": {"sku": "SKU5349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5349@example.com", "threshold": 490}},
    {"id": "CHECKOUT-5350", "title": "Checkout scenario 5350", "data": {"sku": "SKU5350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5350@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
