import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8341", "title": "Checkout scenario 8341", "data": {"sku": "SKU8341", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8341@example.com", "threshold": 410}},
    {"id": "CHECKOUT-8342", "title": "Checkout scenario 8342", "data": {"sku": "SKU8342", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8342@example.com", "threshold": 420}},
    {"id": "CHECKOUT-8343", "title": "Checkout scenario 8343", "data": {"sku": "SKU8343", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8343@example.com", "threshold": 430}},
    {"id": "CHECKOUT-8344", "title": "Checkout scenario 8344", "data": {"sku": "SKU8344", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8344@example.com", "threshold": 440}},
    {"id": "CHECKOUT-8345", "title": "Checkout scenario 8345", "data": {"sku": "SKU8345", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8345@example.com", "threshold": 450}},
    {"id": "CHECKOUT-8346", "title": "Checkout scenario 8346", "data": {"sku": "SKU8346", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8346@example.com", "threshold": 460}},
    {"id": "CHECKOUT-8347", "title": "Checkout scenario 8347", "data": {"sku": "SKU8347", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8347@example.com", "threshold": 470}},
    {"id": "CHECKOUT-8348", "title": "Checkout scenario 8348", "data": {"sku": "SKU8348", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8348@example.com", "threshold": 480}},
    {"id": "CHECKOUT-8349", "title": "Checkout scenario 8349", "data": {"sku": "SKU8349", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8349@example.com", "threshold": 490}},
    {"id": "CHECKOUT-8350", "title": "Checkout scenario 8350", "data": {"sku": "SKU8350", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8350@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
