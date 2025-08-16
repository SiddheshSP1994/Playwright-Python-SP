import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6541", "title": "Checkout scenario 6541", "data": {"sku": "SKU6541", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6541@example.com", "threshold": 410}},
    {"id": "CHECKOUT-6542", "title": "Checkout scenario 6542", "data": {"sku": "SKU6542", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6542@example.com", "threshold": 420}},
    {"id": "CHECKOUT-6543", "title": "Checkout scenario 6543", "data": {"sku": "SKU6543", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6543@example.com", "threshold": 430}},
    {"id": "CHECKOUT-6544", "title": "Checkout scenario 6544", "data": {"sku": "SKU6544", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6544@example.com", "threshold": 440}},
    {"id": "CHECKOUT-6545", "title": "Checkout scenario 6545", "data": {"sku": "SKU6545", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6545@example.com", "threshold": 450}},
    {"id": "CHECKOUT-6546", "title": "Checkout scenario 6546", "data": {"sku": "SKU6546", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6546@example.com", "threshold": 460}},
    {"id": "CHECKOUT-6547", "title": "Checkout scenario 6547", "data": {"sku": "SKU6547", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6547@example.com", "threshold": 470}},
    {"id": "CHECKOUT-6548", "title": "Checkout scenario 6548", "data": {"sku": "SKU6548", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6548@example.com", "threshold": 480}},
    {"id": "CHECKOUT-6549", "title": "Checkout scenario 6549", "data": {"sku": "SKU6549", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6549@example.com", "threshold": 490}},
    {"id": "CHECKOUT-6550", "title": "Checkout scenario 6550", "data": {"sku": "SKU6550", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6550@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
