import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8041", "title": "Checkout scenario 8041", "data": {"sku": "SKU8041", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8041@example.com", "threshold": 410}},
    {"id": "CHECKOUT-8042", "title": "Checkout scenario 8042", "data": {"sku": "SKU8042", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8042@example.com", "threshold": 420}},
    {"id": "CHECKOUT-8043", "title": "Checkout scenario 8043", "data": {"sku": "SKU8043", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8043@example.com", "threshold": 430}},
    {"id": "CHECKOUT-8044", "title": "Checkout scenario 8044", "data": {"sku": "SKU8044", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8044@example.com", "threshold": 440}},
    {"id": "CHECKOUT-8045", "title": "Checkout scenario 8045", "data": {"sku": "SKU8045", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8045@example.com", "threshold": 450}},
    {"id": "CHECKOUT-8046", "title": "Checkout scenario 8046", "data": {"sku": "SKU8046", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8046@example.com", "threshold": 460}},
    {"id": "CHECKOUT-8047", "title": "Checkout scenario 8047", "data": {"sku": "SKU8047", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8047@example.com", "threshold": 470}},
    {"id": "CHECKOUT-8048", "title": "Checkout scenario 8048", "data": {"sku": "SKU8048", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8048@example.com", "threshold": 480}},
    {"id": "CHECKOUT-8049", "title": "Checkout scenario 8049", "data": {"sku": "SKU8049", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8049@example.com", "threshold": 490}},
    {"id": "CHECKOUT-8050", "title": "Checkout scenario 8050", "data": {"sku": "SKU8050", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8050@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
